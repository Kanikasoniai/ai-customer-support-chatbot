from database import init_db, save_lead
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
init_db()
@app.route('/')
def home():
    return render_template("index.html")

user_data = {"step": "start"}

@app.route('/get', methods=['POST'])
def chatbot():
    global user_data

    data = request.get_json()
    user_message = data.get("message") if data else ""

    msg = user_message.lower() if user_message else ""

    # STEP 0: Greeting
    if user_data["step"] == "start":
        user_data["step"] = "ask_name"
        return jsonify({"reply": "Hello! 👋 Welcome to VKAIS.\nWhat's your name?"})

    # STEP 1: Get Name
    elif user_data["step"] == "ask_name":
        user_data["name"] = user_message
        user_data["step"] = "ask_email"
        return jsonify({"reply": f"Nice to meet you, {user_message}! 😊\nPlease share your email."})

    # STEP 2: Get Email
    elif user_data["step"] == "ask_email":
        user_data["email"] = user_message

        # Save to database
        save_lead(user_data["name"], user_data["email"])

        user_data = {"step": "start"}  # reset

        return jsonify({"reply": "Thank you! 🎉 Our team will contact you soon."})

    # Fallback (just in case)
    return jsonify({"reply": "How can I help you?"})



if __name__ == "__main__":
    app.run(debug=True)



