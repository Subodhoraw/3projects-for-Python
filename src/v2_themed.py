import random 
def themed_headline_generator(theme):
    themes = {
        "space": {
            "subjects": ["The astronaut", "A spaceship", "The alien", "The planet", "The star"],
            "verbs": ["explores", "lands on", "discovers", "orbits", "communicates with"],
            "objects": ["a new galaxy", "the moon", "an alien civilization", "a black hole", "the space station"]
        },
        "technology": {
            "subjects": ["The developer", "A robot", "The AI", "The startup", "The engineer"],
            "verbs": ["creates", "launches", "innovates", "programs", "tests"],
            "objects": ["a new app", "the future of tech", "a groundbreaking algorithm", "the next big thing", "a smart device"]
        },
        "nature": {
            "subjects": ["The hiker", "A biologist", "The forest", "The river", "The mountain"],
            "verbs": ["discovers", "protects", "explores", "nurtures", "climbs"],
            "objects": ["a rare species", "the ecosystem", "a hidden trail", "the wildlife", "the natural beauty"]
        },
        "history": {
            "subjects": ["The archaeologist", "A historian", "The ancient city", "The artifact", "The monument"],
            "verbs": ["uncovers", "studies", "restores", "documents", "explores"],
            "objects": ["a lost civilization", "the past", "an ancient secret", "historical records", "a forgotten era"]
        },
        "sports": {
            "subjects": ["The athlete", "A team", "The coach", "The referee", "The fan"],
            "verbs": ["wins", "trains for", "leads", "celebrates", "competes in"],
            "objects": ["the championship", "a new record", "the tournament", "the game", "the victory"]
        },
        "music": {
            "subjects": ["The musician", "A band", "The composer", "The singer", "The DJ"],
            "verbs": ["performs", "composes", "records", "mixes", "produces"],
            "objects": ["a new album", "the concert", "a hit single", "the soundtrack", "the music festival"]
        },
        "food": {
            "subjects": ["The chef", "A food critic", "The restaurant", "The farmer", "The baker"],
            "verbs": ["creates", "tastes", "prepares", "grows", "bakes"],
            "objects": ["a gourmet dish", "the menu", "fresh ingredients", "a delicious dessert", "the culinary experience"]
        },
        "travel": {
            "subjects": ["The traveler", "A tour guide", "The explorer", "The backpacker", "The photographer"],
            "verbs": ["visits", "discovers", "documents", "navigates", "captures"],
            "objects": ["a hidden gem", "the culture", "a scenic route", "the adventure", "the landscape"]
        },
        "health": {
            "subjects": ["The doctor", "A fitness trainer", "The nutritionist", "The patient", "The researcher"],
            "verbs": ["treats", "advises", "studies", "improves", "discovers"],
            "objects": ["a new treatment", "healthy habits", "the disease", "wellness tips", "medical breakthroughs"]
        },
        "art": {
            "subjects": ["The artist", "A sculptor", "The painter", "The gallery owner", "The critic"],
            "verbs": ["creates", "exhibits", "curates", "reviews", "inspires"],
            "objects": ["a masterpiece", "the exhibition", "a new style", "the art world", "the creative process"]
        },
        "fashion": {
            "subjects": ["The designer", "A model", "The stylist", "The brand", "The influencer"],
            "verbs": ["launches", "showcases", "creates", "trends in", "influences"],
            "objects": ["a new collection", "the runway", "fashion trends", "the industry", "a stylish look"]
        },
        "education": {
            "subjects": ["The teacher", "A student", "The principal", "The professor", "The school"],
            "verbs": ["teaches", "learns", "leads", "researches", "innovates"],
            "objects": ["a new curriculum", "the classroom", "educational tools", "the future of learning", "academic success"]
        },
        "environment": {
            "subjects": ["The activist", "A scientist", "The organization", "The community", "The government"],
            "verbs": ["protects", "studies", "advocates for", "restores", "promotes"],
            "objects": ["the ecosystem", "clean energy", "sustainability", "the wildlife", "environmental policies"]
        }}
    if theme not in themes:
        return"theme not found. available themes are: " + ", ".join(themes.keys())
    subject = random.choice(themes[theme]["subjects"]) # corrected variable name
    verb = random.choice(themes[theme]["verbs"])# corrected variable name
    objects = random.choice(themes[theme]["objects"])# corrected variable name
    headline = f"{subject} {verb}{objects}."
    return headline
# Example usage
theme = input("Enter the available themes")
if theme.isdigit():
    theme = list(themes.keys())[int(theme) % len(themes)]  # Convert number to theme
   # You can change the theme to any of the available ones
print(themed_headline_generator(theme))# we have updated the file name, we are to addd its versionn