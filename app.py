from flask import Flask, render_template, request, redirect, session
import geminiSrc

app = Flask(__name__)
app.secret_key = "433e732fe46eb93bed8f0392"
app.permanent_session_lifetime = 360


# initialization of gemini
gemini = geminiSrc.Gemini()


@app.route('/', methods=['GET', 'POST'])
def main():
    session.permanent = True
    session_data = session.get('output_dict', {})
    if request.method == 'POST':
        task_content = request.form['ask']

        try:
            output = gemini.generate(task_content)
            session_data[task_content] = output
            session['output_dict'] = session_data
            return redirect('/')
        except:
            return 'There was an issue connecting to Gemini.'

    else:
        # tasks = Todo.query.order_by(Todo.date_created).all()
        try :
            session_data = session.get('output_dict', {})
            print(session_data)
            return render_template('index.html', output=session_data)
        except:
            return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
