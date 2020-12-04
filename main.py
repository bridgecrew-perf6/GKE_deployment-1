from flask import Flask, render_template, request

app = Flask(__name__,static_folder="/templates/static")

@app.route("/")
def main():
    model = {"title": "Simple Web App Built and Hosted on GCP"}
    return render_template('index.html', model=model)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
