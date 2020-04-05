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
            print("unable to import " + commandName)

def main():
    # call the main method of the requested module
    try:
        if len(sys.argv) < 2:
            commands["help"].main([])
            return
        requestedCommand = sys.argv[1]
        commands[requestedCommand].main(sys.argv)
    except:
        commands["help"].main([])

main()
