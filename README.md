# challenge_konfio
Challenge Konfio creado por Kevin Murgana para la posición de Data Scientist Specialist.

# LLM Prediction Application

This project is a Flask application that uses a fine-tuned GPT-3.5 Turbo model for multi-label predictions based on user input.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd project
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key in `app.py`.

4. Run the application:
   ```bash
   python app.py
   ```

## Usage
Send a POST request to `/predict` with JSON data:
```json
{
  "motivos": "Your input text here"
}