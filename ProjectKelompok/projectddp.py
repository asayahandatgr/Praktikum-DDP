import tkinter as tk
import winsound
from tkinter import ttk
from googletrans import Translator
import ttkbootstrap as ttk


class TranslateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Translator App")
        self.translator = Translator()

        self.style = ttk.Style("vapor")

        self.input_text = tk.StringVar()
        self.output_text = tk.StringVar()

        self.label_input = ttk.Label(root, text="Enter Text:")
        self.entry_input = ttk.Entry(root, textvariable=self.input_text, width=40)
        self.label_input.grid(row=0, column=0, padx=10, pady=10)
        self.entry_input.grid(row=0, column=1, padx=10, pady=10)

        self.entry_input.insert(0, "Masukkan teks disini")
        self.entry_input.bind("<FocusIn>", self.clear_placeholder)

        self.label_output = ttk.Label(root, text="Detect Text:")
        self.entry_output = ttk.Entry(
            root, textvariable=self.output_text, width=40, state="readonly"
        )
        self.label_output.grid(row=1, column=0, padx=10, pady=10)
        self.entry_output.grid(row=1, column=1, padx=10, pady=10)

        self.btn_translate = ttk.Button(
            root, text="Translate", command=self.translate_text
        )
        self.btn_translate.grid(row=2, column=1, pady=10)

        self.translation_direction = ttk.Combobox(
            root,
            values=[
                "English to Indonesian",
                "Indonesian to English",
                "Arab to Indonesian",
                "Indonesian to Arab",
            ],
        )
        self.translation_direction.set("English to Indonesian")
        self.translation_direction.grid(row=2, column=0, padx=10, pady=10)

    def clear_placeholder(self, event):
        if self.entry_input.get() == "Masukkan teks disini":
            self.entry_input.delete(0, tk.END)

    def translate_text(self):
        input_text = self.input_text.get()

        selected_direction = self.translation_direction.get()

        src_lang, dest_lang = (
            ("en", "id")
            if "English to Indonesian" in selected_direction
            else ("id", "en")
            if "Indonesian to English" in selected_direction
            else ("ar", "id")
            if "Arab to Indonesian" in selected_direction
            else ("id", "ar")
        )

        translated_text = self.translator.translate(
            input_text, src=src_lang, dest=dest_lang
        ).text

        frequency = 1500 
        duration = 1000
        winsound.Beep(frequency, duration)

        self.output_text.set(translated_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = TranslateApp(root)
    root.mainloop()