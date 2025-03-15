# pixcodeos/src/custom_os.py
from ai_enhanced_pixcode import AIEnhancedPixCode
from pixcode_interpreter_with_graphs import PixCodeInterpreterWithGraphs
from virtualization import Virtualization
from math import pi, sqrt

class CustomOS:
    def __init__(self):
        """
        Initialize the CustomOS with default components.
        """
        self.ai = AIEnhancedPixCode([1, 2, 3], self)  # Initialize ai attribute
        self.ai_interpreter = AIEnhancedPixCode([])  # Empty list as default data
        self.graphs_interpreter = PixCodeInterpreterWithGraphs([1, 2, 3, 4, 5, 6, 7])  # 7 elements for heptagonal symmetry
        self.vm_manager = Virtualization()  # Add VM manager
        self.file_system = {}

    def load_file_system(self):
        """
        Load the file system with default files.
        """
        try:
            self.file_system = {
                "/file0": "data_0",
                "/file1": "data_1"
            }
            print("File system loaded.")
        except Exception as e:
            print(f"Error loading file system: {e}")

    def read_file(self, path):
        """
        Read a file from the file system.

        Parameters:
        path (str): The path to the file.

        Returns:
        str: The content of the file or an error message.
        """
        try:
            return self.file_system.get(path, "File not found")
        except Exception as e:
            print(f"Error reading file {path}: {e}")
            return "Error reading file"

    def create_vm(self, vm_name, resources=None):
        """
        Create a virtual machine with the specified resources.

        Parameters:
        vm_name (str): The name of the virtual machine.
        resources (dict, optional): The resources for the virtual machine.

        Returns:
        container: The created Docker container.
        """
        try:
            return self.vm_manager.create_vm(vm_name, resources)
        except Exception as e:
            print(f"Error creating VM {vm_name}: {e}")
            return None

    def destroy_vm(self, vm_name):
        """
        Destroy a virtual machine.

        Parameters:
        vm_name (str): The name of the virtual machine to destroy.
        """
        try:
            self.vm_manager.destroy_vm(vm_name)
        except Exception as e:
            print(f"Error destroying VM {vm_name}: {e}")

    def run_vms(self):
        """
        Get a list of running virtual machines.

        Returns:
        str: A list of running virtual machines.
        """
        try:
            return self.vm_manager.run_vms()
        except Exception as e:
            print(f"Error getting running VMs: {e}")
            return "Error getting running VMs"

# Example usage
if __name__ == "__main__":
    try:
        os_instance = CustomOS()
        os_instance.load_file_system()
        print(os_instance.read_file("/file0"))
        vm = os_instance.create_vm("TestVM")
        print(os_instance.run_vms())
        os_instance.destroy_vm("TestVM")
    except Exception as e:
        print(f"Error in CustomOS: {e}")
