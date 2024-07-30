from groq import Groq
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    ask = request.args.get('ask')
    if ask:
        client = Groq()
        completion = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {
                    "role": "user",
                    "content": ask
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        response = ""
        for chunk in completion:
            response += chunk.choices[0].delta.content or ""

        return jsonify({"response": response})
    else:
        return "Veuillez fournir une question dans le paramètre 'ask'. Exemple : /?ask=VotreQuestion"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
