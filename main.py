from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html', username = 'Zackary')

@app.route('/after_extend')
def about():
    return render_template('after_extend.html', username = 'Zackary')

if __name__ == '__main__':
    app.run(debug=True)