"""LICENSE
Copyright 2019 Hermann Krumrey <hermann@krumreyh.com>

This file is part of status-page.

status-page is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

status-page is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with status-page.  If not, see <http://www.gnu.org/licenses/>.
LICENSE"""

import os
from status_page.utils.env import load_secrets


secrets_file = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "secrets.json"
)
load_secrets(secrets_file)
os.environ["PROJECT_ROOT_PATH"] = os.path.abspath(os.path.dirname(__file__))

from status_page.run import app as application
