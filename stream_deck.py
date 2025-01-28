import os
from flask import Flask, render_template_string, url_for
import yt_dlp

###############################################################################
# CONFIGURATION
###############################################################################

# List of YouTube URLs to download
YOUTUBE_URLS = [
    "https://youtu.be/dumKjvADbZE?si=Vg-JVvlj21KIDq4W",
    "https://youtu.be/qJiF3fxJiEU?si=xtoFtOJExui9r5SH",
    "https://youtu.be/8aRCmMlCcY0?si=sQccQMXPflsfcqwI",
    "https://youtu.be/VUfvRciny_Y?si=Dm3L7xkwiUfpNp1i",
    "https://www.youtube.com/watch?v=3gCBFKHVJVA"
]

# Where to store MP3 files
MP3_FOLDER = os.path.join("static", "sounds")

# Updated HTML Template (no more Python's enumerate; using loop.index instead)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stream Deck - Modern Sound Deck</title>
    <!-- Font Awesome Icons -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', sans-serif;
        }

        body {
            background: #1a1a1a;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: radial-gradient(circle at center, #2a2a2a, #1a1a1a);
        }

        .deck-container {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        h1 {
            color: #fff;
            text-align: center;
            margin-bottom: 30px;
            font-weight: 300;
            text-transform: uppercase;
            letter-spacing: 2px;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
        }

        .button-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 15px;
        }

        .deck-button {
            width: 80px;
            height: 80px;
            background: rgba(255, 255, 255, 0.1);
            border: none;
            border-radius: 15px;
            color: #fff;
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        .deck-button:hover {
            background: rgba(255, 255, 255, 0.15);
            transform: scale(1.05);
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.2);
        }

        .deck-button.active {
            background: rgba(0, 255, 255, 0.2);
            box-shadow: 0 0 25px rgba(0, 255, 255, 0.3);
        }

        .deck-button i {
            font-size: 24px;
            margin-bottom: 5px;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
        }

        .button-label {
            font-size: 14px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        @media (max-width: 768px) {
            .button-grid {
                grid-template-columns: repeat(3, 1fr);
            }
        }
    </style>
</head>
<body>
    <div class="deck-container">
        <h1>Stream Deck</h1>
        <div class="button-grid">
            <!-- We rely on Jinja's loop.index to number the buttons -->
            {% for sound in sound_files %}
            <button class="deck-button" onclick="handleClick(this, '{{ url_for('static', filename='sounds/' ~ sound) }}')">
                <i class="fas fa-music"></i>
                <span class="button-label">{{ loop.index }}</span>
            </button>
            {% endfor %}
        </div>
    </div>

    <!-- Hidden audio player -->
    <audio id="audio-player" controls style="display:none;"></audio>

    <script>
        const audioPlayer = document.getElementById('audio-player');

        function handleClick(button, soundUrl) {
            // Toggle visual 'active' state
            button.classList.toggle('active');

            // Play the selected MP3
            audioPlayer.src = soundUrl;
            audioPlayer.play();

            // Log the button clicked
            console.log(`Button #${button.querySelector('.button-label').textContent} clicked!`);
        }
    </script>
</body>
</html>
"""

###############################################################################
# DOWNLOAD FUNCTION (yt-dlp -> MP3)
###############################################################################

def download_mp3(url):
    """
    Uses yt-dlp to download the best audio and convert it to MP3 directly
    (via FFmpegExtractAudio post-processor). The final MP3 is stored in
    static/sounds.
    """
    os.makedirs(MP3_FOLDER, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(MP3_FOLDER, '%(title).200s.%(ext)s'),
        'quiet': False,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
        ],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

###############################################################################
# PREPARE: DOWNLOAD ALL MP3S
###############################################################################

for link in YOUTUBE_URLS:
    download_mp3(link)

###############################################################################
# FLASK APP
###############################################################################

app = Flask(__name__)

@app.route("/")
def index():
    # Grab all .mp3 files from static/sounds
    sound_files = [f for f in os.listdir(MP3_FOLDER) if f.endswith('.mp3')]
    # Render the HTML with the file list
    return render_template_string(HTML_TEMPLATE, sound_files=sound_files)

if __name__ == "__main__":
    app.run(debug=True, port=5050)