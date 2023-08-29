def count_vowels(string):
  """Counts the number of vowels in a given string.
  Args:
    string: The string to count the vowels in.
  Returns:
    The number of vowels in the string.
  """
  # Initialize a variable to store the number of vowels.
  num_vowels = 0
  # Convert the string to lowercase to simplify the comparison.
  string = string.lower()
  # Iterate over the characters in the string.
  for char in string:
    # Check if the character is a vowel.
    if char in 'aeiou':
      # Increment the number of vowels.
      num_vowels += 1
  # Return the number of vowels.
  return num_vowels
# Get the input string from the user.
input_string = input("Hello, how are you?: ")
# Count the number of vowels in the string.
num_vowels = count_vowels(input_string)
# Print the number of vowels.
print(f"Number of vowels: {num_vowels}")