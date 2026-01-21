class InMemoryDB:
    """
    Class for Storing Information 
    """
    def __init__(self):
        self.observations = {}

    def save(self, observation):
        # Save the actual observation object
        self.observations[observation.observation_id] = observation

    def get_all(self):
        # return all the data
        return list(self.observations.values())
        
db = InMemoryDB()