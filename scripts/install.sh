echo "Preparing install..."

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

echo "  -Assessing files..." && cd ..

if [ ! -e "./cli.py" ] || [ ! -d "./py/" ]
then
  catchError "Missing important files/directories"
fi

chmod +x "./cli.py"

echo "  -Entering superuser..."
writeYellow "This is required to write to root-level"
# This just prompts entering your password for sudo
sudo test

echo "  -Checking install location..."

if [ -e $executable ] || [ -d $resource ]
then
  writeRed "Installation already exists, would you like to overwrite it?"
  read -p "(Y/N) " confirm
  confirm=$(echo $confirm | tr 'a-z' 'A-Z')
  if [[ ! $confirm =~ ^Y ]]
  then
    exit
  fi
elif [ ! -d $executableDir ] || [ ! -d $resourceDir ]
then
  writeRed "  -Creating proper directories (this installation may fail)..."
  sudo mkdir $executableDir && sudo mkdir $resource
fi

echo "  -Copying resources..."

sudo cp "cli.py" $executable
sudo cp -a "py/." $resource

writeGreen "Successfully installed ${shell}"
