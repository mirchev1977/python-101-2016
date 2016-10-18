# A function for counting the digits of a number
def sum_of_digits(number):
	if number < 0:
		number *= -1
	sum_of_numbers = 0
	number = str(number)
	for n in number:
		sum_of_numbers += int(n)
	print(sum_of_numbers)

# sum_of_digits(1325132435356)
# sum_of_digits(123)
# sum_of_digits(6)
# sum_of_digits(-10)


# Create list with the digits of a number
def to_digits(number):
	number = str(number)
	list_of_chars = []
	for char in number:
		list_of_chars.append(char)
	print(list_of_chars)
# to_digits(123)
# to_digits(99999)
# to_digits(123023)

# Create number from array
def to_number(digits):
    string = ''
    for digit in digits:
    	digit = str(digit)
    	string += digit
    print(string)
# to_number([1,2,3])

# Count the vowels in a string
def count_vowels(string):
	output_string = ''
	for char in string:
		if (char.lower() != 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u' or char.lower() == 'y'):
			output_string = output_string + char
	return len(output_string)
    		

# print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))


# Count the consonants in a string
def count_consonants(string):
	count = 0
	for char in string:
   		if char.lower() != 'a' and char.lower() != 'e' and char.lower() != 'i' and char.lower() != 'o' and char.lower() != 'u' and char.lower() != 'y' :
   			count += 1
	return count
# print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
# print(count_consonants("Python"))
# print(count_consonants('Theistareykjarbunga'))

# Check if a given number is prime
def prime_number(number):
	is_prime = True
	for x in range(2,number):
		if number % 2 == 0:
			is_prime = False
	return is_prime
# print(prime_number(7))

# Sum of the factorials of the digits in the number
def fact_digits(n):
	output = 0
	for x in range(1, n + 1):
		product = 1
		for y in range(1, x + 1):
			product *= y
		output = product
	return output
# print(fact_digits(6))

# fibonacci sequince
def fibonacci(number):
	a = 0
	b = 1
	output = ''
	output += str(b)
	for x in range(number - 1):
		c = a + b
		output += str(c)
		a = b
		b = c
	return(output)
# print(fibonacci(3))

# Check if a given string is palindrome
def palindrome(string):
	is_palindrome = True
	length = len(string) // 2
	rear = len(string) - 1;
	output = '';
	for i in range(length):
		front = string[i]
		back = string[rear]
		if front != back:
			is_palindrome = False
			break
		rear -= 1
	return is_palindrome
# print(palindrome('kapak'))


# Dictionary with all characters from a string
def char_histogram(string):
	dictionary = {}
	
	# for letter in string:
	# 	current_letter = letter
	# 	counter = 0

	# 	for sub_letter in string:
	# 		if current_letter == sub_letter:
	# 			counter += 1

	# 	dictionary[current_letter] = counter

	for char in string:
		dictionary[char] = list(string).count(char)

	return dictionary
		

print(char_histogram("Pythontponhth"))