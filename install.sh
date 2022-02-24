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
    directory="/usr/local"
    ;;
  *)
    catchError "Unsupported operating system"
    ;;
  esac
executable=$directory"/bin/"$(echo $shell | tr 'A-Z' 'a-z')
resource=$directory"/share/py"

echo "  -Assessing files..."

if [ ! -e "./cli.py" ] || [ ! -d "./py/" ]
then
  catchError "Missing important files/directories"
fi

chmod +x "./cli.py"

echo "  -Entering superuser..."
writeYellow "This is required to write to root-level"

if [ -e $executable ] || [ -d $resource ]
then
  writeRed "Installation already exists, would you like to overwrite it?"
  read -p "(Y/N) " confirm
  confirm=$(echo $confirm | tr 'a-z' 'A-Z')
  if [[ ! $confirm =~ ^Y ]]
  then
    exit
  fi
elif [ ! -d $directory ] || [ ! -d $directory"/bin" ] || [ ! -d $directory"/share" ]
then
  sudo mkdir $directory && sudo mkdir $directory"/bin" && sudo mkdir $directory"/share"
fi

sudo cp cli.py $executable
sudo cp -a py/. $resource

writeGreen "Successfully installed ${shell}"
