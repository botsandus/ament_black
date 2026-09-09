# Copyright 2023 Dexory (c)

import os
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET

import pytest


@pytest.mark.ament_black
@pytest.mark.linter
def test_ament_black():
    rc = os.system('ament_black --help')
    assert rc == 0, 'ament-black python package not properly installed'


@pytest.fixture
def run_cli(tmp_path, monkeypatch):
    package_root = str(Path(__file__).resolve().parents[1])
    monkeypatch.setenv('PYTHONPATH', package_root + os.pathsep + os.environ.get('PYTHONPATH', ''))
    monkeypatch.setenv('BLACK_NUM_WORKERS', '2')

    def run(*args):
        return subprocess.run(
            [sys.executable, '-m', 'ament_black.main', *args],
            cwd=tmp_path,
            capture_output=True,
            text=True,
            timeout=60,
        )

    return run


@pytest.mark.parametrize('file_count', [1, 2])
def test_check_reports_formatting_failures(tmp_path, run_cli, file_count):
    sources = [tmp_path / f'sample {index}.py' for index in range(file_count)]
    for source in sources:
        source.write_text('value=1\n')
    result_file = tmp_path / 'result.xml'

    result = run_cli('--xunit-file', str(result_file), *map(str, sources))

    assert result.returncode == 1, result.stdout + result.stderr
    assert 'No problems found' not in result.stdout
    report = ET.parse(result_file).getroot()
    assert int(report.attrib['failures']) == file_count
    assert len(report.findall('testcase/failure')) == file_count
    for source in sources:
        assert source.read_text() == 'value=1\n'


def test_check_formatted_files(tmp_path, run_cli):
    for name in ['first.py', 'second.py']:
        (tmp_path / name).write_text('value = 1\n')
    result_file = tmp_path / 'result.xml'

    result = run_cli('--xunit-file', str(result_file), '.')

    assert result.returncode == 0, result.stdout + result.stderr
    assert 'No problems found' in result.stdout
    report = ET.parse(result_file).getroot()
    assert report.attrib['failures'] == '0'
    assert report.attrib['errors'] == '0'


def test_syntax_error_is_reported(tmp_path, run_cli):
    (tmp_path / 'invalid.py').write_text('def broken(:\n')
    (tmp_path / 'valid.py').write_text('value = 1\n')
    result_file = tmp_path / 'result.xml'

    result = run_cli('--xunit-file', str(result_file), '.')

    assert result.returncode == 123, result.stdout + result.stderr
    assert 'No problems found' not in result.stdout
    report = ET.parse(result_file).getroot()
    assert report.attrib['errors'] == '1'
    assert 'Cannot parse' in report.find('testcase/error').text


def test_reformat_multiple_files(tmp_path, run_cli):
    sources = [tmp_path / name for name in ['first.py', 'second.py']]
    for source in sources:
        source.write_text('value=1\n')
    result_file = tmp_path / 'result.xml'

    result = run_cli('--reformat', '--xunit-file', str(result_file), *map(str, sources))

    assert result.returncode == 0, result.stdout + result.stderr
    for source in sources:
        assert source.read_text() == 'value = 1\n'
    report = ET.parse(result_file).getroot()
    assert report.attrib['failures'] == '0'
    assert report.attrib['errors'] == '0'
    assert run_cli(*map(str, sources)).returncode == 0


def test_custom_config_is_used(tmp_path, run_cli):
    config = tmp_path / 'black.toml'
    config.write_text('[tool.black]\nskip-string-normalization = true\n')
    for name in ['first.py', 'second.py']:
        (tmp_path / name).write_text("value = 'text'\n")

    assert run_cli('.').returncode == 1
    result = run_cli('--config', str(config), '.')

    assert result.returncode == 0, result.stdout + result.stderr


def test_invalid_config_is_reported(tmp_path, run_cli):
    config = tmp_path / 'black.toml'
    config.write_text('[tool.black\n')
    (tmp_path / 'sample.py').write_text('value = 1\n')
    result_file = tmp_path / 'result.xml'

    result = run_cli('--config', str(config), '--xunit-file', str(result_file), '.')

    assert result.returncode != 0
    assert 'No problems found' not in result.stdout
    report = ET.parse(result_file).getroot()
    assert report.attrib['errors'] == '1'
    assert report.find('testcase/error') is not None
