import requests
import pandas as pd

# Define the CSV path and the URL for the HTTP POST
csv_file = '/workspaces/challenge_konfio/files/intent.csv'
url = 'https://jubilant-sniffle-q9767pq559wf676q-5000.app.github.dev/predict'

def test_predict_endpoint():
    # Load the CSV data
    data = pd.read_csv(csv_file)
    data = data.loc[:10]

    # Test the endpoint for each row in the CSV
    for _, row in data.iterrows():
        motivos = row['motivos']
        payload = {"motivos": motivos}
        
        # Send POST request
        response = requests.post(url, json=payload)

        # Print input and response
        print('Input:', motivos)
        print('Response:', response.json())

if __name__ == "__main__":
    test_predict_endpoint()