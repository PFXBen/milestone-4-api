# Milestone 4 API

This repository contains the API code for Milestone 4 of a Django project. The API is designed to provide functionality and data access for the project's application.

## Getting Started

To get started with the API, follow the instructions below:

### Prerequisites

- Python (version 3.6 or higher)
- Django (version 3.2 or higher)
- PostgreSQL or MySQL (or any other supported database)
- Stripe CLI

### Required .env variables (to be set locally and in heroku)
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOSTNAME
- DB_PORT
- STRIPE_PUBLISHABLE_KEY
- STRIPE_SECRET_KEY
- STRIPE_ENDPOINT_SECRET

### Installation

1. Clone this repository to your local machine or download the source code as a ZIP file.

```shell
git clone https://github.com/PFXBen/milestone-4-api.git
```

2. Navigate to the project directory.

```shell
cd milestone-4-api
```

3. Create and activate a virtual environment (optional but recommended).

```shell
python3 -m venv env
source env/bin/activate
```

4. Install the required packages.

```shell
pip install -r requirements.txt
```

5. Configure the API.

   - Open the `settings.py` file and provide the necessary configuration values, such as the database settings and secret key.

6. Run database migrations.

```shell
python manage.py migrate
```

7. Start the development server.

```shell
python manage.py runserver 5000
```

The API should now be running on `http://localhost:5000`.

### Setting Up Stripe CLI Webhook

1. Install the Stripe CLI by following the instructions in the [Stripe CLI documentation](https://stripe.com/docs/stripe-cli).

2. Authenticate the Stripe CLI with your Stripe account.

```shell
stripe login
```

3. Forward the webhook events to your local development server.

```shell
stripe listen --forward-to http://localhost:5000/webhook
```

This command sets up the Stripe CLI to listen for webhook events and forwards them to your local development server running on port 5000.

4. Copy the webhook signing secret provided by the Stripe CLI.

5. In your Django project, open the `.env` file and paste the webhook signing secret in the appropriate location.

```python
STRIPE_WEBHOOK_SECRET = 'your_webhook_signing_secret'
```

Replace `'your_webhook_signing_secret'` with the actual webhook signing secret provided by the Stripe CLI.



## API Endpoints

The API endpoints are generated based on the views.py files in each application of the Django project. Please refer to the views.py files of each application for the specific endpoints and their corresponding functions.

To access the API endpoints, you can use tools such as cURL or Postman.

Example:

```shell
curl -X

 GET http://localhost:5000/api/users
```

## Authentication

The API may use various authentication mechanisms depending on the project's configuration. Please refer to the project's documentation or code to determine the specific authentication requirements for accessing protected endpoints.

## Error Handling

If an error occurs in the API, it will return an error response in the following format:

```json
{
  "error": {
    "message": "Error message",
    "status": 400
  }
}
```

## Contributing

Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit your code.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

Please make sure to follow the existing code style and include appropriate tests for your changes.

## License

This project is licensed under the [MIT License](LICENSE).
