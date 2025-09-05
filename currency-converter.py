from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

def convert_currency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:4])

    return rate

# print(convert_currency('USD', 'INR'))

app = Flask(__name__)

app.route('/')
def home():
    return "<h1>Currency Rate API<h1><p>Use the endpoint /api/v1/<in_currency>/<out_currency> to get the conversion rate.</p>"

@app.route('/api/v1/<in_currency>/<out_currency>', methods=['GET'])
def api_currency(in_currency, out_currency):
    rate = convert_currency(in_currency, out_currency)
    return jsonify({
        'in_currency': in_currency,
        'out_currency': out_currency,
        'rate': rate
    })

app.run(host='0.0.0.0') 