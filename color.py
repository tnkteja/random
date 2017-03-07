#!/usr/bin/python

from colorama import init, Fore

def success(string):
	print string,Fore.GREEN,u'\u2713', Fore.RESET

def warning(string):
	print string,Fore.YELLOW,'⚠', Fore.RESET

def danger(string):
	print string,Fore.RED,"☠", Fore.RESET
