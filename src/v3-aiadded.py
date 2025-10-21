import random
from datetime import datetime
print("Welcome to Themed Headline Generator v3.0 with AI Additions")

Themes = {
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

SENTIMENT_VERBS = {
    "POSITIVE":["celebrates", "embraces", "achieves", "excels in", "thrives in"],
    "NEGATIVE":["struggles with", "fails in", "collapses under", "declines in", "battles against"],
    "NEUTRAL":["observes", "analyzes", "reports on", "discusses", "examines"]}
TIME_CONTEXT_MODIFIERS = {
    "PAST":["yesterday", "last year", "a decade ago", "in the past", "previously"],
    "PRESENT":["today", "this year", "currently", "nowadays", "at present"],
    "FUTURE":["tomorrow", "next year", "in the future", "upcoming", "soon"]}
class HeadlineGenerator:
    """Generates themed headlines with sentiment and time context modifiers."""
    def __init__(self,keywords="",sentiment ="neutral", time_context ="present", theme ="none"):
        self.keywords = keywords.lower().strip() #KEYWORDS
        self.sentiment = sentiment.lower() #SENTIMENT
        self.time_context = time_context.lower() #time context
        self.theme = theme
        self.confidence_score = 0.0
    

    


#TIME CONTEXT MODIFIERS



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