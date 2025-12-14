# 📊 WhatsApp Chat Analyzer (Streamlit + Python)

A **Streamlit-based web application** that analyzes exported **WhatsApp chat files** and provides detailed insights into chat activity, user behavior, message trends, emojis, and word usage.

This project demonstrates **real-world text processing**, **data analysis**, and **interactive visualization** using Python.

---

## 🚀 Features

* 📁 Upload WhatsApp chat `.txt` file directly via UI
* 👥 User-wise and overall chat analysis
* 💬 Total messages, words, and shared links
* 📆 Monthly & daily activity timelines
* 📊 Most active days & months
* 🔥 Weekly activity heatmap
* 👤 Most active users in group chats
* ☁️ Word cloud generation
* 📝 Most common words analysis
* 😀 Emoji usage & frequency analysis

---

## 🛠️ Tech Stack

* **Language:** Python 🐍
* **Framework:** Streamlit 🌐
* **Libraries Used:**

  * pandas
  * matplotlib
  * seaborn
  * wordcloud
  * emoji
  * urlextract
  * re (regex)

---

## 📂 Project Structure

```
whatsapp-chat-analysis/
│
├── app.py                # Streamlit application
├── helper.py             # Analysis & visualization helpers
├── preprocessor.py       # Chat parsing & preprocessing
├── stop_hinglish.txt     # Custom Hinglish stopwords
├── requirements.txt      # Dependencies
├── .gitignore            # Ignored files
└── .venv/                # Virtual environment (ignored)
```

---

## 📋 Requirements

* **Python 3.8+**
* pip

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/whatsapp-chat-analysis.git
cd whatsapp-chat-analysis
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the App

```bash
streamlit run app.py
```

The application will open in your browser 🌐.

---

## 📥 How to Export WhatsApp Chat

1. Open WhatsApp
2. Select a chat → More → Export chat
3. Choose **Without media**
4. Upload the `.txt` file into the app

---

## 🧠 Key Learning Outcomes

* Parsing unstructured real-world text data
* Regex-based chat preprocessing
* User-level & temporal data analysis
* Interactive dashboards using Streamlit
* Clean project structure & Git practices

---

## 🔮 Future Enhancements

* 📊 Advanced visualizations
* 🌍 Deployment on Streamlit Cloud
* 📱 Support for multiple WhatsApp formats
* 🧠 NLP-based sentiment analysis

---

## 🤝 Contributing

Contributions are welcome!
Fork the repo and submit a pull request 🚀.

---

## 📜 License

This project is open-source under the **MIT License**.


