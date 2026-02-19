from flask import Flask, render_template, send_file, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download-cv')
def download_cv():
    # Path to your actual CV file
    path = "static/docs/Kevin_Nyambega_CV.pdf"
    return send_file(path, as_attachment=True)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    # Logic to send email or save to database
    return f"Thank you {name}, your inquiry has been received.", 200

if __name__ == '__main__':
    app.run(debug=True)
