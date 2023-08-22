import requests
from datetime import datetime
from constant import TOKEN, USER_NAME, PIXELA_END_POINT, GRAPH_ID


class Pixel:
    """
    Class for managing individual pixels on Pixela graphs.
    """

    def __init__(self, time: datetime, hours):
        """Constructor to create  object Pixel
        :param time : type hint takes datetime object
        :param hours: type string takes number"""
        self.day = time
        self.hour = hours
        self.header = {'X-USER-TOKEN': TOKEN}
        self.pixel_dot_endpoint = f"{PIXELA_END_POINT}/{USER_NAME}/graphs/{GRAPH_ID}"
        self.pixel_dot_params = {'date': self.day.strftime("%Y%m%d"),
                                 'quantity': self.hour,
                                 }

    def create_pixel(self):
        """
        Create a pixel on a Pixela graph for the current day and specified quantity.
        """
        response_pixel = requests.post(url=self.pixel_dot_endpoint, json=self.pixel_dot_params, headers=self.header)
        print(response_pixel.text)

    def update_pixel(self, day: datetime, update: dict):
        """
        Update a pixel on a Pixela graph for the specified day with the provided update data.

        param day: The date for the pixel to update.
        param update: A dictionary containing the update data.
        """
        update_endpoint = f"{self.pixel_dot_endpoint}/{day.strftime('%Y%m%d')}"
        updated_response = requests.put(url=update_endpoint, json=update, headers=self.header)
        print(updated_response.text)

    def delete_pixel(self, day: datetime):
        """
        Delete a pixel on a Pixela graph for the specified day.

        :param day: The date for the pixel to delete.
        """
        delete_endpoint = f"{self.pixel_dot_endpoint}/{day.strftime('%Y%m%d')}"
        delete_response = requests.delete(url=delete_endpoint, headers=self.header)
        print(delete_response.text)
