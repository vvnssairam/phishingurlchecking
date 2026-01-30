from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

def is_phishing(url):
    # very basic rules
    if "@" in url:
        return True
    if len(url) > 75:
        return True
    if re.search(r"\d+\.\d+\.\d+\.\d+", url):  # IP address in URL
        return True
    return False

HTML = """
<!DOCTYPE html>
<html>
<head><title>Phishing Detector</title></head>
<body>
<h2>Phishing Website Detector</h2>
<form method="post">
  Enter URL: <input type="text" name="url" size="50">
  <input type="submit" value="Check">
</form>
{% if result %}
<h3>{{result}}</h3>
{% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        url = request.form["url"]
        if is_phishing(url):
            result = "⚠️ This looks like a Phishing URL"
        else:
            result = "✅ This looks Safe"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)