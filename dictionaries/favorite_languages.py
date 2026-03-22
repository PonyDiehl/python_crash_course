# A dictionary of similar objects 

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phill': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
for name in favorite_languages.keys():
    print(name.title())

friends = ['phill', 'sarah']
for name in favorite_languages:
    print(f"\t{name.title()}, I see you love {language}!")