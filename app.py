from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dtr')
def dtr():
    return redirect('http://172.16.255.220:5001/')  # Redirect to DTR System

@app.route('/logs')
def logs():
    return redirect('http://172.16.255.220:5003/')  # Redirect to Logging System

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=80)
    # app.run(host='0.0.0.0', port=80, debug=True)
