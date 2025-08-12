FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    LANG=C.UTF-8 \
    MECABRC=/etc/mecabrc \
    NLTK_DATA=/usr/local/nltk_data

WORKDIR /app

# 1) Dependencias del sistema (audio + MeCab + git)
RUN apt-get update && apt-get install -y \
    ffmpeg git espeak-ng \
    mecab libmecab2 mecab-ipadic-utf8 \
    && echo "dicdir = /var/lib/mecab/dic/ipadic" > /etc/mecabrc \
    && mkdir -p /usr/local/lib/python3.10/site-packages/unidic \
    && ln -s /var/lib/mecab/dic/ipadic /usr/local/lib/python3.10/site-packages/unidic/dicdir \
    && printf "dicdir = /var/lib/mecab/dic/ipadic\n" > /usr/local/lib/python3.10/site-packages/unidic/dicdir/mecabrc \
    && rm -rf /var/lib/apt/lists/*


# 2) Instalar unidic-lite (no requiere "download")
RUN pip install --no-cache-dir unidic-lite

# (Opcional) Verificar que unidic_lite trae diccionario
RUN python - <<'PY'
import unidic_lite, os
print("UniDic-lite DICDIR:", unidic_lite.DICDIR)
assert os.path.isdir(unidic_lite.DICDIR)
PY

# 3) Instalar dependencias de Python del proyecto
COPY requirements-melotts.txt .
RUN pip install --no-cache-dir -r requirements-melotts.txt

# 4) Descargar datos NLTK necesarios
RUN python - <<'PY'
import os, nltk
os.makedirs(os.environ.get("NLTK_DATA", "/usr/local/nltk_data"), exist_ok=True)
for pkg in ["averaged_perceptron_tagger_eng", "averaged_perceptron_tagger", "punkt", "cmudict"]:
    try:
        nltk.download(pkg, download_dir=os.environ["NLTK_DATA"])
    except Exception as e:
        print("NLTK download failed for", pkg, e)
PY

# 5) Copiar el código
COPY . .

# 6) Entry point
ENTRYPOINT ["python", "app/controllers/listening/generate_audio.py"]
