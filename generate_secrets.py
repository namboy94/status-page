#!/usr/bin/env python
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
import sys
import json
import argparse


def generate_secrets(prompt: bool):
    """
    Generates a secrets.json file out of environment variables
    :return: None
    """
    secrets = {}

    for key in [
        "DB_KEY",
        "DB_NAME",
        "DB_USER",
        "SMTP_SERVER",
        "SMTP_ADDRESS",
        "SMTP_PORT",
        "SMTP_PASSWORD",
        "FLASK_SECRET",
        "SERVER_LIST_CONFIG"
    ]:
        if key not in os.environ and prompt:
            value = input("{} is missing, set manually: ".format(key))
        else:
            value = os.environ.get(key)

        if value is None:
            print("No Value for {}, exiting".format(key))
            sys.exit(1)
        else:
            secrets[key] = value

    with open("secrets.json", "w") as f:
        f.write(json.dumps(secrets))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt-if-missing", action="store_true",
                        help="Allows manually adding missing environment "
                             "variables using user prompt")
    args = parser.parse_args()
    generate_secrets(args.prompt_if_missing)
