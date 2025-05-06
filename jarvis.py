# import gradio as gr
# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import requests
# from transformers import AutoTokenizer, AutoModelForCausalLM
# import torch
# import threading
# import json
# import os

# # === Initialization ===
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# # DialoGPT Model
# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# # News API key
# NEWS_API_KEY = "2235209fb3d3415f8a409cd41efb43c3"

# # Music library (keywords to links)
# MUSIC_LIBRARY = {
#     "life": "https://www.youtube.com/watch?v=LHCob76kigA",
#     "success" : "https://www.youtube.com/results?search_query=hall+of+fame",
#     "love" : "https://www.youtube.com/watch?v=tt2k8PGm-TI",
# }

# # === Core Functions ===
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def get_news_headlines():
#     try:
#         response = requests.get(
#             "https://newsapi.org/v2/top-headlines",
#             params={"country": "us", "apiKey": NEWS_API_KEY}
#         )
#         articles = response.json().get("articles", [])[:3]
#         headlines = "\n".join([f"{i+1}. {a['title']}" for i, a in enumerate(articles)])
#         return "📰 Top News Headlines:\n" + headlines
#     except Exception as e:
#         return f"Error getting news: {str(e)}"

# def generate_response(message):
#     inputs = tokenizer.encode(message + tokenizer.eos_token, return_tensors="pt")
#     outputs = model.generate(inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id,
#                             do_sample=True, top_k=50, top_p=0.95, temperature=0.7)
#     response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
#     return response

# def handle_command(command, chat_history):
#     command = command.lower().strip()
    
#     if "open google" in command:
#         webbrowser.open("https://google.com")
#         response = "Opening Google..."
#     elif "open youtube" in command:
#         webbrowser.open("https://youtube.com")
#         response = "Opening YouTube..."
#     elif "open instagram" in command:
#         webbrowser.open("https://instagram.com")
#         response = "Opening Instagram..."
#     elif "open linkedin" in command:
#         webbrowser.open("https://linkedin.com")
#         response = "Opening LinkedIn..."
#     elif "open music" in command:
#         webbrowser.open("https://open.spotify.com")
#         response = "Opening spotify..."
#     elif "open github" in command:
#         webbrowser.open("https://github.com")
#         response = "opening github"
#     elif "open gmail" in command:
#         webbrowser.open("https://mail.google.com")
#         response = "opening gmail..."
#     elif "open telegram" in command:
#         response = "opening telegram..."
#         webbrowser.open("https://web.telegram.org/a")
#     elif "open chatgpt" in command:
#         response = "opening chatgpt..."
#         webbrowser.open("https://github.com")
#     elif "open mycourse" in command:
#         response = "opening mycourse..."
#         webbrowser.open("https://www.apnacollege.in/?msg=not-logged-in")
#     elif "news" in command:
#         response = get_news_headlines()
#     elif command.startswith("play"):
#         song = command.replace("play", "").strip()
#         link = MUSIC_LIBRARY.get(song)
#         if link:
#             webbrowser.open(link)
#             response = f"Playing {song} on YouTube."
#         else:
#             response = f"❌ Song '{song}' not found in library."
#     else:
#         response = generate_response(command)

#     # Speak in background
#     threading.Thread(target=speak, args=(response,)).start()
#     chat_history.append((command, response))
#     return "", chat_history

# def listen_and_respond(chat_history):
#     try:
#         with sr.Microphone() as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
#             text = recognizer.recognize_google(audio)
#             return handle_command(text, chat_history)
#     except sr.WaitTimeoutError:
#         return "", chat_history + [("System", "Listening timed out.")]
#     except sr.UnknownValueError:
#         return "", chat_history + [("System", "Could not understand. Try again.")]
#     except Exception as e:
#         return "", chat_history + [("System", f"Error: {e}")]

# # === Gradio Interface ===
# with gr.Blocks(title="Jarvis Auto Reply", theme=gr.themes.Soft()) as demo:
#     gr.Markdown("## 🤖 JARVIS Auto Reply Personal Voice Assistant")
#     chatbot = gr.Chatbot(label="Conversation")
#     with gr.Row():
#         msg = gr.Textbox(placeholder="Type your message here...", label="Your Message", lines=1)
#         send = gr.Button("Send")
#         voice = gr.Button("🎤 Voice Command")
#         clear = gr.Button("🧹 Clear")

#     # Event handlers
#     send.click(fn=handle_command, inputs=[msg, chatbot], outputs=[msg, chatbot])
#     msg.submit(fn=handle_command, inputs=[msg, chatbot], outputs=[msg, chatbot])
#     voice.click(fn=listen_and_respond, inputs=[chatbot], outputs=[msg, chatbot])
#     clear.click(lambda: [], outputs=chatbot)

# # === Launch App ===
# if __name__ == "__main__":
#     demo.launch(share=True)

# #http://127.0.0.1:7860

import gradio as gr
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import threading
import json
import os

# === Initialization ===
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# DialoGPT Model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# News API key
NEWS_API_KEY = "2235209fb3d3415f8a409cd41efb43c3"

# Music library (keywords to links)
MUSIC_LIBRARY = {
    "life": "https://www.youtube.com/watch?v=LHCob76kigA",
    "success": "https://www.youtube.com/results?search_query=hall+of+fame",
    "love": "https://www.youtube.com/watch?v=tt2k8PGm-TI",
}

# User data storage
USER_DATA_FILE = "users.json"
if not os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "w") as f:
        json.dump({}, f)

def load_users():
    with open(USER_DATA_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f)

# === Core Functions ===
def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_news_headlines():
    try:
        response = requests.get(
            "https://newsapi.org/v2/top-headlines",
            params={"country": "us", "apiKey": NEWS_API_KEY}
        )
        articles = response.json().get("articles", [])[:3]
        headlines = "\n".join([f"{i+1}. {a['title']}" for i, a in enumerate(articles)])
        return "📰 Top News Headlines:\n" + headlines
    except Exception as e:
        return f"Error getting news: {str(e)}"

def generate_response(message):
    inputs = tokenizer.encode(message + tokenizer.eos_token, return_tensors="pt")
    outputs = model.generate(inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id,
                            do_sample=True, top_k=50, top_p=0.95, temperature=0.7)
    response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    return response

def handle_command(command, chat_history):
    command = command.lower().strip()

    if "open google" in command:
        webbrowser.open("https://google.com")
        response = "Opening Google..."
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        response = "Opening YouTube..."
    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
        response = "Opening Instagram..."
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        response = "Opening LinkedIn..."
    elif "open music" in command:
        webbrowser.open("https://open.spotify.com")
        response = "Opening Spotify..."
    elif "open github" in command:
        webbrowser.open("https://github.com")
        response = "Opening GitHub..."
    elif "open gmail" in command:
        webbrowser.open("https://mail.google.com")
        response = "Opening Gmail..."
    elif "open telegram" in command:
        webbrowser.open("https://web.telegram.org/a")
        response = "Opening Telegram..."
    elif "open chatgpt" in command:
        webbrowser.open("https://chat.openai.com")
        response = "Opening ChatGPT..."
    elif "open mycourse" in command:
        webbrowser.open("https://www.apnacollege.in/?msg=not-logged-in")
        response = "Opening MyCourse..."
    elif "news" in command:
        response = get_news_headlines()
    elif command.startswith("play"):
        song = command.replace("play", "").strip()
        link = MUSIC_LIBRARY.get(song)
        if link:
            webbrowser.open(link)
            response = f"Playing {song} on YouTube."
        else:
            response = f"❌ Song '{song}' not found in library."
    else:
        response = generate_response(command)

    # Speak in background
    threading.Thread(target=speak, args=(response,)).start()
    chat_history.append((command, response))
    return "", chat_history

def listen_and_respond(chat_history):
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            text = recognizer.recognize_google(audio)
            return handle_command(text, chat_history)
    except sr.WaitTimeoutError:
        return "", chat_history + [("System", "Listening timed out.")]
    except sr.UnknownValueError:
        return "", chat_history + [("System", "Could not understand. Try again.")]
    except Exception as e:
        return "", chat_history + [("System", f"Error: {e}")]

# === Gradio Interface ===
with gr.Blocks(title="Jarvis AI", theme=gr.themes.Soft()) as demo:
    # Session state
    state = gr.State({"authenticated": False, "email": ""})

    def show_home():
        return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)

    def show_login():
        return gr.update(visible=False), gr.update(visible=True), gr.update(visible=False)

    def show_chat():
        return gr.update(visible=False), gr.update(visible=False), gr.update(visible=True)

    def register_user(email, state):
        users = load_users()
        if email in users:
            return "Email already registered. Please login.", state
        users[email] = {}
        save_users(users)
        state["authenticated"] = True
        state["email"] = email
        return f"Successfully registered with email: {email}", state

    def login_user(email, state):
        users = load_users()
        if email in users:
            state["authenticated"] = True
            state["email"] = email
            return f"Welcome back, {email}!", state
        else:
            return "Email not found. Please register.", state

    def logout_user(state):
        state["authenticated"] = False
        state["email"] = ""
        return state

    # Home Page
    with gr.Column(visible=True) as home_page:
        gr.Markdown("## Welcome to Jarvis AI")
        gr.Markdown("Please login or register to continue.")
        login_btn = gr.Button("Login")
        register_btn = gr.Button("Register")

    # Login Page
    with gr.Column(visible=False) as login_page:
        gr.Markdown("## Login")
        login_email = gr.Textbox(label="Email")
        login_submit = gr.Button("Submit")
        login_output = gr.Textbox(label="Status", interactive=False)
        back_to_home_from_login = gr.Button("Back")

    # Register Page
    with gr.Column(visible=False) as register_page:
        gr.Markdown("## Register")
        register_email = gr.Textbox(label="Email")
        register_submit = gr.Button("Submit")
        register_output = gr.Textbox(label="Status", interactive=False)
        back_to_home_from_register = gr.Button("Back")

    # Chat Page
    with gr.Column(visible=False) as chat_page:
        gr.Markdown("## 🤖 Jarvis AI Chat")
        chatbot = gr.Chatbot(label="Conversation")
        with gr.Row():
            msg = gr.Textbox(placeholder="Type your message here...", label="Your Message", lines=1)
            send = gr.Button("Send")
            voice = gr.Button("🎤 Voice Command")
            clear = gr.Button("🧹 Clear")
            logout = gr.Button("Logout")

    # Button Click Events
    login_btn.click(fn=show_login, outputs=[home_page, login_page, register_page])
    register_btn.click(fn=show_login, outputs=[home_page, register_page, login_page])
    back_to_home_from_login.click(fn=show_home, outputs=[home_page, login_page, register_page])
    back_to_home_from_register.click(fn=show_home, outputs=[home_page, register_page, login_page])

    login_submit.click(fn=login_user, inputs=[login_email, state], outputs=[login_output, state])
    register_submit.click(fn=register_user, inputs=[register_email, state], outputs=[register_output, state])

    # After successful login or registration, show chat page
    def check_authentication(state):
        if state["authenticated"]:
            return gr.update(visible=False), gr.update(visible=False), gr.update(visible=True)
        else:
            return gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)

    login_submit.click(fn=check_authentication, inputs=[state], outputs=[home_page, login_page, chat_page])
    register_submit.click(fn=check_authentication, inputs=[state], outputs=[home_page, register_page, chat_page])

    send.click(fn=handle_command, inputs=[msg, chatbot], outputs=[msg, chatbot])
    msg.submit(fn=handle_command, inputs=[msg, chatbot], outputs=[msg, chatbot])
    voice.click(fn=listen_and_respond, inputs=[chatbot], outputs=[msg, chatbot])
    clear.click(lambda: [], outputs=chatbot)
    logout.click(fn=logout_user, inputs=[state], outputs=[state])
    logout.click(fn=show_home, outputs=[home_page, login_page, chat_page])

demo.launch()

# # jarvis_ai.py



