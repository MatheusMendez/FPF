#/bin/bash

mkdir matheus
cd matheus
mkdir resultado
wget http://vanilton.net/v1/download/zip.zip
unzip ./zip.zip
mv readme.md ./resultado

rm -f zip.zip