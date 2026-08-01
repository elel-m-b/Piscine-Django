#!/bin/bash
###############################################################################
# Exercise 04: Virtualenv
#
# Creates a python3 virtualenv named "django_venv", installs the
# requirement.txt file inside it, and leaves the virtualenv activated
# once the script is done.
#
# NOTE: for the virtualenv to stay activated in your current shell once
# the script finishes, this script must be *sourced*, not executed:
#   source my_script.sh
#   . ./my_script.sh
###############################################################################

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${SCRIPT_DIR}/django_venv"
REQ_FILE="${SCRIPT_DIR}/requirement.txt"

# Create the virtualenv if it does not already exist
if [ ! -d "${VENV_DIR}" ]; then
    echo "Creating virtualenv '${VENV_DIR}' ..."
    python3 -m venv "${VENV_DIR}"
fi

# Activate the virtualenv
source "${VENV_DIR}/bin/activate"

# Install the requirements inside the virtualenv
echo "Installing requirements from ${REQ_FILE} ..."
pip install --upgrade pip
pip install -r "${REQ_FILE}"

echo "Virtualenv 'django_venv' is now active."
