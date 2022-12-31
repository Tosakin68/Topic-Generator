import random
import json
from tkinter import *

# Liste der möglichen Themen
# Öffne die JSON-Datei
with open("themes.json", "r",encoding="utf-8") as f:
  # Lese den Inhalt der Datei als JSON-Objekt
  themes_json = json.load(f)

# Konvertiere das JSON-Objekt in eine Liste von Themen
themes = themes_json["themes"]

# Funktion zum Generieren eines zufälligen Themas
def generate_theme():
  theme_label.config(text=random.choice(themes))

# Erstelle das Hauptfenster
window = Tk()
window.title("Topic-Generator")
window.iconbitmap("icon.ico")
window.minsize(600, 400)

# Erstelle ein Label zur Anzeige des generierten Themas
theme_label = Label(window, text="")
theme_label.pack()
theme_label.place(relx=0.5, rely=0.5, anchor="center")

# Erstelle einen Button zum Generieren eines Themas
generate_button = Button(window, text="Generate Topic", command=generate_theme)
generate_button.pack()
generate_button.place(relx=0.5, rely=0.6, anchor="center")

# Starte die GUI-Schleife
window.mainloop()