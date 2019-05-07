import json
import sys
import csv
import os

root = {}
root["Person"] = []

def input_from_file():
	input_file = sys.argv[1]
	csv.register_dialect('myDialect', delimiter = ',',quoting=csv.QUOTE_ALL,skipinitialspace=True)
	declared_headers = []
	csv_rows = []
	with open(input_file,'r') as csvFile:
		reader = csv.DictReader(csvFile)  
		root["Person"] = [row for row in reader]
		for i in root["Person"]:
			i.pop("nationality", None)
		print(json.dumps(root, indent=4))

def user_input():
	print("Proceeding User input ..")
	while True:
		# User data from input 
		first_name = input("What's your first name?")
		last_name = input("What's your last name?")
		print("Nice to meet you " + first_name + last_name + "!")

		while True:
			try:
				age = int(input("Your age? "))
			except ValueError:
				print("Sorry we didnt understand")
				continue

			if age < 0:
				print("Sorry your response must not be negative ")
				continue
			else:
				#Value is good
				break
		print("So, you are already %d years old, " % (age) + first_name + "!")

		favourite_color = input("what is your favourite color ?")
		print(favourite_color+" is nice!")
		Nationality = input("what is your Nationality?")
		
		# User data to json dump
		data = {}
		data['first_name'] = first_name
		data['last_name'] = last_name
		data['age'] = age
		data['favourite_color'] = favourite_color
		root["Person"].append(data)

		Furtherdata = input(" Want to feed more data ? yes/no ")
		if Furtherdata == "yes":
			continue
		else:
			break
	print(json.dumps(root, sort_keys=True, indent=4))

def main():
	if len(sys.argv) == 2:
		try:
			fh = open(sys.argv[1],"r")
			input_from_file()
		except FileNotFoundError:
			print("Input file is not available!! please check")
	elif len(sys.argv) > 2:
		print("Unknown no.of arguments, please pass only one input file ")
		print("e.g., python3 "+sys.argv[0]+" <Input file>")
		exit()
	else:
		user_input()

if __name__ == "__main__":
	main()

