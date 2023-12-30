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
            output = gemini.generate(task_content)
            return redirect('/')
        except:
            return 'There was an issue connecting to Gemini.'

    else:
        # tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', )

if __name__ == '__main__':
    app.run(debug=True)
