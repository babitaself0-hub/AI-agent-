from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>My AI</title>
<style>
body {
    margin:0;
    font-family: Arial;
    display:flex;
    flex-direction:column;
    height:100vh;
}
#welcome {
    flex:1;
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:30px;
    color:gray;
}
#chat {
    flex:1;
    overflow:auto;
    padding:10px;
}
#inputArea {
    display:flex;
    border-top:1px solid #ccc;
}
input {
    flex:1;
    padding:10px;
}
button {
    padding:10px;
}
</style>
</head>

<body>

<div id="welcome">Hello User 👋</div>

<div id="chat"></div>

<div id="inputArea">
    <input id="msg" placeholder="Ask anything...">
    <button onclick="send()">Send</button>
</div>

<script>
async function send() {
    let input = document.getElementById("msg");
    let message = input.value;

    if(message === "") return;

    document.getElementById("welcome").style.display = "none";

    let chat = document.getElementById("chat");
    chat.innerHTML += "<p><b>You:</b> " + message + "</p>";

    let res = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({message: message})
    });

    let data = await res.json();

    chat.innerHTML += "<p><b>AI:</b> " + data.reply + "</p>";

    input.value = "";
    chat.scrollTop = chat.scrollHeight;
}
</script>

</body>
</html>
"""

@app.route("/chat", methods=["POST"])
def chat():
    user = request.json["message"]

    # simple AI (you can replace with real AI later)
    reply = "You said: " + user

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()
