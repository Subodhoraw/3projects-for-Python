import random 

print("Welcome to Themed Headline Generator v2.0")

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
        }
        # ... (other themes omitted for brevity)
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

    subject = random.choice(themes[selected_theme]["subjects"])
    verb = random.choice(themes[selected_theme]["verbs"])
    obj = random.choice(themes[selected_theme]["objects"])
    headline = f"{subject} {verb} {obj}."
    return headline


# Example usage
print("\n📰 " + themed_headline_generator())
