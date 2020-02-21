#!/usr/bin/env python3
import os
import sys
import importlib

commands = {}

for file in os.listdir("addons"):
    if file.endswith(".py"):
        commandName = file.replace('.py', '')
        moduleName = "addons." + file.replace('.py', '')
        try:
            module = importlib.import_module(moduleName)
            commands[commandName] = module
        except:
            print("unable to import")

requestedCommand = sys.argv[1]
# call the main method of the requested module
commands[requestedCommand].main(sys.argv)
