
from flask import Flask
from address_parser.routes.medium_parser import medium_parser_bp
from address_parser.routes.simple_address import simple_parser_bp
from address_parser.routes.complex_parser import complex_parser_bp

app = Flask(__name__)

app.register_blueprint(simple_parser_bp)
app.register_blueprint(medium_parser_bp)
app.register_blueprint(complex_parser_bp)


if __name__ == '__main__':
    app.run(debug=True)
