from flask import Blueprint, request, jsonify

# Defining a Blueprint for simple address parsing
simple_parser_bp = Blueprint('parser-simple', __name__)


# Defining an error handler for when the input address is not in the expected format
@simple_parser_bp.errorhandler(ValueError)
def handle_value_error(error):
    """
    Handles ValueError raised by the simple parser.

    Returns a JSON error response with a message describing the error.
    """
    response = {
        'error': 'Incorrect format',
        'message': str(error)
    }
    return jsonify(response), 500


# Defining a route to handle requests to parse a simple address (Case #1)
@simple_parser_bp.route('/parser-simple/', methods=['POST'])
def simple_parser():
    """
    Parses a simple address input string into its street and housenumber components.

        The function accepts a POST request with a JSON payload containing an 'input_address' field
        or a form-encoded request with an 'input_address' field.

    Returns:
        A JSON object with 'street' and 'housenumber' fields.
    """
    if request.is_json:
        input_address = request.get_json().get('input_address')
    else:
        input_address = request.form['input_address']
    input_list = input_address.split()
    if len(input_list) != 2:
        raise ValueError("The input is not in correct format or simple. You can use /parser-complex endpoint.")
    return jsonify({"street": input_list[0], "housenumber": input_list[1]})
