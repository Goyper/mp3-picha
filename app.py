from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    url = request.json.get('url')
    if not url:
        return {'error': 'No URL provided'}, 400
    
    # Configurar yt-dlp para la conversión a MP3
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info_dict)
        mp3_filename = filename.replace('.webm', '.mp3').replace('.mp4', '.mp3')
        os.rename(filename, mp3_filename)  # Renombramos el archivo a mp3
    
    return send_file(mp3_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
