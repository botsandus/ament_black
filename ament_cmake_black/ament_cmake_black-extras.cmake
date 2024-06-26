# Copyright 2019 Picknik Robotics
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#
# copied from ament_cmake_black/ament_cmake_black-extras.cmake
# cmake-format: off
find_package(ament_cmake_test QUIET REQUIRED)
include("${ament_cmake_black_DIR}/ament_black.cmake")
ament_register_extension("ament_lint_auto" "ament_cmake_black" "ament_cmake_black_lint_hook.cmake")
# cmake-format: on
