# src/virtualization.py
import docker
from math import pi, sqrt
from sklearn.linear_model import LinearRegression
import numpy as np

class Virtualization:
    def __init__(self):
        """
        Initialize the Virtualization class with default values.
        """
        self.virtual_machines = {}
        self.client = docker.from_env()
        self.phi = (1 + sqrt(5)) / 2
        self.model = LinearRegression()
        self.usage_history = []  # [cpu_usage, memory_usage] pairs
        self.mystic_factor = 1.5  # Add mystic_factor attribute

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
            if resources is None:
                resources = {"cpu": 1.0, "memory": "512m"}
            
            # Predict optimal resources if enough data
            if len(self.usage_history) >= 5:
                X = np.array([h[0] for h in self.usage_history]).reshape(-1, 1)
                y = [h[1] for h in self.usage_history]
                self.model.fit(X, y)
                pred_memory = self.model.predict([[resources["cpu"]]])[0]
                resources["memory"] = f"{int(pred_memory)}m"

            pentagonal_scale = (pi + self.phi + sqrt(5)) / 3
            scaled_cpu = resources["cpu"] * pentagonal_scale
            memory_value = int(resources["memory"].replace('m', ''))
            scaled_memory = f"{int(memory_value * pentagonal_scale)}m"
            
            container = self.client.containers.run(
                "ubuntu:latest", detach=True, name=vm_name, command="tail -f /dev/null",
                cpu_quota=int(scaled_cpu * 100000), mem_limit=scaled_memory
            )
            self.virtual_machines[vm_name] = container
            self.usage_history.append([scaled_cpu, memory_value])  # Log usage
            print(f"Created VM: {vm_name} with AI-optimized resources")
            return container
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
            if vm_name in self.virtual_machines:
                self.virtual_machines[vm_name].stop()
                self.virtual_machines[vm_name].remove()
                del self.virtual_machines[vm_name]
                print(f"Destroyed VM: {vm_name}")
            else:
                print(f"VM {vm_name} not found.")
        except Exception as e:
            print(f"Error destroying VM {vm_name}: {e}")

    def run_vms(self):
        """
        Get a list of running virtual machines.

        Returns:
        str: A list of running virtual machines.
        """
        try:
            return f"Running VMs: {list(self.virtual_machines.keys())}"
        except Exception as e:
            print(f"Error getting running VMs: {e}")
            return "Error getting running VMs"

# Example usage
if __name__ == "__main__":
    try:
        vm_manager = Virtualization()
        vm_manager.create_vm("TestVM1")
        vm_manager.create_vm("TestVM2", {"cpu": 2.0, "memory": "1024m"})
        print(vm_manager.run_vms())
    except Exception as e:
        print(f"Error in Virtualization: {e}")
