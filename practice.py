# GCI2018_Practice_1

x = 1
while x <= 10:
	print("GCI is great")
	x += 1

name = input("What's your name? ")
if len(name) > 0 and name.isalpha():
	reverse = name[::-1]
	print("Hello " + str(name) + ", please to meet you! Did you know you name backwards is " + str(reverse) + "?")
