import dash
from dash import html, dcc, Input, Output
import requests

app = dash.Dash(__name__)

# Layout for the dashboard
app.layout = html.Div([
    html.H1("NER Model Dashboard"),
    html.Div([
        dcc.Textarea(
            id='input-text',
            placeholder="Enter text here...",
            style={'width': '100%', 'height': '100px'}
        ),
        html.Button("Predict", id='predict-button', n_clicks=0),
        html.Div(id='prediction-output', style={'marginTop': 20}),
    ]),
])

# Callback to handle predictions
@app.callback(
    Output('prediction-output', 'children'),
    [Input('predict-button', 'n_clicks')],
    [Input('input-text', 'value')]
)
def update_prediction(n_clicks, text):
    if n_clicks > 0 and text:
        response = requests.post("http://127.0.0.1:8000/predict", json={"text": text})
        if response.status_code == 200:
            predictions = response.json()['entities']
            return html.Ul([html.Li(f"{ent['text']} ({ent['label']})") for ent in predictions])
        else:
            return f"Error: {response.status_code}"
    return "No input provided yet."

if __name__ == "__main__":
    app.run_server(debug=True)
