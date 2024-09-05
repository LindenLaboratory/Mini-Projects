'''
This is a small project I made to host a web server on my computer that allows people on my local network to send me urgent messages
'''

#IMPORTS
from flask import Flask,request
import webbrowser

#SETUP
app = Flask(__name__)
message = ""

#FUNCTIONS
    #NOTIFY
def popup(string):
    global message
    message = string
    webbrowser.open('http://127.0.0.1/message')
    #FLASK
@app.route("/",methods=["GET"])
def index():
    return """/
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NotifIsaac</title>
    <link href="https://fonts.googleapis.com/css2?family=Maven+Pro:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
            font-family: 'Maven Pro', sans-serif;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            box-sizing: border-box;
        }

        .container {
            width: 100%;
            max-width: 400px;
            padding: 20px;
            background-color: #1e1e1e;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        textarea {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            background-color: #333333;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            resize: none;
            height: 100px;
        }

        button {
            width: 100%;
            padding: 10px;
            font-size: 18px;
            margin-top: 15px;
            background-color: #6200ea;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #3700b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <form id="messageForm">
            <textarea id="message" placeholder="Type your message here..."></textarea>
            <button type="submit">Send</button>
        </form>
    </div>

    <script>
        document.getElementById('messageForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            const message = document.getElementById('message').value.trim();

            if (message === "") {
                alert("Please enter a message before sending.");
                return;
            }

            fetch('/send', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            })
            .then(response => {
                if (response.ok) {
                    alert("Message sent successfully!");
                    document.getElementById('message').value = ""; // Clear the textarea
                } else {
                    alert("Failed to send message.");
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert("An error occurred. Please try again.");
            });
        });
    </script>
</body>
</html>
"""

@app.route("/send",methods=["POST"])
def send():
    message = request.get_json()["message"]
    popup(message)
    return "Message Sent!"

@app.route("/message",methods=["GET"])
    return f"""/
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notification</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Maven+Pro:wght@700&display=swap');
        
        body {{
            background-color: red;
            color: white;
            font-family: 'Maven Pro', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            text-align: center;
        }}

        h1 {{
            font-size: 4rem;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1>{message}</h1>
</body>
</html>
"""
    
#MAINLOOP
app.run("0.0.0.0")
