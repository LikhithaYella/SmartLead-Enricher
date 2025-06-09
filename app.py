
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_leads', methods=['POST'])
def get_leads():
    company = request.form.get('company')
    leads = {
        "company": company,
        "domain": f"{company.lower().replace(' ', '')}.com",
        "email": f"contact@{company.lower().replace(' ', '')}.com",
        "linkedin": f"https://linkedin.com/company/{company.lower().replace(' ', '')}"
    }
    return jsonify(leads)

if __name__ == '__main__':
    app.run(debug=True)
