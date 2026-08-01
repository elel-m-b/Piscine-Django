#!/bin/bash
###############################################################################
# Exercise 01: Pip
#
# Installs the development version of the "path" library (formerly path.py)
# from its GitHub repository into a local folder named "local_lib", then
# runs my_program.py which uses that library.
###############################################################################

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LIB_DIR="${SCRIPT_DIR}/local_lib"
LOG_FILE="${SCRIPT_DIR}/pip_install.log"
PROGRAM="${SCRIPT_DIR}/my_program.py"

# Display which pip version is used
echo "Using pip version:"
python3 -m pip --version

# (Re)install the path library development version from GitHub into local_lib,
# overwriting any previous install found there.
echo "Installing 'path' (path.py) development version into ${LIB_DIR} ..."
rm -rf "${LIB_DIR}"
mkdir -p "${LIB_DIR}"

python3 -m pip install \
    --upgrade \
    --force-reinstall \
    --target "${LIB_DIR}" \
    "git+https://github.com/jaraco/path.git" > "${LOG_FILE}" 2>&1

INSTALL_STATUS=$?

if [ ${INSTALL_STATUS} -ne 0 ]; then
    echo "Installation failed, see ${LOG_FILE} for details."
    exit 1
fi

echo "Installation successful, logs written to ${LOG_FILE}"

# Run the python program, making the freshly installed library importable.
PYTHONPATH="${LIB_DIR}:${PYTHONPATH}" python3 "${PROGRAM}"
