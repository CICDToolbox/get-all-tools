#!/usr/bin/env python

"""
Tool Download Script.

This script automates the process of downloading various CI/CD tool scripts from a specified GitHub repository,
saves them to a designated directory, and sets the appropriate permissions for execution.

The script performs the following actions:
1. Defines a list of tools to be downloaded.
2. Creates a target directory for saving the tool scripts if it does not already exist.
3. Iterates over the list of tools, downloading each tool's script from its respective GitHub repository.
4. Saves the downloaded scripts to the target directory with a prefix to identify them.
5. Sets the downloaded scripts to be executable.

Features:
- Timeout Handling: Ensures that the script does not hang indefinitely by setting a timeout for HTTP requests.
- HTTP Error Handling: Catches and reports HTTP errors, such as 404 Not Found or 500 Internal Server Error.
- General Exception Handling: Catches and reports other exceptions that may occur during the download or file operations.
- Directory Creation: Creates the target directory if it does not exist, ensuring a smooth setup process.

Dependencies:
- requests: A simple, yet elegant HTTP library for Python.

Usage:
1. Ensure you have Python 3 and the requests library installed.
2. Save this script to a file, for example, download_tools.py.
3. Make the script executable: chmod +x download_tools.py
4. Run the script: ./download_tools.py

Example:
    $ ./download_tools.py
    Successfully downloaded and set permissions for action-lint
    Successfully downloaded and set permissions for awesomebot
    ...

Notes:
- The script assumes a specific directory structure in the GitHub repositories.
- The scripts are downloaded from the 'master' branch of each repository.
"""

import os
import sys
import requests

from requests.exceptions import HTTPError, Timeout

# Define constants
FILE_PATH: str = os.path.join(os.environ['HOME'], 'bin')

TOOLS: list[str] = [
    "action-lint", "awesomebot", "bandit", "hadolint", "json-lint", "markdown-lint",
    "perl-lint", "php-lint", "puppet-lint", "pur", "pycodestyle", "pydocstyle",
    "pylama", "pylint", "reek", "rubocop", "shellcheck", "validate-citations-file", "yaml-lint"
]

BASE_URL = "https://raw.githubusercontent.com/CICDToolbox"
TIMEOUT = 10  # seconds


def download_tool(tool_name: str) -> None:
    """
    Download the tool's pipeline script from the given URL and save it to the specified file path.

    Args:
        tool_name (str): The name of the tool to download.

    Raises:
        HTTPError: If an HTTP error occurs during the request.
        Timeout: If the request times out.
        Exception: For any other exceptions that occur during the request or file operations.
    """
    url: str = f"{BASE_URL}/{tool_name}/master/pipeline.sh"
    destination: str = os.path.join(FILE_PATH, f"cicd-{tool_name}")

    try:
        response: requests.Response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
        with open(destination, 'wb') as file:
            file.write(response.content)
        os.chmod(destination, 0o700)
        print(f"Successfully downloaded and set permissions for {tool_name}")

    except HTTPError as http_err:
        print(f"HTTP error occurred while downloading {tool_name}: {http_err}")
    except Timeout as timeout_err:
        print(f"Timeout error occurred while downloading {tool_name}: {timeout_err}")
    except Exception as err:
        print(f"An error occurred while downloading {tool_name}: {err}")


def main() -> None:
    """Control the main flow of the program to create the tools directory and download the specified tools."""
    try:
        os.makedirs(FILE_PATH, exist_ok=True)
        for tool in TOOLS:
            download_tool(tool)
    except Exception as e:
        print(f"An error occurred while setting up tools directory or downloading tools: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
