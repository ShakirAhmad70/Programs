import tkinter as tk
import nltk
from nltk.corpus import wordnet

class DictionaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dictionary App")

        self.label = tk.Label(root, text="Enter a word:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Get Definition", command=self.get_definition)
        self.button.pack()

        self.definition_text = tk.Text(root)
        self.definition_text.pack()

    def get_definition(self):
        word = self.entry.get()
        definition = self.get_word_definition(word)
        
        self.definition_text.delete(1.0, tk.END)
        self.definition_text.insert(tk.END, definition)

    def get_word_definition(self, word):
        synsets = wordnet.synsets(word)
        if synsets:
            return synsets[0].definition()
        else:
            return "Word not found."

if __name__ == "__main__":
    # Download NLTK data if not already downloaded
    nltk.download('wordnet')
    
    root = tk.Tk()
    app = DictionaryApp(root)
    root.mainloop()
