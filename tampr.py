#!/usr/bin/env python3
import os
import sys
import importlib

commands = {}

# import all addons and keep references to the modules
for file in os.listdir("addons"):
    if file.endswith(".py"):
        commandName = file.replace('.py', '')
        moduleName = "addons." + file.replace('.py', '')
        try:
            module = importlib.import_module(moduleName)
            commands[commandName] = module
        except:
            print("unable to import")

# call the main method of the requested module
requestedCommand = sys.argv[1]
commands[requestedCommand].main(sys.argv)
