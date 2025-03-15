# PixCodeOS - Developed by [Your Name] with AI as Co-Developer
# AI tools (e.g., Grok) generated code based on my Sator Square equations and vision.

import json
from math import sqrt

class UserProfileManager:
    def __init__(self):
        """
        Initialize the UserProfileManager with an empty user profiles dictionary.
        """
        self.user_profiles = {}

    def load_profile(self, user_id):
        """
        Load a user profile from a JSON file.

        Parameters:
        user_id (str): The ID of the user.

        Returns:
        dict: The loaded user profile.
        """
        try:
            with open(f"{user_id}_profile.json", "r") as file:
                self.user_profiles[user_id] = json.load(file)
        except FileNotFoundError:
            self.user_profiles[user_id] = {}
        except Exception as e:
            print(f"Error loading profile for user {user_id}: {e}")
            self.user_profiles[user_id] = {}

    def save_profile(self, user_id):
        """
        Save a user profile to a JSON file.

        Parameters:
        user_id (str): The ID of the user.
        """
        try:
            with open(f"{user_id}_profile.json", "w") as file:
                json.dump(self.user_profiles[user_id], file)
        except Exception as e:
            print(f"Error saving profile for user {user_id}: {e}")

    def update_profile(self, user_id, profile_data):
        """
        Update a user profile with new data.

        Parameters:
        user_id (str): The ID of the user.
        profile_data (dict): The new profile data.
        """
        try:
            if user_id not in self.user_profiles:
                self.user_profiles[user_id] = {}
            self.user_profiles[user_id].update(profile_data)
            self.save_profile(user_id)
        except Exception as e:
            print(f"Error updating profile for user {user_id}: {e}")

    def encrypt_profile(self, user_id, data):
        """
        Encrypt a user profile using the Sator Square key.

        Parameters:
        user_id (str): The ID of the user.
        data (dict): The profile data to encrypt.

        Returns:
        str: The encrypted profile data.
        """
        try:
            SATOR_KEY = ''.join(['T', 'E', 'N', 'E', 'T'])
            encrypted = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(json.dumps(data), SATOR_KEY * (len(data) // len(SATOR_KEY) + 1)))
            return encrypted
        except Exception as e:
            print(f"Error encrypting profile for user {user_id}: {e}")
            return ""

    def decrypt_profile(self, user_id, encrypted_data):
        """
        Decrypt a user profile using the Sator Square key.

        Parameters:
        user_id (str): The ID of the user.
        encrypted_data (str): The encrypted profile data.

        Returns:
        dict: The decrypted profile data.
        """
        try:
            SATOR_KEY = ''.join(['T', 'E', 'N', 'E', 'T'])
            decrypted = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(encrypted_data, SATOR_KEY * (len(encrypted_data) // len(SATOR_KEY) + 1)))
            return json.loads(decrypted)
        except Exception as e:
            print(f"Error decrypting profile for user {user_id}: {e}")
            return {}

# Example usage
if __name__ == "__main__":
    try:
        profile_manager = UserProfileManager()
        profile_manager.load_profile("User123")
        profile_manager.update_profile("User123", {"theme": "dark"})
        encrypted_data = profile_manager.encrypt_profile("User123", profile_manager.user_profiles["User123"])
        print("Encrypted Data:", encrypted_data)
        decrypted_data = profile_manager.decrypt_profile("User123", encrypted_data)
        print("Decrypted Data:", decrypted_data)
    except Exception as e:
        print(f"Error in UserProfileManager: {e}")
