from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                            book_name = [1,2]
                            )

if __name__ == "__main__":
    app.run(debug=True)