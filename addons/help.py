#!/usr/bin/env python3
import os
import sys
import importlib

commands = {}

def main(args):
    # this is done in main because otherwise it would recursively
    # import itself forever
    for file in os.listdir("addons"):
        if file.endswith(".py"):
            commandName = file.replace('.py', '')
            moduleName = "addons." + file.replace('.py', '')
            try:
                module = importlib.import_module(moduleName)
                commands[commandName] = module
            except:
                print("unable to import")

    if len(args) == 3:
        commands[sys.argv[2]].help()
    else:
        help_prompt()

def short_desc():
    print("  help - view the help prompts for all subcommands")

def help():
    print(sys.argv[0] + " help - view the help prompts for subcommands\n")
    print("If you're looking for more information on how to use a")
    print("subcommand (such as 'exif', for example), you can run:")
    print(sys.argv[0] + " help exif")
    print("which will output the help prompt specific to the exif")
    print("subcommand.")

def help_prompt():
    print("Command usage: " + sys.argv[0] + " <subcommand>")
    print("Valid subcommands:")
    for name in commands:
        # print help usage
        commands[name].short_desc()
    print("Use the 'help' subcommand to get help for any of the other subcommands")
    print("by running: " + sys.argv[0] + " help <subcommand>")
    print("For example: " + sys.argv[0] + " help exif")
    print("will show the help prompt for the exif subcommand")

