import sys
import json
import datetime
from json import JSONEncoder
from storage import Storage


arguments = sys.argv[2:]

def order_arguments_and_parameters(arguments):
	parameters = dict()
	parameter = None
	for argument in arguments:
		if argument[0:2] == "--":
			parameter = argument
			parameters[parameter] = list()
		elif parameter:
			parameters[parameter].append(argument)
		else:
			print("Incorrect parameters")
	return parameters


def parse_parameters():
	global parsed_parameters
	parsed_parameters = dict()
	for item, value in parameters.items():
		parsed_value = ' '.join(value)
		parsed_parameters[item] = parsed_value
	return parsed_parameters


def convert_deadline_format(parsed_parameters):
	date_str = parsed_parameters.get("--deadline")
	if date_str:
		try:
			date_dt = datetime.strptime(date_str, '%b %d %Y %H:%M')
			parsed_parameters["--deadline"] = date_dt
		except:
			print("Incorrect date time format. Please provide date in MMM DD YYYY HH:mm format ex: Jun 1 2005 15:45")
	return parsed_parameters


if arguments:
	note_db = Storage()
	name = sys.argv[1]
	arguments = sys.argv[2:]
	hashed_parameters = hash(str(arguments))

	parameters = order_arguments_and_parameters(arguments)

	parsed_parameters = parse_parameters()


	parsed_parameters["hash"] = hashed_parameters

	if name == "add":
		note_db.add(parsed_parameters)
	elif name == "update":
		note_db.add(parsed_parameters, hashed_parameters)
	elif name == "remove":
		note_db.remove(hashed_parameters)
	elif name == "all":
		note_db.all(hashed_parameters)
	else:
		print("Please select one of the options: add, update, remove, all")
