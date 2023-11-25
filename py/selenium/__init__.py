# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import os
import sys

# parent_directory = os.path.abspath("..")
# sys.path.append(parent_directory)
#
# from parent_directory.version import SE_VERSION
# path to version py/version.py
# path to __init__.py py/selenium/__init__.py
# I want to import SE_VERSION from py/version.py to py/selenium/__init__.py
# I have to add parent_directory to sys.path
# and then I can import SE_VERSION from py/version.py to py/selenium/__init__.py

parent_directory = os.path.abspath("..")
sys.path.append(parent_directory)

from parent_directory.version import SE_VERSION

__version__ = SE_VERSION
