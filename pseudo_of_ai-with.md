"""
VERSION 3.0 - AI-STYLE WITH CONTEXT
=====================================
This version adds AI-like contextual awareness to generate smarter headlines.

KEY FEATURES:
- Keyword-based headline generation
- Sentiment analysis (positive, negative, neutral)
- Context-aware selection of subjects, verbs, and objects
- Time-based modifiers (past, present, future)
- Relevance scoring for better combinations
- History tracking with metadata
"""

import random
from datetime import datetime

# ============================================================================
# PSEUDO CODE EXPLANATION
# ============================================================================

"""
ALGORITHM: AI-Style Context-Aware Headline Generation

1. INPUT PHASE:
   ├─ Get user input (keyword, sentiment, time context)
   ├─ Validate input
   └─ Extract context parameters

2. CONTEXT ANALYSIS PHASE:
   ├─ Analyze keyword relevance to themes
   ├─ Match sentiment to appropriate verbs/adjectives
   ├─ Determine time context (past/present/future)
   └─ Score theme compatibility

3. INTELLIGENT SELECTION PHASE:
   ├─ Score each subject based on keyword match
   ├─ Select verb based on sentiment + context
   ├─ Choose object that relates to keyword
   ├─ Apply time modifiers if needed
   └─ Calculate relevance score

4. GENERATION PHASE:
   ├─ Build headline with selected components
   ├─ Add contextual modifiers
   ├─ Apply formatting rules
   └─ Return headline with confidence score

5. OUTPUT PHASE:
   ├─ Display headline with metadata
   ├─ Show relevance/confidence score
   ├─ Store in history with full context
   └─ Offer refinement options
"""

# ============================================================================
# THEMES DATABASE
# ============================================================================

THEMES = {
    "space": {
        "subjects": ["The astronaut", "A spaceship", "The alien", "The planet", "The star"],
        "verbs": ["explores", "lands on", "discovers", "orbits", "communicates with"],
        "objects": ["a new galaxy", "the moon", "an alien civilization", "a black hole", "the space station"],
        "keywords": ["space", "galaxy", "astronaut", "alien", "star", "moon", "planet"]
    },
    "technology": {
        "subjects": ["The developer", "A robot", "The AI", "The startup", "The engineer"],
        "verbs": ["creates", "launches", "innovates", "programs", "tests"],
        "objects": ["a new app", "the future of tech", "a groundbreaking algorithm", "the next big thing", "a smart device"],
        "keywords": ["tech", "AI", "app", "algorithm", "robot", "developer", "code"]
    },
    "nature": {
        "subjects": ["The hiker", "A biologist", "The forest", "The river", "The mountain"],
        "verbs": ["discovers", "protects", "explores", "nurtures", "climbs"],
        "objects": ["a rare species", "the ecosystem", "a hidden trail", "the wildlife", "the natural beauty"],
        "keywords": ["nature", "forest", "wildlife", "ecosystem", "hiking", "species", "mountain"]
    },
    "health": {
        "subjects": ["The doctor", "A fitness trainer", "The nutritionist", "The patient", "The researcher"],
        "verbs": ["treats", "advises", "studies", "improves", "discovers"],
        "objects": ["a new treatment", "healthy habits", "the disease", "wellness tips", "medical breakthroughs"],
        "keywords": ["health", "fitness", "doctor", "medicine", "wellness", "treatment", "disease"]
    },
    "education": {
        "subjects": ["The teacher", "A student", "The professor", "The school", "The academic"],
        "verbs": ["teaches", "learns", "discovers", "researches", "innovates"],
        "objects": ["a new curriculum", "the classroom", "educational tools", "academic success", "knowledge"],
        "keywords": ["education", "school", "student", "learning", "teacher", "study", "curriculum"]
    }
}

# ============================================================================
# SENTIMENT MAPPING
# ============================================================================

SENTIMENT_VERBS = {
    "positive": ["discovers", "creates", "achieves", "improves", "celebrates", "succeeds in", "launches"],
    "negative": ["struggles with", "confronts", "battles", "challenges", "faces", "overcomes"],
    "neutral": ["explores", "examines", "studies", "documents", "finds", "presents"]
}

# ============================================================================
# TIME CONTEXT MODIFIERS
# ============================================================================

TIME_MODIFIERS = {
    "past": ["Yesterday", "Last week", "Recently", "Previously"],
    "present": ["Today", "Currently", "Now", "Right now"],
    "future": ["Tomorrow", "Next week", "Soon", "Will soon"]
}

# ============================================================================
# CONTEXT CLASS - Stores user input context
# ============================================================================

class HeadlineContext:
    """
    PSEUDO CODE:
    ─────────────
    CLASS HeadlineContext:
        ATTRIBUTES:
            - keyword: user's search keyword
            - sentiment: emotion level (positive/negative/neutral)
            - time_context: when (past/present/future)
            - theme: selected theme
            - confidence_score: how well match keyword
        
        METHODS:
            - __init__: Initialize with user inputs
            - validate_inputs: Check if inputs are valid
            - get_context_details: Return all context info
    """
    
    def __init__(self, keyword="", sentiment="neutral", time_context="present", theme=None):
        self.keyword = keyword.lower().strip()
        self.sentiment = sentiment.lower()
        self.time_context = time_context.lower()
        self.theme = theme
        self.confidence_score = 0.0
    
    def validate_inputs(self):
        """Check if inputs are valid"""
        if self.sentiment not in SENTIMENT_VERBS:
            self.sentiment = "neutral"
        if self.time_context not in TIME_MODIFIERS:
            self.time_context = "present"
        return True
    
    def get_context_details(self):
        """Return all context information"""
        return {
            "keyword": self.keyword,
            "sentiment": self.sentiment,
            "time_context": self.time_context,
            "theme": self.theme,
            "confidence": self.confidence_score
        }

# ============================================================================
# MATCHER CLASS - Finds best theme for keyword
# ============================================================================

class ContextMatcher:
    """
    PSEUDO CODE:
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
    
    @staticmethod
    def match_keyword_to_theme(keyword):
        """Find the best theme for the given keyword"""
        if not keyword:
            return random.choice(list(THEMES.keys()))
        
        scores = {}
        
        for theme_name, theme_data in THEMES.items():
            score = 0
            keywords = theme_data["keywords"]
            
            # Check for keyword matches
            for tkeyword in keywords:
                if keyword in tkeyword or tkeyword in keyword:
                    score += 2  # Direct match gets higher score
                elif keyword[0:3] in tkeyword:  # First 3 letters match
                    score += 1
            
            if score > 0:
                scores[theme_name] = score
        
        # Return theme with highest score, or random if no match
        if scores:
            best_theme = max(scores, key=scores.get)
            confidence = scores[best_theme] / 10.0  # Normalize confidence
            return best_theme, min(confidence, 1.0)
        
        return random.choice(list(THEMES.keys())), 0.5

    @staticmethod
    def select_components(context):
        """
        PSEUDO CODE:
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
        theme_data = THEMES[context.theme]
        
        # Select subject (random from theme)
        subject = random.choice(theme_data["subjects"])
        
        # Select verb based on sentiment
        sentiment_verbs = SENTIMENT_VERBS.get(context.sentiment, SENTIMENT_VERBS["neutral"])
        available_verbs = sentiment_verbs + theme_data["verbs"]
        verb = random.choice(available_verbs)
        
        # Select object (prefer those matching keyword if available)
        objects = theme_data["objects"]
        if context.keyword:
            matching_objects = [obj for obj in objects if context.keyword in obj]
            obj = random.choice(matching_objects) if matching_objects else random.choice(objects)
        else:
            obj = random.choice(objects)
        
        return subject, verb, obj

# ============================================================================
# HEADLINE GENERATOR CLASS - Main AI engine
# ============================================================================

class AIHeadlineGenerator:
    """
    PSEUDO CODE:
    ─────────────
    CLASS AIHeadlineGenerator:
        METHOD generate_headline(keyword, sentiment, time_context):
            
            // STEP 1: Create context
            context = NEW HeadlineContext(keyword, sentiment, time_context)
            context.validate_inputs()
            
            // STEP 2: Match keyword to best theme
            context.theme, confidence = ContextMatcher.match_keyword_to_theme(keyword)
            context.confidence_score = confidence
            
            // STEP 3: Select components
            subject, verb, object = ContextMatcher.select_components(context)
            
            // STEP 4: Build headline with time modifier
            time_modifier = RANDOM_CHOICE(TIME_MODIFIERS[context.time_context])
            
            IF context.time_context != "present":
                headline = f"{time_modifier}, {subject} {verb} {object}."
            ELSE:
                headline = f"{subject} {verb} {object}."
            
            // STEP 5: Return headline with metadata
            RETURN {
                "headline": headline,
                "theme": context.theme,
                "sentiment": context.sentiment,
                "confidence": context.confidence_score,
                "timestamp": CURRENT_TIME
            }
    """
    
    def __init__(self):
        self.headline_history = []
    
    def generate_headline(self, keyword="", sentiment="neutral", time_context="present"):
        """Generate AI-style contextual headline"""
        
        # Step 1: Create and validate context
        context = HeadlineContext(keyword, sentiment, time_context)
        context.validate_inputs()
        
        # Step 2: Match keyword to best theme
        if keyword:
            theme, confidence = ContextMatcher.match_keyword_to_theme(keyword)
            context.theme = theme
            context.confidence_score = confidence
        else:
            context.theme = random.choice(list(THEMES.keys()))
            context.confidence_score = 0.8
        
        # Step 3: Select components
        subject, verb, obj = ContextMatcher.select_components(context)
        
        # Step 4: Build headline with time modifier
        time_modifier = random.choice(TIME_MODIFIERS[context.time_context])
        
        if context.time_context != "present":
            headline = f"{time_modifier}, {subject} {verb} {obj}."
        else:
            headline = f"{subject} {verb} {obj}."
        
        # Step 5: Create result with metadata
        result = {
            "headline": headline,
            "theme": context.theme,
            "sentiment": context.sentiment,
            "time_context": context.time_context,
            "keyword": keyword,
            "confidence": round(context.confidence_score, 2),
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        
        # Store in history
        self.headline_history.append(result)
        
        return result
    
    def display_result(self, result):
        """Display headline with all metadata"""
        print("\n" + "="*70)
        print("📰 AI-GENERATED HEADLINE")
        print("="*70)
        print(f"Headline: {result['headline']}")
        print(f"Theme: {result['theme'].capitalize()}")
        print(f"Sentiment: {result['sentiment'].capitalize()}")
        print(f"Time Context: {result['time_context'].capitalize()}")
        print(f"Keyword Match: {result['keyword'] if result['keyword'] else 'None'}")
        print(f"Confidence Score: {result['confidence']*100:.0f}%")
        print(f"Generated At: {result['timestamp']}")
        print("="*70 + "\n")
    
    def show_history(self):
        """Display all generated headlines"""
        if not self.headline_history:
            print("No headlines generated yet!")
            return
        
        print("\n" + "="*70)
        print("📜 HEADLINE HISTORY")
        print("="*70)
        for i, result in enumerate(self.headline_history[-10:], 1):
            print(f"{i}. {result['headline']} (Confidence: {result['confidence']*100:.0f}%)")
        print("="*70 + "\n")

# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """Main program execution"""
    print("\n" + "="*70)
    print("🤖 HEADLINE GENERATOR v3.0 - AI WITH CONTEXT")
    print("="*70)
    
    generator = AIHeadlineGenerator()
    
    while True:
        print("\nOptions:")
        print("1. Generate with keyword")
        print("2. Generate with sentiment")
        print("3. Generate with time context")
        print("4. Generate with all options")
        print("5. View history")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            keyword = input("Enter keyword (e.g., 'tech', 'health', 'space'): ")
            result = generator.generate_headline(keyword=keyword)
            generator.display_result(result)
        
        elif choice == "2":
            print("Sentiments: positive, negative, neutral")
            sentiment = input("Enter sentiment: ").strip()
            result = generator.generate_headline(sentiment=sentiment)
            generator.display_result(result)
        
        elif choice == "3":
            print("Time contexts: past, present, future")
            time_context = input("Enter time context: ").strip()
            result = generator.generate_headline(time_context=time_context)
            generator.display_result(result)
        
        elif choice == "4":
            keyword = input("Enter keyword (optional): ")
            sentiment = input("Enter sentiment (positive/negative/neutral): ")
            time_context = input("Enter time context (past/present/future): ")
            result = generator.generate_headline(keyword=keyword, sentiment=sentiment, time_context=time_context)
            generator.display_result(result)
        
        elif choice == "5":
            generator.show_history()
        
        elif choice == "6":
            print("\nThank you for using Headline Generator v3.0!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()