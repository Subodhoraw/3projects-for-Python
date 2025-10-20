import random
print("Welcome to Themed Headline Generator v3.0 with AI Additions")
def themed_headline_generator():
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
        "fantasy": {
            "subjects": ["The wizard", "A dragon", "The knight", "The elf", "The sorcerer"],
            "verbs": ["casts a spell on", "battles with", "discovers", "protects", "enchants"],
            "objects": ["a magical realm", "the ancient artifact", "the dark forest", "the hidden treasure", "the mystical creature"]
        },
        "history": {
            "subjects": ["The emperor", "A soldier", "The explorer", "The philosopher", "The queen"],
            "verbs": ["conquers", "discovers", "debates about", "rules over", "builds"],
            "objects": ["a vast empire", "new lands", "ancient wisdom", "a powerful kingdom", "historic monuments"]
        }
    }

    theme_list = list(themes.keys())

    print("\nAvailable Themes:")
    for i, theme in enumerate(theme_list):
        print(f"  {i} - {theme}")

    while True:
        theme_input = input("\nChoose a theme by name or number: ").strip().lower()
        if theme_input in themes:
            selected_theme = theme_input
            print(f"\nGenerating headline for theme: {selected_theme}")
            break
        elif theme_input.isdigit() and 0 <= int(theme_input) < len(theme_list):
            selected_theme = theme_list[int(theme_input)]
            print(f"\nGenerating headline for theme: {selected_theme}")
            break
        print("Invalid theme. Please try again.")