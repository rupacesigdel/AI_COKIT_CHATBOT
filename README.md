# Co_chatbot - Django CopilotKit Chatbot

## Overview

This project is a chatbot web application built using Django and the CopilotKit SDK. The application allows users to interact with an AI-powered chatbot that provides real-time responses based on user queries. The goal of this project is to explore the CopilotKit SDK, demonstrate UI/UX design principles, and integrate AI for commercial assistance.

## Contain

- [Features](#features)
- [Demo Video](#demo-video)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Demo Video
[Watch the demo video]()

## Features

- **Real-Time Chat: Users can send messages and receive real-time responses.
- **CopilotKit Integration: The chatbot is powered by CopilotKit for generating responses.
- **Interactive UI: A user-friendly chat interface built using HTML, CSS, and Bootstrap.
- **Error Handling: Displays error messages when the chatbot fails to generate a response.
- **Database Integration: Stores chat history in a database for future reference.

## Technologies Used

- Python
- Django
- CopilotKit SDK
- PostgreSQL

## Installation

### Setting Up Your Environment

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/rupacesigdel/AI_COKIT_CHATBOT.git
    cd Co_chatbot
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows: source myenv\Scripts\activate
    ```

3. **Upgrade pip (if needed):**

    ```bash
    pip install --upgrade pip
    ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Database Setup:**

    - Configure your database settings in `settings.py`.
    - Run migrations to set up the database schema:

      ```bash
      python manage.py migrate
      ```


## Project Structure
- AI_COKIT_CHATBOT/
- │
- ├── chatbot/
- │   ├── __init__.py
- │   ├── admin.py
- │   ├── apps.py
- │   ├── forms.py
- │   ├── models.py
- │   ├── tests.py
- │   ├── views.py
- │   ├── fraud_detection.py
- │   ├── templates/
- │   │   └── chatbot/
- │   │       ├── chat.html
- │   ├── static/
- │   │   └── chatbot/
- │   │       └── styles.css
- │   └── migrations/
- │       └── __init__.py
- │
- ├── Co_chatbot/
- │   ├── __init__.py
- │   ├── asgi.py
- │   ├── settings.py
- │   ├── urls.py
- │   ├── wsgi.py
- │
- ├── manage.py
- ├── README.md
- └── requirements.txt



## Usage

1. **Start the Development Server:**

    ```bash
    python manage.py runserver
    ```

2. **Access the Web Application:**

    Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.
    
3. Open the chat interface in your browser.
4. Type a message and click "Send" to interact with the chatbot.
5. The bot will generate responses using CopilotKit.


## Contributing

1. **Fork the Repository:**

    - Create a fork of the repository on GitHub.

2. **Create a Pull Request:**

    - Open a pull request from your forked repository to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **Django Community:** For the robust web framework that serves as the foundation of our application.
- **CopilotKit SDK:** For providing the powerful AI tools that drive the chatbot responses.
---

Feel free to customize this `README.md` file according to your project's specific details and requirements.
