^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ament_cmake_black
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.2.2 (2023-10-11)
------------------
* Nacho/fix ci tests (`#5 <https://github.com/botsandus/ament_black/issues/5>`_)
  * Add missing test dependency
  * pre-commit
  * Add pre-commit workflow
  * Add CLI test to make sure the package has been properly installed
  * Remove ament hooks
  * Add missing apt-python dependency
  Not sure if it's necessary ...
  * Fix CI pre-commit
  The CI error was fixed in: https://github.com/psf/black/issues/2964
  Thus, we need black >22.3.0
* Contributors: Ignacio Vizzo

0.2.1 (2023-10-11)
------------------
* Fix multiple files reformat crash and improve file detection using black
* Contributors: Ignacio Vizzo

0.2.0 (2023-10-09)
------------------------
* Create a new release for a renewed and mantained package
* Contributors: Ignacio Vizzo [Dexory]

0.1.0 (2022-05-31)
------------------
* Initial release.
