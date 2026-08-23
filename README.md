# 🍳 AI Recipe Finder

A Flask web app that turns your leftover ingredients into creative recipes using Google's Gemini AI, with structured JSON output and a linked YouTube search for each dish.

## Features

- 💬 Simple chat-style interface — type in your ingredients, get a recipe back
- 🤖 AI-generated recipes via Gemini, with randomized cuisine styles for variety each time
- ✅ Structured, validated output (recipe name, ingredients, prep time) using Pydantic schemas
- 🔁 Automatic retries if the AI response doesn't match the expected schema
- 📺 Auto-generated YouTube search link for each recipe
- ⚡ Async fetch requests — no page reloads

## File Structure

```
your_project/
├── app.py              # Flask app & routes
├── recipe_ai.py        # Gemini client, Recipe schema, prompt logic
├── templates/
│   └── index.html      # Chat UI
├── static/
│   └── chat.js          # Frontend fetch logic
├── requirements.txt
└── README.md
```

## Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/ai-recipe-finder.git
   cd ai-recipe-finder
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Gemini API key**

   Get a key from [Google AI Studio](https://aistudio.google.com/), then set it as an environment variable — never hardcode it in the source.
   ```bash
   export GEMINI_API_KEY="your-api-key-here"   # Windows: set GEMINI_API_KEY=your-api-key-here
   ```

5. **Run the app**
   ```bash
   python app.py
   ```
   Visit `http://127.0.0.1:5000` in your browser.

## requirements.txt

```
flask
google-genai
pydantic
```

## Notes

- ⚠️ Never commit your API key. Use environment variables or a `.env` file (add `.env` to `.gitignore`).
- The YouTube link is a **search link**, not a specific pre-verified video — the AI cannot browse YouTube directly.
- Recipe results are AI-generated and may occasionally need a retry if they don't match the expected format (handled automatically).

## License

MIT
