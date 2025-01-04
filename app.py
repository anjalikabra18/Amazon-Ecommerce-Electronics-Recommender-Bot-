from flask import Flask, render_template, request, jsonify
from multimodal import img2txt, transcribe, text_to_speech
from ecommbot.ingest import ingestdata
from ecommbot.retrieval import generation
import os

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')

# Load vector store and generate response chain
try:
    vstore = ingestdata("done")
    response_chain = generation(vstore)
except Exception as e:
    print(f"Error initializing vector store or response chain: {e}")
    vstore = None
    response_chain = None

# Route to render the main chat interface
@app.route("/")
def index():
    return render_template("chat.html")

# Route to handle user queries
@app.route("/ask", methods=["POST"])
def ask():
    try:
        text = request.json.get("text")
        audio = request.files.get("audio")

        # Handle text input
        if text:
            if response_chain and vstore:
                response_text = response_chain.invoke(text)
            else:
                response_text = "The response system is currently unavailable."
            return jsonify({"question": text, "response": response_text})

        # Handle audio input
        if audio:
            # Save the uploaded audio file
            temp_audio_path = os.path.join("static", "audio", "recording.wav")
            audio.save(temp_audio_path)

            # Transcribe the audio to text
            question = transcribe(temp_audio_path)
            if not question.strip():
                return jsonify({"error": "Sorry, I could not understand your audio input."})

            # Generate a response based on the transcribed text
            if response_chain and vstore:
                response_text = response_chain.invoke(question)
            else:
                response_text = "The response system is currently unavailable."

            # Generate audio response from text
            audio_filename = "response.mp3"
            audio_response_path = text_to_speech(response_text, audio_filename)

            return jsonify({
                "question": question,
                "response": response_text,
                "audio_response": f"static/audio/{audio_filename}"
            })

        # If no input is provided
        return jsonify({"error": "No input provided. Please type a question or record audio."})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the app
if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
