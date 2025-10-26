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
    def validate_inputs(self):
       """Check if inputs are valid"""
       if self.sentiment not in SENTIMENT_VERBS:
        self.sentiment = "Neutral"
       if self.time_context not in TIME_CONTEXT_MODIFIERS:
        self.time_context = "present"
        return True
    def get_context_details(self):
       """Return all context information"""
       return{
          "keywords": self.keywords,
          "sentiment":self.sentiment,
          "time_context" :self.time_context,
          "theme": self.theme,
          "confidence":self.confidence_score
       }

#matcher class
class ContextMatcher:
   """PSEUDO CODE:
    ─────────────
    CLASS ContextMatcher:
        METHOD match_keyword_to_theme(keyword):
            FOR each theme IN themes:
                score = 0
                FOR each theme_keyword IN theme.keywords:
                    IF keyword IN theme_keyword OR theme_keyword IN keyword:
                        score += 1
                IF score > 0:
                    ADD (theme, score) TO matches
            
            RETURN theme with highest score
    """
   def match_keyword_theme(keyword):
      """ find the best theme for the given keyword"""
      if not keyword:
         return random.choice(list(Themes.keys))
      score = {}
      for theme_name, theme_data in Themes.items():
         scores = 0
         keywords = theme_data["keywords"]

         #check keywords matches 
         for tkeyword in keywords:
             if keyword in tkeyword or  tkeyword in keyword:
                score += 2 #direct match get higher score 
             elif keyword[0:3] in tkeyword :
                score += 1         
         if score  > 0:
            score[theme_name] = score 
        #return theme with highest score,or random if no match
      if scores:
         best_theme = max(scores, key=scores.get)
         confidence = score[best_theme] /10.0
         return best_theme,min(confidence,1.0)
      return random.choice(list(Themes.keys())),0.5
   @staticmethod 
   def select_components(context):
      """PSEUDO CODE:
        ─────────────
        METHOD select_components(context):
            theme = context.theme
            sentiment = context.sentiment
            
            // Subject selection: Random from theme
            subject = RANDOM_CHOICE(theme.subjects)
            
            // Verb selection: Based on sentiment
            verb_pool = SENTIMENT_VERBS[sentiment]
            verb = RANDOM_CHOICE(verb_pool)
            
            // Object selection: Prefer ones matching keyword
            object = RANDOM_CHOICE(theme.objects)
            
            RETURN (subject, verb, object)
           """
      

    

    


#TIME CONTEXT MODIFIERS



    