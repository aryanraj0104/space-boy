# Space Boy

**A lightweight 2D space arcade game built with Python and pygame.**

> Simple setup • Retro feel • Easy to run

---

## 🎮 Overview

**Space Boy** is a small 2D space shooter written in Python. The project is intentionally kept simple so anyone can clone it, install dependencies in one command, and start playing.

The game uses local assets for graphics, audio, and fonts, and stores the high score persistently.

---

## ✨ Features

- 🚀 Classic 2D arcade-style gameplay
- 🎵 Built-in audio and sound effects
- 🖼️ Custom graphics and fonts
- 💾 Persistent high score (`highscore.txt`)
- 🧪 Beginner-friendly Python project

---

## 🧰 Requirements

- **Python 3.8 or higher**
- Works on Windows, macOS, and Linux

All external dependencies are handled automatically.

---

## ⚙️ Setup & Installation (Recommended)

Follow these steps to run the game in an isolated virtual environment.

### 1️⃣ Clone the repository

```bash
git clone https://github.com/aryanraj0104/space-boy.git
cd space-boy
```

### 2️⃣ Create & activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3️⃣ Install all dependencies (ONE command)

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Game

After installing dependencies, start the game with:

```bash
python main.py
```

The game window should open immediately.

---

## 📁 Project Structure

```
space-boy/
├── audio/           # Sound effects and music
├── font/            # Font files used in-game
├── graphics/        # Sprites and image assets
├── highscore.txt    # Stores best score
├── main.py          # Game entry point
├── requirements.txt # Dependencies
├── pyproject.toml   # Project metadata
└── README.md
```

---

## 🎯 Controls

Controls are defined inside `main.py`. Typical mappings include:

- **Move**: Arrow keys / WASD
- **Shoot / Action**: Space
- **Quit**: Escape or window close

(Refer to `main.py` for exact bindings.)

---

## 💾 High Score

The game saves your best score in `highscore.txt`. To reset the score, simply delete or edit this file.

---

## 🎨 Customization

You can easily customize the game:

- Replace sprites in `graphics/`
- Swap sound effects or music in `audio/`
- Change fonts in `font/`

No code changes required.

---

## 📦 Packaging (Optional)

This project includes a `pyproject.toml` for modern Python tooling and future packaging support. Advanced users can install the project locally using:

```bash
pip install .
```

---

## 🤝 Contributing

Contributions are welcome!

Suggestions:
- Improve gameplay mechanics
- Add new enemy types
- Add a menu or pause screen
- Improve documentation

Fork the repo, create a branch, and open a pull request.

---

## 📄 License

No license file is currently included. Consider adding an MIT License if you plan to share or reuse this project publicly.

---

## 👤 Author

Created by **Aryan Raj**

---

Enjoy the game 🚀