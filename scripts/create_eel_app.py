#!/usr/bin/env python3
import os
from subprocess import check_output
from sys import argv
from json import loads

from app_templates import basic_template

def usage():
	usage_msg = """
USAGE:
create_eel_app COMMAND [OPTIONS]

COMMANDS
create -> creates a new app
launch -> launches an app
publish -> packages the app using pyinstaller
usage -> show this message

EXAMPLE USE:
create_eel_app.py create hello_world
cd hello_world
create_eel_app.py launch 
create_eel_app.py publish
"""
	print(usage_msg)

def create_file(filename: str, file_content: str = "", is_dir: bool = False):
	print("Creating {}...".format(filename), end="")
	if not is_dir:
		with open(filename, "w") as file:
			file.write(file_content)
	else:
		os.makedirs(filename, exist_ok=True)
	print("done")

def create_template_files(app_name: str, files: dict) -> bool:
	for file_name, file_content in files.items():
		print("Creating {}...".format(file_name), end="")
		
		if os.path.dirname(file_name) != '':
			os.makedirs(os.path.dirname(file_name), exist_ok=True)

		if file_content:
			with open(file_name, "w") as f:
				f.write(file_content)
		print("done")
	return True

def create_app_files(app_name: str) -> bool:
	create_file(app_name, is_dir=True)
	os.chdir(app_name)
	create_file(app_name, is_dir=True)
	create_file("README.md", file_content="# {}".format(app_name))
	return True

def git_init():
	if not "version" in str(check_output(["git", "--version"])):
		print("No git installed, skipping repository initialization")
		return
	os.system("git init")
	print("Initialized git repo")

def create_app(app_name: str, template_files: dict):
	if create_app_files(app_name) and create_template_files(app_name, template_files):
		print("Created {}".format(app_name))
		git_init()
	else:
		print("Could not create {}".format(app_name))

def load_config(filename: str = "app_config.json") -> dict:
	# look for the file
	if not os.path.isfile(filename):
		# if it is not found, print an error and return an empty dict
		print("Could not locate {}".format(filename))
		return {}
	# load it into config
	config = {}
	with open(filename, "r") as f:
		config = loads(f.read())
	return config

def launch_app():
	config = load_config()
	if config == {}:
		return
	try:
		app_name = config["entry"]
	except:
		# if the file does not have the attrib we're looking for
		# print an error and return
		print("Could not locate the 'entry' attribute in app_config.json")
		return
	# launch the app
	# TODO: Make sure the python binary is located at 'python' and not at some
	# other location (python3, python2, etc)
	print("Launching {}".format(app_name))
	os.system("python {}".format(app_name))

def publish_app():
	config = load_config()
	if config == {}:
		return
	try:
		build_dir = config["build_dir"]
		excluded_modules = config["excluded_modules"]
		entry = config["entry"]
		web_folder = config["web_folder"] + "/"
	except:
		print("Couldn't find build attributes in app_config.json")
		return
	cmd = "pyinstaller -m eel {} {}".format(entry, web_folder)
	if len(excluded_modules) > 0:
		for em in excluded_modules:
			cmd += " --exclude {}".format(em)
	cmd += " --distpath {} --onefile --noconsole".format(build_dir)
	print("Bundling the app with pyinstaller")
	os.system(cmd)

if len(argv) == 3 and argv[1] == "create":
	try:
		parent_dir = os.getcwd()
		app_name = argv[2]
		create_app(app_name, basic_template.Files)
		os.chdir(parent_dir)
	except IndexError:
		print("No app name was given. See 'create_eel_app.py usage'")
		quit()
elif len(argv) == 2:
	# TODO: implement these functions
	if argv[1] == "launch":
		launch_app()
	elif argv[1] == "publish":
		publish_app()
else:
	usage()
	quit()
