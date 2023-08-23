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
                             'color': 'ajisai',
                             'timezone': 'America/Los_Angeles'
                             }

    def create_graph(self):
        """
        Create a graph on Pixela using the specified parameters.
        """
        graph_response = requests.post(url=self.graph_endpoint, json=self.graph_params, headers=self.header)
        print(graph_response.text)

    def update_graph(self):
        update_graph_endpoint = f"{self.graph_endpoint}/{GRAPH_ID}"
        updated_graph = requests.put(url=update_graph_endpoint, json=self.graph_params, headers=self.header)
        print(updated_graph.text)


