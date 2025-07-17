from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/colour-picker')
def colourPicker():
   return render_template('colour-picker.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


