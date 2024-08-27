
from flask import Flask
from configuration import configure_all

app = Flask(__name__)




app.secret_key = b'\xf1\x88\xa1\xd3\xa4\xb4\x92\x1c\x1b\x8e\xfe\xe3\xd1\xd8\xab\xfe\xad\x87\x11'

configure_all(app)

if __name__ == '__main__':
    app.run(debug=True)
