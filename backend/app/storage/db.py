import json

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

    def save_to_disk(self):
    # data saved to json
        data_to_save = {
            obs_id: obs.__dict__ for obs_id, obs in self.observations.items()
        }
        data_to_save = {
        }
        with open("data_backup.json", "w") as f:
            json.dump(data_to_save, f, indent=4)

    def clear(self):
        self.records = []

db = InMemoryDB() # app is talking to the same dictionary