from crypt import methods
from flask import Flask, render_template, request, redirect
import geminiSrc

app = Flask(__name__)

# initialization of gemini
gemini = geminiSrc.Gemini()


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        task_content = request.form['ask']

        try:
            file = open('output.txt', 'w')
            output = gemini.generate(task_content)
            file.write(output)
            file.close()
            return redirect('/')
        except:
            return 'There was an issue connecting to Gemini.'

    else:
        # tasks = Todo.query.order_by(Todo.date_created).all()
        file = open('output.txt', 'r')
        file_output = file.read()
        return render_template('index.html', output=file_output)

if __name__ == '__main__':
    app.run(debug=True)
