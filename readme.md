# askup 🧠

A simple, zero‑dependency CLI tool to ask the web using OpenAI’s GPT‑4o search‑preview model. Get concise answers with citations directly in your terminal.

---

## Features

- **Instant Web Search**: Query the internet and get AI‑summarized responses.

- **Context Size Control**: Choose `small`, `medium`, or `large` web search context.

- **Lightweight**: No heavy dependencies—just Python and OpenAI.

- **Easy Installation**: Install globally with `pipx`.

---

## Installation

**1. Using `pipx` (recommended)**

```
pipx install git+https://github.com/darshankrishna7/Askup.git
```

**To upgrade**

```
pipx upgrade askup
```

**2. Manual install (virtualenv)**

```
git clone https://github.com/darshankrishna7/Askup.git
cd askup
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Configuration

Before running askup, you must provide your OpenAI API key.

**A. Export in current session**
```
export OPENAI_API_KEY="sk-..."
```

**B. Persist in your shell config (.zshrc / .bashrc)**
(Optional)

```
echo 'export OPENAI_API_KEY="sk-..."' >> ~/.zshrc
source ~/.zshrc
```

You can also define defaults in a `.env` file at the project root (if you are installing manually):

```
OPENAI_API_KEY=sk-...
WEB_AI_MODEL=gpt-4o-search-preview
WEB_AI_SEARCH_CONTEXT_SIZE=medium
```

## Usage

```
# Show help
askup --help

# Ask a question
askup -q "Why is the sky blue?"

# Change search context size (small | medium | large)
askup -q "What is quantum entanglement?" -c large

# Check tool version
askup --version
```

## Options

| Flag                   | Description                                                 |
|------------------------|-------------------------------------------------------------|
| `-q`, `--question`     | Your web‑searchable question (string)                       |
| `-c`, `--context-size` | Web search context size: `small`, `medium`, or `large`      |
| `--help`         | Show help message                                           |
| `-v`, `--version`      | Show current tool version                                   |


## Improvements

- A way to configure model
- Add a way to edit config file