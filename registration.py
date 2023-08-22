# Import necessary libraries and constants
import requests
from constant import TOKEN, USER_NAME, PIXELA_END_POINT


class Registration:
    """
    Class for user registration with Pixela.
    """

    def __init__(self):
        self.pixela_endpoint = PIXELA_END_POINT
        self.users_params = {'token': TOKEN,
                             'username': USER_NAME,
                             'agreeTermsOfService': 'yes',
                             'notMinor': 'yes',
                             'thanksCode': 'bfc10f75c93aae60ff105ea242a134b356de1b6dce85567ae4abf0b811b5880d'
                             }
        self.header = {'X-USER-TOKEN': TOKEN}

    def register(self):
        """
        Register a user with Pixela using the specified parameters.
        """
        registration_response = requests.post(url=self.pixela_endpoint, json=self.users_params)
        print(registration_response.text)
