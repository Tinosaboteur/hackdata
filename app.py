from flask import Flask, request, render_template, send_file
import csv
import os

app = Flask(__name__)

# Tạo file CSV nếu chưa có
DATA_FILE = "user_data.csv"
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Tên", "Email", "Nội dung"])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        content = request.form.get("content")

        # Ghi vào CSV
        with open(DATA_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([name, email, content])

    return render_template("index.html")

@app.route("/download")
def download():
    return send_file(DATA_FILE, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Cổng phải mở khi deploy
