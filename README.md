# 📝 Tiny Notepad with Ollama

A sleek local notepad app powered by [Ollama](https://ollama.com/) to generate text using LLMs. Write notes, chat with models, and tweak generation parameters — all in a clean Tkinter-based GUI.


## Features

- Save timestamped notes
- Load & view past notes from sidebar
- Query any installed Ollama model
- Adjustable generation settings:
  - `temperature`
  - `top_p`
  - `top_k`
  - `repeat_penalty`
  - `presence_penalty`
  - `frequency_penalty`
  - `stop sequences`

---

## 💡 What is Ollama?

Ollama lets you run open-source large language models **locally**, including LLaMA, Mistral, Gemma, and more. It provides a lightweight API on `localhost:11434`.

Install Ollama from: https://ollama.com

Once installed, load a model like this:

```bash
ollama run llama3.2
````

---

## 🚀 How to Run This App

1. **Install Python dependencies** (if not already):

   ```bash
   pip install requests
   ```

2. **Start the app**:

   ```bash
   python tiny_notepad.py
   ```

3. If Ollama isn't running, the app will try to start `ollama serve` for you.

---

## 🎛️ Model Parameters Explained

| Parameter           | Purpose                                             | Default    |
| ------------------- | --------------------------------------------------- | ---------- |
| `temperature`       | Controls randomness (0 = deterministic, 2 = wild)   | 0.7        |
| `top_p`             | Limits tokens to a cumulative probability (nucleus) | 0.9        |
| `top_k`             | Limits to top-k likely tokens                       | 40         |
| `repeat_penalty`    | Penalizes repeated phrases                          | 1.0        |
| `presence_penalty`  | Encourages new topics                               | 0.0        |
| `frequency_penalty` | Penalizes high-frequency terms                      | 0.0        |
| `stop`              | Comma-separated strings to halt generation          | *(custom)* |

---

## 📁 Notes Location

All saved notes are stored in the `notes/` folder and autosaved as `notes_YYYY-MM-DD_HH-MM-SS.txt`.

---

## ✨ Tip

You can install additional models via:

```bash
ollama pull mistral
ollama pull llama3
```

Then restart the app and pick them from the dropdown.
