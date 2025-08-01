# Find the shortest and longest words in a given list.
def shortest_longest_words(words_list):
    shortest_word = min(words_list, key=len)
    longest_word = max(words_list, key=len)
    return shortest_word, longest_word
 
words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
result = shortest_longest_words(words)
 
print(result)
 
# output:
# ('kiwi', 'grapefruit')


#Write a Python function that takes a list and an element as input. The function should add the element to the list only if it's not already present in the list.

def add_unique_element(input_list, element):
    if element not in input_list:
        input_list.append(element)
 
my_list = ["apple", "banana", "kiwi"]
add_unique_element(my_list, "banana")
add_unique_element(my_list, "orange")
 
print(my_list)
 
# output:
# ['apple', 'banana', 'kiwi', 'orange']

# Remove duplicates from a list and sort it
def remove_duplicates_and_sort(input_list):
    unique_sorted_list = sorted(set(input_list))
    return unique_sorted_list
 
input_list = ["apple", "banana", "kiwi", "banana", "orange", "apple"]
result = remove_duplicates_and_sort(input_list)
 
print(result)
 
# output:
# ['apple', 'banana', 'kiwi', 'orange']

#Write a Python function that takes a list of numbers as input and returns a sorted list containing only the non-negative numbers from the input list.
def sort_non_negative_numbers(input_list):
    non_negative_numbers = []
    for num in input_list:
        if num >= 0:
            non_negative_numbers.append(num)
    sorted_non_negative_numbers = sorted(non_negative_numbers)
    return sorted_non_negative_numbers
 
numbers = [5, -3, 0, 9, -2, 7, -1, 4]
result = sort_non_negative_numbers(numbers)
 
print(result)
 
# output:
# [0, 4, 5, 7, 9]