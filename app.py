from flask import Flask,render_template
app= Flask(__name__)
@app.route('/')
def house():
    words=["cat","cddog"]
    return render_template('index_html', words=words)
