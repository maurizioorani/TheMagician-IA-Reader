# ✨ The Magician IA Reader: AI-Powered Italian NLP & Tarot Insights ✨

Welcome to **The Magician IA Reader**! This project presents a unique application combining the power of Artificial Intelligence with the mystique of tarot reading, specifically tailored for **Italian natural language**.

**What it Does:**

This application functions as an AI-driven tarot reader. It takes natural language input (primarily Italian) and, using an AI model guided by traditional tarot card meanings, provides interpretative insights.

**Key Features:**

* **Italian Natural Language Support:** Understands and interacts in fluent Italian.
* **Local AI Model ('phi4'):** Runs on the efficient 'phi4' model, ideal for local processing and privacy.
* **CSV-driven Knowledge Base:** Utilizes structured CSV files to store and reference detailed tarot card meanings.
* **Deep Insights:** Transforms raw text queries into meaningful, context-aware interpretations based on tarot symbolism.

**How it Works:**

The core of The Magician IA Reader lies in its use of the 'phi4' local AI model. This model is fine-tuned or prompted using comprehensive data from CSV files, which contain the interpretations for each tarot card. When a user provides text input in Italian, the application processes it through the AI, which then generates a response informed by the tarot meanings.

**Why Use It?**

* **Researchers & Developers:** Explore the capabilities of local AI models for natural language understanding and generation in Italian.
* **AI Enthusiasts:** Experiment with a practical application of AI in a unique domain.
* **Curious Minds:** Experience an innovative way to interact with AI for personal insights.

Step into the world where AI meets intuition with The Magician IA Reader!

---

## ⚙️ Installation

### Prerequisites

- **Python 3.8 or higher**
- **pip** – Python package installer

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/maurizioorani/TheMagician-IA-Reader.git
   cd TheMagician-IA-Reader
   ```

Set Up a Virtual Environment (Recommended)

```bash
# On Unix/macOS:
python -m venv venv
source venv/bin/activate


# On Windows:
python -m venv venv
venv\Scripts\activate
Install Dependencies
```

The repository is structured into two main directories:

Frontend (Streamlit):

```bash
cd frontend
pip install -r requirements.txt
Backend (Langchain):
```
```bash
cd ../backend
pip install -r requirements.txt
Configure Environment Variables
```
Run the Application

```bash
streamlit run app.py
```
The Streamlit interface will typically be available at http://localhost:8501.

## 📖 How to Use
Access the App: Open your browser and navigate to the URL provided by Streamlit (commonly http://localhost:8501).

Input Your Text Data: Use the intuitive interface to paste, type, or upload the text you want to analyze.

Configure Analysis Settings: Select from various options such as sentiment analysis, keyword extraction, or custom text interpretations. The interaction between the Streamlit frontend and the Langchain-powered backend dynamically processes your input.

Review the Insights: View detailed analytics and visualizations that reveal themes, sentiments, and other hidden patterns in your text.

Iterate and Customize: Experiment with different configurations to refine your analysis as per your project’s needs.

## 🤝 Contributing
Contributions are welcome! If you have improvements or new features to add, please:

Fork the repository.

Create a new branch for your changes.

Submit a pull request with a clear description of your modifications.

For major changes, please discuss them via an issue before implementation.
