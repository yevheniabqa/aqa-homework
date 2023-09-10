def camel_to_snake(variable_name):
    snake_case = ""
    for char in variable_name:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    if snake_case.startswith("_"):
        snake_case = snake_case[1:]
    return snake_case

camel_case_variables = ["FirstItem", "FriendsList", "MyTuple"]

snake_case_variables = [camel_to_snake(var) for var in camel_case_variables]

print(snake_case_variables)
