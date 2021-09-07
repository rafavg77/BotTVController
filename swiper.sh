#!/bin/bash

function swipeUp(){
    adb shell input swipe 300 300 500 1000
}

function swipeDown(){
    adb shell input swipe 500 1000 300 300
}

function main(){
    if [[ $1 == 'u' ]]
    then
        swipeUp
    elif [[ $1 == 'd' ]]
    then
        swipeDown
    fi
}

main $1