# 🎛️ StreamDeck - Midnight Maker Edition

**When regular buttons just won't glow enough**  
*Crafted at 11 PM between smoke alarms and questionable YouTube choices*

![StreamDeck Interface](https://github.com/otoua046/StreamDeck/blob/main/assets/Screenshot%202025-01-27%20at%2011.41.27%E2%80%AFPM.png?raw=true)  
*(Actual proof it worked once)*

## 🚀 Features
- ✨ YouTube-to-MP3 sorcery (100% legal* *may contain traces of fair use)
- 🌌 Interface that blinds you with science (literally)
- 🔥 One-click audio anarchy
- 🏃♂️ `run` script for maximum lazy efficiency
- ☕ Powered by questionable life choices and burnt garlic

## ⚙️ Setup (For the "I Want It Now" Crowd)

```bash
# 1. Clone this sleep-deprived creation
git clone https://github.com/yourusername/StreamDeck.git
cd StreamDeck

# 2. Bless the run script with executable powers
chmod +x run  # This counts as DevOps experience

# 3. Launch our digital Frankenstein
./run
```

## 🧑💻 Manual Setup (For Terminal Warriors)

```bash
# 1. Conda environment setup
conda create -n streamdeck python=3.8
conda activate streamdeck  # Enter the neon matrix

# 2. Install requirements.txt
conda install --yes --file requirements.txt  # It's 3 packages but let's pretend

# 3. FFmpeg installation (audio wrangling magic)
# [FFmpeg.org](https://ffmpeg.org/download.html) - Install like a pro

# 4. Edit YOUTUBE_URLS in stream_deck.py
# Expert move: Add elevator music for maximum chaos

# 5. Ignite the chaos!
python stream_deck.py
```

## 🔮 Coming Soon(ish)
- 📦 3D printed case (designed between pizza bites)
- 🔌 ESP32 integration (for that sweet IoT street cred)
- 🎚️ Mechanical switches that wake the neighbors
- 🤖 AI companion that judges your music taste
- 🔥 Literal smoke machine support (patent pending)

## 🍳 Kitchen Confidential
This project was:
- Built instead of sleeping like a normal person
- Tested on 1 (one) bewildered houseplant
- Fueled by questionable midnight snacks
- Documented through gritted teeth
- Named during a Wikipedia black hole session

*"Couldn't you just use a normal soundboard?" - Everyone who doesn't get it*

---

**Tech Stuff (For the Boring Police):**  
- `requirements.txt`:
  ```txt
  flask==2.0.1          # For web magic
  yt-dlp==2021.12.27    # YouTube wrangler
  python-slugify==5.0.2 # Makes filenames less terrible
  ```

- `run.sh` Incantation:
  ```bash
  #!/usr/bin/env bash
  eval "$(conda shell.bash hook)"  # Conda dark arts
  conda activate streamdeck         # Neon mode activated
  python stream_deck.py            # Release the hounds!
  ```

**Warning:** May cause sudden urges to buy 3D printers. Not responsible for RGB addiction or garlic bread cravings.  

*Crafted with AI and regret by Sam*  
*"It worked on my machine" warranty included*
