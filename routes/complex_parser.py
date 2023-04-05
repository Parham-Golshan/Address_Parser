from flask import Blueprint, request, jsonify
import re

# Defining a Blueprint for complex address parsing
complex_parser_bp = Blueprint('parser-complex', __name__)


# Defining an error handler for when the input address is not in the expected format
@complex_parser_bp.errorhandler(ValueError)
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


# Defining a route to handle requests to parse a complex address (Case #3)
@complex_parser_bp.route('/parser-complex/', methods=['POST'])
def complex_parser():
    """
        Parses a complex address and returns the street name and house number as JSON.

        The function accepts a POST request with a JSON payload containing an 'input_address' field
        or a form-encoded request with an 'input_address' field.

        Generally, The input address should have the format '<house number> <street name>' or
        '<street name> <prefix> <house number>'.
        The function uses a regular expression to extract the house number and street names from the input address.
        If the input address is not in the expected format, the function raises a ValueError.

        Returns:
            A JSON object with 'street' and 'housenumber' fields.
        """
    if request.is_json:
        input_address = request.get_json().get('input_address')
    else:
        input_address = request.form['input_address']
    pattern = re.compile(r'(?P<number>^\d+,*|(?:\bNo|#)*\s*\d+\s?.?$)')
    match = re.search(pattern=pattern, string=input_address)
    if not match:
        raise ValueError('The address_input is not in expected formats')
    house_number = match.group('number').strip().strip(',')
    street = re.sub(pattern, '', input_address).strip().strip(',')

    return jsonify(street=street, housenumber=house_number)
