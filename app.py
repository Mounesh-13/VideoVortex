from flask import Flask, request, send_file, render_template
import yt_dlp
import os
import re

app = Flask(__name__)

def detect_platform(url):
    if re.search(r'youtube\.com|youtu\.be', url):
        return 'youtube'
    elif re.search(r'instagram\.com', url):
        return 'instagram'
    elif re.search(r'twitter\.com|x\.com', url):
        return 'twitter'
    else:
        return 'unknown'

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None

    if request.method == 'POST':
        url = request.form['url']

        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'format': 'best' # Always download best
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                filename = ydl.prepare_filename(info_dict)
                ydl.download([url])

            return send_file(filename, as_attachment=True)

        except Exception as e:
            error = str(e)

    return render_template('index.html', error=error)

if __name__ == '__main__':
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    app.run(debug=True)