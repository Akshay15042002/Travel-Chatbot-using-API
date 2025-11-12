from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Set up your OpenAI API key. Replace 'YOUR_API_KEY' with your actual API key.
openai.api_key = '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'

# Define a function to get travel recommendations from GPT-3.
def get_travel_recommendation(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=500  # Adjust based on your needs.
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    user_input = request.json.get("user_input")
    
    if user_input.lower() == "exit":
        return jsonify({"message": "Goodbye!"})

    # Construct a prompt to send to OpenAI GPT-3.
    prompt = f"You: {user_input}\nChatbot:"

    if "find flight details" in user_input.lower():
        # You would typically fetch flight details here from a flight API.
        # Example: Call your flight API and get flight details.
        # flight_details = fetch_flight_details(user_input)

        # For the sake of this example, let's assume you fetched flight details as a string.
        flight_details = "Flight details for XYZ Airlines: Departure: 08:00 AM, Arrival: 10:00 AM, Price: $300"

        return jsonify({"message": flight_details})
    else:
        # Get a travel recommendation from GPT-3 based on user input.
        recommendation = get_travel_recommendation(prompt)
        return jsonify({"message": recommendation})

if __name__ == "__main__":
    app.run(debug=True)
