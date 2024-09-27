from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder=os.getcwd())

# Ruta para servir el archivo CSS desde la misma carpeta
@app.route('/diseño.css')
def serve_css():
    return send_from_directory(os.getcwd(), 'diseño.css')

# Ruta para servir las imágenes
@app.route('/imagenes/<path:filename>')
def serve_images(filename):
    return send_from_directory(os.path.join(os.getcwd(), 'imagenes'), filename)

@app.route('/codigo/videos/video.html')
def serve_js():
    return send_from_directory(os.getcwd(), 'video.html')

@app.route('/scripts.js')
def serve_js():
    return send_from_directory(os.getcwd(), 'scripts.js')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
