import requests
import json
import tkinter as tk

def words():
    word = word_entry.get()
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    r = requests.get(url)
    dict = json.loads(r.text)
    try:
        data = dict[0]["meanings"][0]["definitions"][0]["definition"]
        output_label.config(text=f"{data}")
    except Exception:
        output_label.config(text="Error")

window = tk.Tk()
window.title("Dictionary")

word_label = tk.Label(window,text="Enter the Word")
word_label.pack()

word_entry = tk.Entry(window)
word_entry.pack()

search_button = tk.Button(window,text="Search",command=words)
search_button.pack()

output_label = tk.Label(window,text="")
output_label.pack()

window.mainloop()

