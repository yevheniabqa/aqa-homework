program_langs = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "JavaScript": "Brendan Eich",
    "C++": "Bjarne Stroustrup"
}

for language, developer in program_langs.items():
    print(f"My favorite programming language is {language}. It was created by {developer}.")

del program_langs["C++"]

print("\nUpdated Dictionary:")
print(program_langs)





