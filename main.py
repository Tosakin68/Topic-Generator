import random
import json
from tkinter import *

# Liste der möglichen Themen
# Öffne die JSON-Datei
with open("themes.json", "r",encoding="utf-8") as f:
  # Lese den Inhalt der Datei als JSON-Objekt
  themes_json = json.load(f)

# Konvertiere das JSON-Objekt in eine Liste von Themen
gaming = themes_json["gaming"]
movies = themes_json["movies"]
music = themes_json["music"]

# Funktion zum Generieren eines zufälligen Themas
def generate_theme():
  theme_label.config(text=random.choice(music))

# Erstelle das Hauptfenster
window = Tk()
window.title("Topic-Generator")
window.iconbitmap("icon.ico")
window.minsize(600, 400)

# Erstelle die Kombobox für die Themenbereiche
category_var = StringVar(window)
category_var.set("all") # Standardauswahl
category_dropdown = OptionMenu(window, category_var, "all", "gaming", "movies", "music")
category_dropdown.pack()

def update_themes(category):

  # Aktualisiere das Label mit einem zufälligen Thema
  if(category == "all"):
    choices = [gaming, movies, music]
    random_string = random.choice(choices)
    theme_label.config(text=random.choice(random_string))
  else:
    if(category == "gaming"):
        category = gaming
    if(category == "movies"):
        category = movies
    if (category == "music"):
        category = music

    theme_label.config(text=random.choice(category))

category_var.trace("w", lambda *args: update_themes(category_var.get()))

# Erstelle ein Label zur Anzeige des generierten Themas
theme_label = Label(window, text="")
theme_label.pack()
theme_label.place(relx=0.5, rely=0.5, anchor="center")

# Erstelle einen Button zum Generieren eines Themas
generate_button = Button(window, text="Generate Topic", command=generate_theme)
generate_button.pack()
generate_button.place(relx=0.5, rely=0.6, anchor="center")

generate_button.config(command=lambda: update_themes(category_var.get()))

# Starte die GUI-Schleife
window.mainloop()