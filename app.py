from flask import Flask, render_template, request, redirect, url_for

# For the CodeCollab, you can discuss anything in this Python script OR the HTML template!

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
  staff_member_data = [{
      'name': 'Nicki Minaj',
      'role': 'Head of School'
  }, {
      'name': 'Bad Bunny',
      'role': 'Assistant Head of School'
  }, {
      'name': 'Olivia Rodrigo',
      'role': 'Senior Class President'
  }]
  return render_template('index.html', staff_members=staff_member_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
