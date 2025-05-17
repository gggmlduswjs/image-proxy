from flask import Flask, request, send_file
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/image')
def proxy_image():
    url = request.args.get('url')
    if not url:
        return "URL parameter is required", 400

    try:
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://www.kyobobook.co.kr/"
        }
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return send_file(BytesIO(response.content), mimetype='image/jpeg')
    except Exception as e:
        return f"Error fetching image: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
