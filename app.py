
from minor_project import *
from flask import Flask , render_template,request


app = Flask(__name__ , static_folder ='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start',methods=['GET','POST'])
def start():
    # driver()
    return render_template('index2.html')

@app.route('/output', methods=['GET','POST'])
def output():
    output_text = request.form['text1']
    output = "test output"
    readl = output_text.split('\r\n')
    print(readl)
    output = driver(readl)
    # print(output)
    for l in output:
        print(l)
    
    return render_template('output.html',output_text = output)

@app.route('/about')
def about():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True , port=8000)