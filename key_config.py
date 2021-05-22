# Any keys used in the app will be called from this file

import os
SECRET_KEY = os.getenv("secret_key", "change-me-or-delete-me")