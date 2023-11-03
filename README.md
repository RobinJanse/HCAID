# HCAID
This project is built for the minor Artificial Intelligence. Specifically built for Human Centric AI Design, where AI ethics is the main focus. The project is built with the Django framework.

## Installation and Running the Server

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Navigate to the hcaidApi directory:

```bash
cd django/hcaidApi
```

3. Start the server:

```bash	
python manage.py runserver
```

## Troubleshooting
If the styling isn't working, navigate back to the root directory and run the _collectstatic_ management command:

```bash	
python manage.py collectstatic
```

This command will collect all the static files into the STATIC_ROOT directory, which is defined in the settings.py file.
