FROM python:3.10-slim

WORKDIR /app

# Install necessary system dependencies and clean up
RUN apt-get update && apt-get install -y \
    ffmpeg git espeak-ng \
    mecab libmecab2 mecab-ipadic-utf8 \
    && rm -rf /var/lib/apt/lists/*

# Set the MECABRC environment variable
ENV MECABRC=/etc/mecabrc

# Clone unidic_lite directly from GitHub
RUN git clone https://github.com/megagonlabs/unidic_lite.git /unidic_lite

# Install Python dependencies from requirements file
COPY requirements-melotts.txt .  # Ensure the requirements file is copied before installation
RUN pip install --no-cache-dir -r requirements-melotts.txt

# Install unidic_lite
WORKDIR /unidic_lite
RUN python -m unidic_lite.download

# Setup NLTK data for the necessary packages
ENV NLTK_DATA=/usr/local/nltk_data
RUN python - <<'PY'
import os, nltk
os.makedirs(os.environ.get("NLTK_DATA", "/usr/local/nltk_data"), exist_ok=True)
for pkg in ["averaged_perceptron_tagger_eng", "averaged_perceptron_tagger", "cmudict"]:
    nltk.download(pkg, download_dir=os.environ["NLTK_DATA"])
PY

# Copy the application code into the container
COPY . .

# Set the entrypoint to start the audio generation script
ENTRYPOINT ["python", "app/controllers/listening/generate_audio.py"]
