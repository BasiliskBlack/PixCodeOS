import numpy as np

class AdvancedPixCodeInterpreter:
    def __init__(self):
        """
        Initialize the AdvancedPixCodeInterpreter with an empty data array.
        """
        self.data = np.array([])

    def load_data(self, data):
        """
        Load data into the interpreter.

        Parameters:
        data (list or np.ndarray): The data to load.
        """
        try:
            self.data = np.array(data)
        except Exception as e:
            print(f"Error loading data: {e}")

    def process_data(self):
        """
        Process the data by doubling each element.

        Returns:
        np.ndarray: The processed data.
        """
        try:
            processed_data = self.data * 2  # Example processing
            return processed_data
        except Exception as e:
            print(f"Error processing data: {e}")
            return None

    def normalize_data(self):
        """
        Normalize the data to have values between 0 and 1.

        Returns:
        np.ndarray: The normalized data.
        """
        try:
            normalized_data = (self.data - np.min(self.data)) / (np.max(self.data) - np.min(self.data))
            return normalized_data
        except Exception as e:
            print(f"Error normalizing data: {e}")
            return None

    def save_data(self, filename):
        """
        Save the data to a file.

        Parameters:
        filename (str): The name of the file to save the data to.
        """
        try:
            np.save(filename, self.data)
        except Exception as e:
            print(f"Error saving data: {e}")

if __name__ == "__main__":
    interpreter = AdvancedPixCodeInterpreter()
    interpreter.load_data([1, 2, 3, 4, 5])
    print("Processed Data:", interpreter.process_data())
    print("Normalized Data:", interpreter.normalize_data())
    interpreter.save_data("processed_data.npy")