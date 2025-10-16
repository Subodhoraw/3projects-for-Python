import random
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime

class HeadlineGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Themed Headline Generator v3.0")
        self.root.geometry("700x650")
        self.root.config(bg="#f0f0f0")
        
        # Headline history
        self.headline_history = []
        
        # Define themes
        self.themes = {
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
            }
        }
        
        self.setup_ui()
    
    def setup_ui(self):
        # Header
        header_frame = tk.Frame(self.root, bg="#2c3e50")
        header_frame.pack(fill="x", padx=0, pady=0)
        
        title_label = tk.Label(header_frame, text="📰 Themed Headline Generator v3.0", 
                              font=("Arial", 16, "bold"), bg="#2c3e50", fg="white")
        title_label.pack(pady=15)
        
        # Main content frame
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=20, pady=15)
        
        # Theme selection section
        theme_label = tk.Label(main_frame, text="Select a Theme:", font=("Arial", 12, "bold"), bg="#f0f0f0")
        theme_label.pack(anchor="w", pady=(0, 10))
        
        theme_frame = tk.Frame(main_frame, bg="#f0f0f0")
        theme_frame.pack(fill="x", pady=(0, 15))
        
        # Dropdown menu
        theme_options = list(self.themes.keys())
        self.theme_var = tk.StringVar(value=theme_options[0])
        theme_dropdown = ttk.Combobox(theme_frame, textvariable=self.theme_var, 
                                     values=theme_options, state="readonly", width=25, font=("Arial", 11))
        theme_dropdown.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        # Buttons frame
        button_frame = tk.Frame(theme_frame, bg="#f0f0f0")
        button_frame.pack(side="left")
        
        generate_btn = tk.Button(button_frame, text="Generate Headline", command=self.generate_headline,
                                bg="#3498db", fg="white", font=("Arial", 10, "bold"), padx=15, pady=8)
        generate_btn.pack(side="left", padx=(0, 5))
        
        random_btn = tk.Button(button_frame, text="Random Theme", command=self.generate_random,
                              bg="#e74c3c", fg="white", font=("Arial", 10, "bold"), padx=15, pady=8)
        random_btn.pack(side="left")
        
        # Headline display section
        headline_label = tk.Label(main_frame, text="Generated Headline:", font=("Arial", 12, "bold"), bg="#f0f0f0")
        headline_label.pack(anchor="w", pady=(10, 5))
        
        headline_box = tk.Frame(main_frame, bg="white", relief="sunken", borderwidth=2)
        headline_box.pack(fill="x", pady=(0, 15))
        
        self.headline_display = tk.Label(headline_box, text="Click 'Generate Headline' to start",
                                        font=("Arial", 14, "italic"), bg="white", fg="#34495e", wraplength=600, pady=20)
        self.headline_display.pack(fill="both", expand=True)
        
        # Control buttons
        control_frame = tk.Frame(main_frame, bg="#f0f0f0")
        control_frame.pack(fill="x", pady=(0, 15))
        
        copy_btn = tk.Button(control_frame, text="📋 Copy", command=self.copy_headline,
                            bg="#27ae60", fg="white", font=("Arial", 10), padx=15, pady=8)
        copy_btn.pack(side="left", padx=(0, 5))
        
        save_btn = tk.Button(control_frame, text="💾 Save", command=self.save_headline,
                            bg="#8e44ad", fg="white", font=("Arial", 10), padx=15, pady=8)
        save_btn.pack(side="left", padx=(0, 5))
        
        history_btn = tk.Button(control_frame, text="📜 History", command=self.show_history,
                               bg="#f39c12", fg="white", font=("Arial", 10), padx=15, pady=8)
        history_btn.pack(side="left")
        
        # History display
        history_label = tk.Label(main_frame, text="Recent Headlines:", font=("Arial", 11, "bold"), bg="#f0f0f0")
        history_label.pack(anchor="w", pady=(10, 5))
        
        self.history_display = scrolledtext.ScrolledText(main_frame, height=6, font=("Arial", 9),
                                                         bg="white", relief="sunken", borderwidth=1)
        self.history_display.pack(fill="both", expand=True, pady=(0, 15))
        self.history_display.config(state="disabled")
        
        # Footer
        footer_frame = tk.Frame(self.root, bg="#34495e")
        footer_frame.pack(fill="x", padx=0, pady=0)
        
        footer_label = tk.Label(footer_frame, text="v3.0 | Made with Python & Tkinter", 
                               font=("Arial", 9), bg="#34495e", fg="white")
        footer_label.pack(pady=10)
    
    def generate_headline(self):
        selected_theme = self.theme_var.get()
        subject = random.choice(self.themes[selected_theme]["subjects"])
        verb = random.choice(self.themes[selected_theme]["verbs"])
        obj = random.choice(self.themes[selected_theme]["objects"])
        headline = f"{subject} {verb} {obj}."
        
        self.headline_display.config(text=headline, fg="#2c3e50")
        
        # Add to history
        timestamp = datetime.now().strftime("%H:%M:%S")
        history_entry = f"[{timestamp}] {headline}"
        self.headline_history.insert(0, history_entry)
        self.update_history_display()
    
    def generate_random(self):
        random_theme = random.choice(list(self.themes.keys()))
        self.theme_var.set(random_theme)
        self.generate_headline()
    
    def copy_headline(self):
        headline_text = self.headline_display.cget("text")
        if headline_text and headline_text != "Click 'Generate Headline' to start":
            self.root.clipboard_clear()
            self.root.clipboard_append(headline_text)
            messagebox.showinfo("Copied", "Headline copied to clipboard!")
        else:
            messagebox.showwarning("No Headline", "Generate a headline first!")
    
    def save_headline(self):
        headline_text = self.headline_display.cget("text")
        if headline_text and headline_text != "Click 'Generate Headline' to start":
            try:
                with open("headlines.txt", "a") as file:
                    file.write(f"{headline_text}\n")
                messagebox.showinfo("Saved", "Headline saved to 'headlines.txt'!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save: {str(e)}")
        else:
            messagebox.showwarning("No Headline", "Generate a headline first!")
    
    def show_history(self):
        if not self.headline_history:
            messagebox.showinfo("History", "No headlines generated yet!")
        else:
            history_text = "\n".join(self.headline_history[:10])
            messagebox.showinfo("Recent Headlines", history_text)
    
    def update_history_display(self):
        self.history_display.config(state="normal")
        self.history_display.delete(1.0, tk.END)
        for entry in self.headline_history[:10]:
            self.history_display.insert(tk.END, entry + "\n")
        self.history_display.config(state="disabled")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = HeadlineGeneratorApp(root)
    root.mainloop()