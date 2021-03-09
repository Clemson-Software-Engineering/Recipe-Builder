import base64
import os

# Get these 3 values from registering your developer account/application with https://developer.kroger.com/
client_id = "recipe-builder-1e7cdb57aa7cc7a53546b7b52754185b1131751567875226221"
client_secret = "Tp358tZuKFzAbDVXn9UUZZtOFDSYp73VkBbgdr0Z"
redirect_uri = "http://localhost/recipeBuilder"

# Authentication requires base64 encoded id:secret, which is precalculated here
encoded_client_token = base64.b64encode(f"{client_id}:{client_secret}".encode('ascii')).decode('ascii')

# This is here to make testing the customer client easier.  Obviously we would never want to ask a user for
# this information.
# FUTURE: Remove this in favor of using the standard authorization path
customer_username = "dcathap@clemson.edu"
customer_password = "clemson2021!"
