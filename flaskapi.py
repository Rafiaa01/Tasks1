from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])

def sentiment_analysis():
    
    if not request.is_json:
        return jsonify({
            "error": "Invalid input. Please provide JSON data."
        }), 400
        
    data = request.get_json()
    
    if 'text' not in data:
        return jsonify({
            "error": "Missing 'text' field in the request data."
        }), 400
    
    if not isinstance(data['text'], str):
        return jsonify({
            "error": "'text' field must be a string."
        }), 400
    
    if len(data['text'].strip()) == 0:
        return jsonify({
            "error": "'text' field cannot be empty."
        }), 400
    
    text=data["text"].lower()
    
    if "love" in text:
        sentiment = "positive"
    elif "hate" in text:
        sentiment = "negative"  
    else:
        sentiment = "missing"
       
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True) 