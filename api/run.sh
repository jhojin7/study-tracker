#!/bin/sh

pwd
wd=`pwd`

# build
$wd/gradlew build

# run db in background
#~/src/h2/bin/h2.sh &
java -jar $wd/build/libs/*-SNAPSHOT.jar
