# News-App Project

## Description
This project is an News App developed using Django and Bootstrap for UI design.

## Features
- News according to the user location.
- News according to other countries and categories.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/SaugatMgr/News-App.git
    ```
2. Navigate to the project directory:
    ```bash
    cd News-App
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

A `.env.local` file needs to be created in the main project folder with the following contents:
```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=postgres://db_user:db_password@localhost:db_port_number/db_name
NEWS_API_KEY=your_news_api_key
```

Then follow the following steps:
1. **Create a superuser:**
    - Run the following command and follow the prompts:
        ```bash
        python manage.py createsuperuser
        ```
2. **Run the server:**
    ```bash
    python manage.py runserver
    ```
    
## Usage
Note: At first, you need to register and create API key for the News API used in this project. Go to [https://newsapi.org] and register account then click on Get API key. After you get API key, paste it to the env file in the project.

## Technologies Used
- Django for the web framework
- Jazzmin for the admin panel customization
- Bootstrap for UI
