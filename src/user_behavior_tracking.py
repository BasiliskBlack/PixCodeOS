import json
import os
from datetime import datetime

class UserBehaviorTracker:
    def __init__(self, log_file='user_behavior_log.json'):
        self.log_file = log_file
        self.load_log()

    def load_log(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as file:
                self.log = json.load(file)
        else:
            self.log = []

    def save_log(self):
        with open(self.log_file, 'w') as file:
            json.dump(self.log, file, indent=4)

    def log_action(self, action):
        timestamp = datetime.now().isoformat()
        self.log.append({'timestamp': timestamp, 'action': action})
        self.save_log()

# Example usage
if __name__ == "__main__":
    tracker = UserBehaviorTracker()
    tracker.log_action('opened_file')
    tracker.log_action('closed_file')