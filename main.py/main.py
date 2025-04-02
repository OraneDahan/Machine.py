class Machine:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.status = "off"
    
    def start(self):
        self.status = "on"
        print(f"The {self.name} ({self.model}) is now running.")
    
    def stop(self):
        self.status = "off"
        print(f"The {self.name} ({self.model}) is now off.")
    
    def get_status(self):
        return f"The {self.name} ({self.model}) is {self.status}."