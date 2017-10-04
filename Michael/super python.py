true = 0 == 0
# http://learnpython.org/en/Hello%2C_World%21
print("Hello, World!")
# http://learnpython.org/en/Variables_and_Types
# change this code
if (true):
	mystring = "hello"
	myfloat = 10.0
	myint = 20

	# testing code
	if mystring == "hello":
		print("String: %s" % mystring)
	if isinstance(myfloat, float) and myfloat == 10.0:
		print("Float: %f" % myfloat)
	if isinstance(myint, int) and myint == 20:
		print("Integer: %d" % myint)
	# http://learnpython.org/en/Lists
	numbers = []
	numbers.append(1)
	numbers.append(2)
	numbers.append(3)
	strings = ["hello", "world"]
	names = ["John", "Eric", "Jessica"]

	# write your code here
	second_name = names[1]


	# this code should write out the filled arrays and the second name in the names list (Eric).
	print(numbers)
	print(strings)
	print("The second name on the names list is %s" % second_name)
# http://learnpython.org/en/Basic_Operators
if (true):
	# unsolvable
	x = object()
	y = object()

	# TODO: change this code
	x_list = [x] * 10
	y_list = [y] * 10
	big_list = x_list + y_list

	print("x_list contains %d objects" % len(x_list))
	print("y_list contains %d objects" % len(y_list))
	print("big_list contains %d objects" % len(big_list))

	# testing code
	if x_list.count(x) == 10 and y_list.count(y) == 10:
		print("Almost there...")
	if big_list.count(x) == 10 and big_list.count(y) == 10:
		print("Great!")
# http://learnpython.org/en/String_Formatting
if (true):
	data = ("John", "Doe", 53.44)
	format_string = "Hello %s %s. Your current balance is $%s."

	print(format_string % data)
# http://learnpython.org/en/Basic_String_Operations
if (true):
	s = "Strings are awesome!"
	# Length should be 20
	print("Length of s = %d" % len(s))

	# First occurrence of "a" should be at index 8
	print("The first occurrence of the letter a = %d" % s.index("a"))

	# Number of a's should be 2
	print("a occurs %d times" % s.count("a"))

	# Slicing the string into bits
	print("The first five characters are '%s'" % s[:5]) # Start to 5
	print("The next five characters are '%s'" % s[5:10]) # 5 to 10
	print("The thirteenth character is '%s'" % s[12]) # Just number 12
	print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
	print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

	# Convert everything to uppercase
	print("String in uppercase: %s" % s.upper())

	# Convert everything to lowercase
	print("String in lowercase: %s" % s.lower())

	# Check how a string starts
	if s.startswith("Str"):
		print("String starts with 'Str'. Good!")

	# Check how a string ends
	if s.endswith("ome!"):
		print("String ends with 'ome!'. Good!")

	# Split the string into three separate strings,
	# each containing only a word
	print("Split the words of the string: %s" % s.split(" "))
# http://learnpython.org/en/Conditions
# change this code
if (true):
	number = 16
	second_number = 0
	first_array = [1,4,5]
	second_array = [1,2]

	if number > 15:
		print("1")

	if first_array:
		print("2")

	if len(second_array) == 2:
		print("3")

	if len(first_array) + len(second_array) == 5:
		print("4")

	if first_array and first_array[0] == 1:
		print("5")

	if not second_number:
		print("6")
# http://learnpython.org/en/Loops
if (true):
	numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
	]

	for number in numbers:
		if (number == 237):
			break
		if (number % 2 == 0):
			print(number)
# http://learnpython.org/en/Functions
if (true):
	# Modify this function to return a list of strings as defined above
	def list_benefits():
		return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

	# Modify this function to concatenate to each benefit - " is a benefit of functions!"
	def build_sentence(benefit):
		return benefit + " is a benefit of functions!"

	def name_the_benefits_of_functions():
		list_of_benefits = list_benefits()
		for benefit in list_of_benefits:
			print(build_sentence(benefit))

	name_the_benefits_of_functions()
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# http://learnpython.org/en/Classes_and_Objects
if (true):
	# your code goes here
	car1 = Vehicle()
	car2 = Vehicle()
	car1.name = "Fer"
	car1.kind = "convertible"
	car1.color = "red"
	car1.value = 60000.0
	car1.name = "Jump"
	car2.kind = "van"
	car2.color = "blue"
	car2.value = 10000.0

	# test code
	print(car1.description())
	print(car2.description())
# http://learnpython.org/en/Dictionaries
if (true):
	phonebook = {
		"John" : 938477566,
		"Jack" : 938377264,
		"Jake" : 938273443
	}

	# write your code here


	# testing code
	if "Jake" in phonebook:
		print("Jake is listed in the phonebook.")
	if "Jill" not in phonebook:
		print("Jill is not listed in the phonebook.")
# http://learnpython.org/en/Modules_and_Packages
import re
if (true):
	# Your code goes here
	find_members = []
	for member in dir(re):
		if "find" in member:
			find_members.append(member)

	print(sorted(find_members))
# http://learnpython.org/en/Numpy_Arrays
if (true):
	weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

	import numpy as np
	wk = np.array(weight_kg)
	print(wk ** 2.2)

	# Create a numpy array np_weight_kg from weight_kg
		

	# Create np_weight_lbs from np_weight_kg

	# Print out np_weight_lbs
# http://learnpython.org/en/Pandas_Basics has no challenges.