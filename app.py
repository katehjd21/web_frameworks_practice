from flask import Flask, render_template
app = Flask(__name__, static_url_path="/flask-app/static")

@app.route('/')
def home():
   return render_template('index.html')
# if __name__ == '__main__':
#    app.run(debug=True)

@app.route('/colour-picker')
def colourPicker():
   return render_template('colour-picker.html')
# if __name__ == '__main__':
#    app.run(debug=True)

