from flask import Flask, render_template, request

app = Flask(__name__)

scam_keywords = [
    "otp", "urgent", "bank", "verify", "account", "suspended", 
    "click here", "limited time", "update your info", "password", 
    "unauthorized", "refund", "lottery", "win", "urgent action",
    "free gift", "KYC", "blocked", "PAN card", "Aadhaar"
]

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        message = request.form["message"].lower()  # Make case-insensitive
        if any(keyword in message for keyword in scam_keywords):
            result = "🚨 Suspicious message! Possible scam."
        else:
            result = "✅ Safe message."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
