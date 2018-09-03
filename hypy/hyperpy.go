package main

import (
	"fmt"
	"os"
)

func main(){
	command := os.Args[1]
	response := hyperpy(command)
	if response == true {
		os.Exit(0)
	} else {

	}
}

func hyperpy(command string) bool {
	if command == "" || command == "help" {
		hyperpy_help()
		return false
	}
	if command == "hello" {
		hello()
		return true
	}
	return false
}

func hyperpy_help(){
	help_msg := `Hello !!!!guys!!!!!

this is hyperpy help.
	usage:
		freeze : generate requrements.txt
		hello  : hello!!!
		libup  : update all your python library`

		fmt.Println(help_msg)
}

func hello(){
	fmt.Println("hello!!!")
}