from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_message = request.form['message']
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message}
                ]
            )
            ai_message = response['choices'][0]['message']['content']
        except Exception as e:
            ai_message = "Sorry, there was an error: " + str(e)

        return render_template('index.html', user_message=user_message, ai_message=ai_message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
