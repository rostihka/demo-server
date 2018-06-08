#!/bin/bash

PROGNAME=$(basename $0)

error_exit()
{
  echo "${PROGNAME}: ${1:-"Unknown Error"}" 1>&2
  exit 1
}

echo "Check current directory"

if [ "$(basename $PWD)" != "demo-server" ]
then
  error_exit "Line $LINENO: Incorrect project root directory. Run the script from qrs-server/ directory."
fi

echo "Install prerequisites"

sudo apt-get update && sudo apt-get install -y  \
  g++ \
  git \
  libmemcached-dev \
  libxml2-dev \
  libxslt1-dev \
  libz-dev \
  python-dev \
  python-m2crypto \
  python-pip \
  vim \
  tdsodbc \
  unixodbc-dev \
  xmlsec1

sudo pip install virtualenv

echo "Configure git"

gitusername=$(git config --get user.name)
if [ -z "$gitusername" ]
then
  read -p "Enter your name (example, John Doe): " gitusername
  git config --global user.name "$gitusername"
else
  echo "Your user name is $gitusername"
fi

gituseremail=$(git config --get user.email)
if [ -z "$gituseremail" ]
then
  read -p "Enter your email: " gituseremail
  git config --global user.email $gituseremail
else
  echo "Your email is $gituseremail"
fi

echo "Configure odbc"

if [ $(grep -i "\[freetds\]" /etc/odbcinst.ini | wc -l) -eq 0 ]
then
  sudo sh -c 'echo "[FreeTDS]
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so
" >> /etc/odbcinst.ini'
fi

echo "Create a virtual environment"

virtualenv ../py_ve/qrs || error_exit "Line $LINENO: Can't create a virtual environment."

echo "Setup the project"

source ../py_ve/qrs/bin/activate || error_exit "Line $LINENO: Can't activate python virtual environment."

pip install -r requirements.txt || error_exit "Line $LINENO: Can't install requirements."