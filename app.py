from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/offers', methods=['GET', 'POST'] )
def result():       
    return render_template('offers.xhtml')    

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html')    

if __name__ == "__main__":
    app.run()