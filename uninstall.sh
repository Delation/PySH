echo "Preparing uninstall..."

echo "  -Writing utility functions and variables..."
function writeNeutral {
  echo "\033[0m"
}
function writeGreen {
  printf "\033[0;32m${1}"
  writeNeutral
}
function writeRed {
  printf "\033[0;31m${1}"
  writeNeutral
}
function writeYellow {
  printf "\033[1;33m${1}"
  writeNeutral
}
function catchError {
  writeRed "Exception encountered: ${1}"
  exit 1
}
shell="PySH"

echo "  -Interpreting script for operating system..."
case $OSTYPE in

  "darwin"*)
    executableDir="/usr/local/bin"
    resourceDir="/usr/local/share"
    ;;
  *)
    catchError "Unsupported operating system"
    ;;
  esac
executable=$executableDir"/"$(echo $shell | tr 'A-Z' 'a-z')
resource=$resourceDir"/pysh"

echo "  -Entering superuser..."
writeYellow "This is required to write to root-level"
# This just prompts entering your password for sudo
sudo test

echo "  -Checking install location..."

if [ ! -e $executable ] && [ ! -d $resource ]
then
  writeRed "Installation does not exist"
  exit 1
fi

echo "  -Deleting resources..."

sudo rm -rf $resource
sudo rm $executable

writeGreen "Successfully uninstalled ${shell}"
