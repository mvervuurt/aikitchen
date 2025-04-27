from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for financial data
financial_data = [{'amount': 100, 'description': 'Salary'}, {'amount': -50, 'description': 'Dinner'}]

@app.route('/add_record', methods=['POST'])
def add_record():
    data = request.get_json()
    if not data or 'amount' not in data or 'description' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    financial_data.append(data)
    return jsonify({'message': 'Record added successfully'}), 201

@app.route('/get_record/<int:record_id>', methods=['GET'])
def get_record(record_id):
    if record_id < 0 or record_id >= len(financial_data):
        return jsonify({'error': 'Record not found'}), 404
    return jsonify(financial_data[record_id]), 200

@app.route('/list_records', methods=['GET'])
def list_records():
    return jsonify(financial_data), 200

if __name__ == '__main__':
    app.run(debug=True)