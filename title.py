def convert_to_title_case(input_string):
    title_case_string=""
    capitalize_next=True

    for char in input_string:
        if capitalize_next and char.isalpha():
            title_case_string+=char.upper()
            capitalize_next=False
        else:
            title_case_string+=char.lower()
            if char.isspace():
                capitalize_next=True
    return title_case_string

user_input=input("Enter a string of more than one word")
title_case_result= convert_to_title_case(user_input)
print("Original string",user_input)
print("Title case string",title_case_result)
