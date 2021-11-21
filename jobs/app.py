from flask import Flask, render_template
from flask.helpers import url_for

app = Flask('__name__', template_folder='jobs/templates')

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
