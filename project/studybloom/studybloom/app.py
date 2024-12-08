from flask import Flask, request, jsonify
import sympy as sp

app = Flask(__name__)

# Route to handle the chat messages
@app.route('/chat', methods=['GET'])
def chat():
    # Get the user's message from the query string
    user_message = request.args.get('message', '')

    if user_message.strip() == "":
        return jsonify({"response": "Please enter a polynomial to find its roots."})

    # Process the user's message to create a polynomial
    try:
        # Here, we are assuming the user is providing a polynomial like "x**2 - 5*x + 6"
        x = sp.symbols('x')
        polynomial = sp.sympify(user_message)  # Convert the string input into a sympy expression
        roots = sp.solve(polynomial, x)  # Find the roots of the polynomial

        # Convert the roots to a list of strings (to send them in JSON)
        roots_list = [str(root) for root in roots]

        response_message = f"The roots of the polynomial are: {', '.join(roots_list)}"
    except Exception as e:
        response_message = f"Error: {str(e)}"

    # Return the response as JSON
    return jsonify({"response": response_message})

if __name__ == '__main__':
    app.run(debug=True)
