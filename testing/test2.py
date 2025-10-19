import  random
print("Welcome to Themed Headline Generator v2.0")
def themed_headline_generator():
    themes = {
        "space": {
            "subjects": ["The astronaut", "A spaceship", "The alien", "The planet", "The star"],
            "verbs": ["explores", "lands on", "discovers", "orbits", "communicates with"],
            "object": ["a new galaxy", "the moon", "an alien civilization", "a black hole", "the space station"]
        },
        "technology": {
            "subjects": ["The developer", "A robot", "The AI", "The startup", "The engineer"],
            "verbs": ["creates", "launches", "innovates", "programs", "tests"],
            "object": ["a new app", "the future of tech", "a groundbreaking algorithm", "the next big thing", "a smart device"]
        },
        "nature": {
            "subjects": ["The hiker", "A biologist", "The forest", "The river", "The mountain"],
            "verbs": ["discovers", "protects", "explores", "nurtures", "climbs"],
            "object": ["a rare species", "the ecosystem", "a hidden trail", "the wildlife", "the natural beauty"]
        },
        "history": {
            "subjects": ["The archaeologist", "A historian", "The ancient city", "The artifact", "The monument"],
            "verbs": ["uncovers", "studies", "restores", "documents", "explores"],
            "object": ["a lost civilization", "the past", "an ancient secret", "historical records", "a forgotten era"]
        },
        "sports": {
            "subjects": ["The athlete", "A team", "The coach", "The referee", "The fan"],
            "verbs": ["wins", "trains for", "leads", "celebrates", "competes in"],
            "object": ["the championship", "a new record", "the tournament", "the game", "the victory"]
        },
        "music": {
            "subjects": ["The musician", "A band", "The composer", "The singer", "The DJ"],
            "verbs": ["performs", "composes", "records", "mixes", "produces"],
            "object": ["a new album", "the concert", "a hit single", "the soundtrack", "the music festival"]
        },
        "food": {
            "subjects": ["The chef", "A food critic", "The restaurant", "The farmer", "The baker"],
            "verbs": ["creates", "tastes", "prepares", "grows", "bakes"],
            "object": ["a gourmet dish", "the menu", "fresh ingredients", "a delicious dessert", "the culinary experience"]
        },
        "travel": {
            "subjects": ["The traveler", "A tour guide", "The explorer", "The backpacker", "The photographer"],
            "verbs": ["visits", "discovers", "documents", "navigates", "captures"],
            "object": ["a hidden gem", "the culture", "a scenic route", "the adventure", "the landscape"]
        }}

    theme_list = list(themes.keys())
    print("\nAvailable Themes:")
    for i, theme in enumerate(theme_list): #enumerate to get index and theme
        print(f"{i} -{theme}")
        