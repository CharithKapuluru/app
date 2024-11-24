from flask import Flask, request, render_template_string

app = Flask(__name__)

# Simple example to take user input and display it
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the input from the form
        user_input = request.form.get('user_input', '')
        # Render the input directly in the response
        return render_template_string(f"""
            <h1>Your Input:</h1>
            <p>{user_input}</p>
            <a href="/">Go Back</a>
        """)
    # Render a form for user input
    return '''
        <form method="POST">
            <label for="user_input">Enter something:</label>
            <input type="text" id="user_input" name="user_input" />
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
