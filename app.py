from flask import Flask, render_template
import geminiSrc

app = Flask(__name__)

# initialization of gemini
gemini = geminiSrc.Gemini()


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/<in_put>')
def hello_world(in_put):  # put application's code here
    output = gemini.generate(in_put)
    return output
    # return render_template('index.html', output=output)


if __name__ == '__main__':
    app.run(debug=True)
