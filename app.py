from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Налаштування пошти (для Gmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'reparaciones.rubi@gmail.com'
app.config['MAIL_PASSWORD'] = 'viul mtkp ghlj cgee'  # не звичайний пароль, а "App Password"

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message(f"Повідомлення з сайту від {name}",
                  sender=email,
                  recipients=['reparaciones.rubi@gmail.com'])  # твій email
    msg.body = f"Ім'я: {name}\nEmail: {email}\n\n{message}"

    try:
        mail.send(msg)
        flash("Повідомлення надіслано успішно!", "success")
    except Exception as e:
        print(str(e))
        flash("Виникла помилка при надсиланні.", "error")

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
