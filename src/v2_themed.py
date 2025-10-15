import random 
print("Welcome to Themed Headline Generator v2.0")
def themed_headline_generator(theme):
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
        },
        "health": {
            "subjects": ["The doctor", "A fitness trainer", "The nutritionist", "The patient", "The researcher"],
            "verbs": ["treats", "advises", "studies", "improves", "discovers"],
            "object": ["a new treatment", "healthy habits", "the disease", "wellness tips", "medical breakthroughs"]
        },
        "art": {
            "subjects": ["The artist", "A sculptor", "The painter", "The gallery owner", "The critic"],
            "verbs": ["creates", "exhibits", "curates", "reviews", "inspires"],
            "object": ["a masterpiece", "the exhibition", "a new style", "the art world", "the creative process"]
        },
        "fashion": {
            "subjects": ["The designer", "A model", "The stylist", "The brand", "The influencer"],
            "verbs": ["launches", "showcases", "creates", "trends in", "influences"],
            "object": ["a new collection", "the runway", "fashion trends", "the industry", "a stylish look"]
        },
        "education": {
            "subjects": ["The teacher", "A student", "The principal", "The professor", "The school"],
            "verbs": ["teaches", "learns", "leads", "researches", "innovates"],
            "object": ["a new curriculum", "the classroom", "educational tools", "the future of learning", "academic success"]
        },
        "environment": {
            "subjects": ["The activist", "A scientist", "The organization", "The community", "The government"],
            "verbs": ["protects", "studies", "advocates for", "restores", "promotes"],
            "object": ["the ecosystem", "clean energy", "sustainability", "the wildlife", "environmental policies"]
        }}
    theme_list = list(themes.keys())
    selected_theme = None
    while True:
        theme_input = input(f"Choose a theme ({', '.join(theme_list)} or number 0-{len(theme_list)-1}): ").strip().lower()
        if theme_input in themes:
            selected_theme = theme_input
            print(f"Generating headline for theme: {selected_theme}")
            break
        elif theme_input.isdigit() and 0 <= int(theme_input) < len(theme_list):
            selected_theme = theme_list[int(theme_input)]
            print(f"Generating headline for theme: {selected_theme}")
            break
        print("Invalid theme. Please try again.")
    subject = random.choice(themes[selected_theme]["subjects"])
    verb = random.choice(themes[selected_theme]["verbs"])
    obj = random.choice(themes[selected_theme]["object"])
    headline = f"{subject} {verb} {obj}."
    return headline

# Example usage
# Convert number to theme
# You can change the theme to any of the available ones
# We have updated the file name, and we are to add its version.