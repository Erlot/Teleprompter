import tkinter as tk
import nltk


# Ensure nltk's 'punkt' tokenizer is available; uncomment if needed
# nltk.download('punkt')

class TeleprompterApp:
    def __init__(self, root):
        self.root = root
        self.sentences = []
        self.current_index = 0

        self.setup_ui()

    def setup_ui(self):
        self.root.title("Teleprompter Input")

        self.text_entry = tk.Text(self.root, height=15, width=50)
        self.text_entry.pack(pady=20)

        start_btn = tk.Button(self.root, text="Start", command=self.start_prompter)
        start_btn.pack(pady=10)

    def start_prompter(self):
        text = self.text_entry.get("1.0", tk.END)
        paragraphs = [p for p in text.split('\n') if p]  # Split text into non-empty paragraphs

        # Tokenize each paragraph into sentences, adding a "BREAK" between paragraphs
        self.sentences = []
        for paragraph in paragraphs:
            self.sentences.extend(nltk.tokenize.sent_tokenize(paragraph))
            self.sentences.append("BREAK")  # Add "BREAK" after each paragraph

        if self.sentences:
            self.prompter_window = tk.Toplevel()
            self.prompter_window.title("Teleprompter")
            self.prompter_label = tk.Label(self.prompter_window, text="", font=('Helvetica', 18), wraplength=500)
            self.prompter_label.pack(pady=20)

            self.update_display()

            self.prompter_window.bind("<Down>", self.next_sentence)
            self.prompter_window.bind("<Up>", self.previous_sentence)

    def update_display(self):
        # Check if the current sentence is "BREAK"
        if self.sentences[self.current_index] == "BREAK":
            display_text = "BREAK -- Pause Speaking"
        else:
            display_text = self.sentences[self.current_index]
        self.prompter_label.config(text=display_text)

    def next_sentence(self, event):
        if self.current_index < len(self.sentences) - 1:
            self.current_index += 1
            self.update_display()

    def previous_sentence(self, event):
        if self.current_index > 0:
            self.current_index -= 1
            self.update_display()


if __name__ == "__main__":
    root = tk.Tk()
    app = TeleprompterApp(root)
    root.mainloop()
