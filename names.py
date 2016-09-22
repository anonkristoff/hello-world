# 5e DnD name Generator
# Using the chart on the Dungeon Master's Screen,
# generate a random name.

import random

def get_number():
	return random.randint(1,20)

def generate_name():
	name = ""
	beginning = ["", "", "", "", "A", "Be", "De", "El", "Fa", "Jo", "Ki", "La", "Ma", "Na", "O", "Pa", "Re", "Si", "Ta", "Va"]
	middle = ["bar", "ched", "dell", "far", "gran", "hal", "jen", "kel", "lim", "mor", "net", "penn", "quil", "rond", "sark", "shen", "tur", "vash", "yor", "zen"]
	end = ["", "a", "ac", "ai", "al", "am", "an", "ar", "ea", "el", "er", "ess", "ett", "ic", "id", "il", "in", "is", "or", "us"]
	name = beginning[get_number()-1] + middle[get_number()-1] + end[get_number()-1]
	return name

print(generate_name())