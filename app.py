from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

openai.api_key = "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"  # Substitueix amb la clau real

@app.route('/assistents/investigador', methods=['POST'])
def investigador():
    try:
        data = request.json
        isin = data.get('isin')
        if not isin:
            return jsonify({"error": "ISIN no proporcionat"}), 400

        prompt = f"ISIN: {isin}. Proporciona dades com: nom del fons, distribució sectorial, distribució geogràfica, rendiment històric, etc."
        response = openai.Completion.create(
            engine="text-davinci-003",  # Canvia a "gpt-4" si tens accés
            prompt=prompt,
            max_tokens=200
        )
        return jsonify({"result": response.choices[0].text.strip()})

    except Exception as e:
        return jsonify({"error": f"Error al servidor: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)