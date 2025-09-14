from flask import Flask, render_template, request

app = Flask(__name__)

# Home route (example)
@app.route("/")
def home():
    return "<h1>Welcome to Bibek College of Kathmandu</h1>"

# Contact page route
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # For now just print to console
        print(f"New Message: {name}, {email}, {message}")

        return "✅ Message received! We will contact you soon."

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
