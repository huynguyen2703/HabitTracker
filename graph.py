import requests
from constant import TOKEN, USER_NAME, PIXELA_END_POINT, GRAPH_ID


class Graph:
    """
    Class for managing Pixela graphs.
    """

    def __init__(self):
        self.header = {'X-USER-TOKEN': TOKEN}
        self.graph_endpoint = f"{PIXELA_END_POINT}/{USER_NAME}/graphs"
        self.graph_params = {'id': GRAPH_ID,
                             'name': 'Coding Tracker',
                             'unit': 'Hour',
                             'type': 'float',
                             'color': 'ajisai'
                             }

    def create_graph(self):
        """
        Create a graph on Pixela using the specified parameters.
        """
        graph_response = requests.post(url=self.graph_endpoint, json=self.graph_params, headers=self.header)
        print(graph_response.text)
