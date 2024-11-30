from flask import Flask, request, jsonify
from deployment.scripts.utils import clean_text, process_result

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the LLM Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    
    data = request.get_json(force=True)
    user_input = data.get('motivos', '')

    # Clean the Prompt
    prompt_cleaned = clean_text(user_input)

    # Call the LLM-Model the input text, we pass the fine tuned model.
    predictions = process_result(model="ft:gpt-3.5-turbo-0125:suprabound::AZ9ij1gt", prompt_cleaned = prompt_cleaned)

    return jsonify({'predictions': predictions})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)