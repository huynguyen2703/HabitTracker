from datetime import datetime
from registration import Registration
from graph import Graph
from pixel import Pixel

# Get the current date and time in UTC
today = datetime.now().utcnow()

# Prompt the user for the number of hours they have coded today
hours_prompt = input('How many hours have you coded today? ')

# Create instances of Registration, Graph, and Pixel classes
account = Registration()
the_graph = Graph()
the_pixel = Pixel(today, hours_prompt)

# Register the user
account.register()

# Create a graph for tracking coding hours
the_graph.create_graph()

# Create a pixel to represent the coding hours for today
the_pixel.create_pixel()
