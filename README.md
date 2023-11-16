# 4-Phrase 📚🌐

4-Phrase is a powerful API designed for fetching word meanings from various online sources, including Urban Dictionary and Oxford Dictionary. Dive into the world of words and expressions with ease!

## Deployment 🚀
This project is deployed on [Render](https://render.com/), and you can access the API via [https://four-word.onrender.com](https://four-word.onrender.com) url.

If you want to explore it out, go to [Swagger](https://four-word.onrender.com/docs) and test the API directl in your browser.

## Project Structure 🌳

```
├── app
│   ├── configs
│   │   ├── environment.py
│   │   └── logger.py
│   ├── controller
│   │   ├── controller_word.py
│   ├── domain
│   │   ├── mapper
│   │   │   ├── map_urban_dictionary.py
│   │   ├── dictionary.py
│   │   └── word_params.py
│   ├── endpoints
│   │   ├── phrase.py
│   │   └── word.py
│   ├── http
│   │   ├── core_service.py
│   │   ├── http_client.py
│   ├── models
│   ├── openai
│   │   └── request.py
│   ├── webscraping
│   │   └── oxford.py
├── routes
│   ├── api.py
├── main.py
├── README.md
├── requirements.txt
```

## Technologies Used 🛠️
- FastAPI
- Pydantic
- Async
- BeautifulSoup4
- Requests

## How to Run 🏃‍♂️

### Step 1: Create a Python Virtual Environment

To ensure a clean and isolated environment for running the 4-Phrase API, you'll want to create a Python virtual environment. Follow these steps:

#### For Windows:
```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate
```

#### For macOS/Linux:
```bash
# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

Once activated, your terminal prompt should change to indicate that you are now working within the virtual environment.

### Step 2: Install Dependencies

With the virtual environment active, install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Step 3: Launch the API

Choose one of the following methods to start the 4-Phrase API:

- Using Uvicorn:
  ```bash
  uvicorn main:app --host 0.0.0.0 --port $PORT
  ```

- Using VSCode Debug: Set up a debug configuration in VSCode and start the application using the debugger.

Now, your 4-Phrase API should be up and running, ready to fetch word meanings from various sources! 🌐📖