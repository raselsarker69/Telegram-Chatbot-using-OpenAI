# 🤖 Telegram Chatbot using OpenAI (GPT-3.5 / GPT-4)

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A smart and fast **Telegram Chatbot** built with [Aiogram](https://docs.aiogram.dev/en/latest/) and [OpenAI API](https://platform.openai.com/docs/). This chatbot can chat intelligently using **GPT-3.5 / GPT-4**, and can be easily extended with custom features like function calling, weather updates, etc.

---

## 📸 Demo

![Demo](https://user-images.githubusercontent.com/raselsarker69/demo-image.gif)


---


## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/telegram-openai-chatbot.git
cd telegram-openai-chatbot
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv telebot
telebot\Scripts\activate   # For Windows
# OR
source telebot/bin/activate  # For macOS/Linux
```


## 3. Setup Environment Variables
```bash
BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
```

## 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ✨ Features

- 🧠 Chat with OpenAI GPT-3.5 or GPT-4
- ⚡ Async performance using Aiogram
- 🔐 Secure API keys using `.env`
- 🧩 Easily extendable with custom commands
- 🌐 Supports future integration like webhooks, function calls

---

## 🔧 Technologies Used
- Aiogram – Fast async Telegram bot framework
- OpenAI API – GPT-3.5 / GPT-4 conversational AI
- Python – Language of choice
- dotenv – Manage secrets securely

---

## 📂 Project Structure
```python
src/
├── __init__.py
├── helper.py
├── prompt.py
notebooks/
├── telebot-notebook.ipynb
.env
setup.py
app.py
test.py
requirements.txt

```
---

## 🤝 Contributing
- Contributions are welcome!
- Fork the project
- Create your feature branch (git checkout -b feature/xyz)
- Commit your changes (git commit -m 'Add xyz feature')
- Push to the branch (git push origin feature/xyz)
- Open a Pull Request