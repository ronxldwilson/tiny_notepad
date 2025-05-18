# Tiny Notepad with Ollama

A sleek local notepad app powered by **[Ollama](https://ollama.com/)**. Write notes, chat with open-source language models, and tweak generation settings. Built with a minimal Tkinter-based GUI.
The goal of the project is to be an accessible, light weight version of open-webui capabilities available via a notepad app.

## What is Tiny Notepad?

**Tiny Notepad** is a Python desktop app that allows you to:

* **Write and save timestamped notes**
* **Load previous notes from a sidebar**
* **Interact with any locally installed Ollama model**
* **Adjust LLM generation parameters** like temperature, top\_p, top\_k, etc.

Ideal for journaling, note-taking, or exploring how LLMs respond to prompts — all running entirely on your machine.

---

## Features

* Clean Tkinter GUI
* Local-first: works offline with Ollama
* Sidebar to browse saved notes
* Real-time interaction with models (via Ollama API)
* Editable generation settings:

  * `temperature`
  * `top_p`
  * `top_k`
  * `repeat_penalty`
  * `presence_penalty`
  * `frequency_penalty`
  * `stop` sequences

---

## Installation

1. **Install Python (>=3.7)**

2. **Install Tiny Notepad**

```bash
pip install tiny-notepad
```

3. **Install `ollama` (required)**
   [Download Ollama](https://ollama.com/download) and follow platform-specific installation instructions.

4. **Run a model via Ollama**

Before using the app, make sure a model is pulled and running:

```bash
ollama pull llama3
ollama run llama3
```
OR
```bash
ollama serve
```


---

## Usage

Once installed via `pip`, launch the app using:

```bash
tiny-notepad
```

> The app will auto-check for Ollama and attempt to start `ollama serve` if it's not already running.

---

## Saved Notes

All notes are saved in a `notes/` directory, auto-named like:

```
notes_2025-05-18_14-33-21.txt
```

You can browse and reopen them from the built-in sidebar.

---

## Generation Parameters

| Parameter           | Description                                       | Default    |
| ------------------- | ------------------------------------------------- | ---------- |
| `temperature`       | Controls randomness (0 = deterministic, 2 = wild) | 0.7        |
| `top_p`             | Nucleus sampling (probability threshold)          | 0.9        |
| `top_k`             | Limits to top-k tokens                            | 40         |
| `repeat_penalty`    | Penalizes repeated tokens                         | 1.0        |
| `presence_penalty`  | Encourages new topic exploration                  | 0.0        |
| `frequency_penalty` | Penalizes frequent tokens                         | 0.0        |
| `stop`              | Comma-separated stop sequences to end generation  | *(custom)* |

All parameters can be adjusted in the GUI in real time.

---

## Tip

Pull and try other models using Ollama:

```bash
ollama pull mistral
ollama pull gemma
```

They will appear in the model dropdown after restarting the app.

---

## License

MIT License © 2025 Ronald Wilson

