# ✍️ AI Writer Suite

**AI Writer Suite** is an intelligent content generator built using **LangChain**, **FastAPI**, **Streamlit**, and powerful LLMs like **Gemini (Google)** and **LLaMA 3.2 (Ollama)**. This app allows users to generate high-quality essays and child-friendly poems based on any topic with ease.

<img width="1029" alt="Image" src="https://github.com/user-attachments/assets/05b4bc73-4a3a-4883-b421-7ee00f864111" />
<img width="1029" alt="Image" src="https://github.com/user-attachments/assets/3ecc6020-a932-4afa-abef-1e896ca19ee2" />
---

## 🚀 Features

- ✏️ Generate 100-word essays using **Gemini Flash 1.5**
- 📜 Create poems for 5-year-old children using **LLaMA 3.2**
- ⚙️ Interactive frontend built with **Streamlit**
- 🔁 FastAPI backend with LangChain integration
- 🧩 Modular design — easy to scale or plug in new models
- 🔓 100% open-source and beginner-friendly

---

## 🧰 Tech Stack

| Tool        | Purpose                              |
|-------------|---------------------------------------|
| **LangChain** | Prompt templating & chaining        |
| **FastAPI**  | Backend API Server                   |
| **Streamlit**| Frontend UI                          |
| **Gemini Flash 1.5** | Essay generation (via Google API) |
| **LLaMA 3.2 via Ollama** | Poem generation          |
| **Uvicorn**  | ASGI server to run FastAPI app       |
| **Python**   | Main programming language             |

---

## 🖥️ Project Structure

```
AI-Writer-Suite/
├── app.py              # FastAPI backend
├── client.py           # Streamlit frontend
├── .env                # API keys (not tracked in GitHub)
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
└── ...
```

---

## ⚙️ How It Works

### Essay Generation (Gemini):
- The app sends a topic to FastAPI → LangChain formats it using a prompt → Gemini Flash 1.5 generates a 100-word essay.

### Poem Generation (LLaMA 3.2):
- The app sends a topic → LangChain formats a poem prompt → Ollama (LLaMA 3.2) generates a child-friendly poem.

---

## 📦 Setup & Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/RNNivash/AI-Writer-Suite.git
cd AI-Writer-Suite
```

### 2. Set up `.env` file
```
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start Ollama server
```bash
ollama run llama3
```

### 5. Run FastAPI backend
```bash
python app.py
```

### 6. Run Streamlit frontend
```bash
streamlit run client.py
```

---

## 🙋‍♂️ Author

Made with ❤️ by **Nivash R N**  
🔗 [LinkedIn](https://www.linkedin.com/in/nivash-r-n/)  
📧 hello.nivashinsights@gmail.com

---

## 📜 License

© 2025 Nivash R N. All rights reserved.  
Feel free to fork, star, and contribute ⭐
