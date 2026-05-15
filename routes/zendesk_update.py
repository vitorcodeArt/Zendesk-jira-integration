from flask import Flask

app = Flask(__name__)

@app.route('/zendesk_to_jira/', methods=['PUT'])
def update_issue():
     print("Hello")
     return "Hi"

if __name__ == '__main__':
    app.run(debug=True)