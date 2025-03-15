class VMManagement:
    def __init__(self):
        """
        Initialize the VMManagement with an empty list of VMs.
        """
        self.vms = []

    def create_vm(self, name):
        """
        Create a virtual machine with the specified name.

        Parameters:
        name (str): The name of the virtual machine.
        """
        try:
            if not isinstance(name, str) or not name:
                raise ValueError("VM name must be a non-empty string.")
            self.vms.append(name)
            print(f"VM '{name}' created.")
        except Exception as e:
            print(f"Error creating VM '{name}': {e}")

    def list_vms(self):
        """
        List all virtual machines.

        Returns:
        list: A list of virtual machine names.
        """
        try:
            return self.vms
        except Exception as e:
            print(f"Error listing VMs: {e}")
            return []

    def delete_vm(self, name):
        """
        Delete a virtual machine with the specified name.

        Parameters:
        name (str): The name of the virtual machine to delete.
        """
        try:
            if name in self.vms:
                self.vms.remove(name)
                print(f"VM '{name}' deleted.")
            else:
                print(f"VM '{name}' not found.")
        except Exception as e:
            print(f"Error deleting VM '{name}': {e}")

# Example usage
if __name__ == "__main__":
    try:
        manager = VMManagement()
        manager.create_vm("TestVM")
        print("VMs:", manager.list_vms())
        manager.delete_vm("TestVM")
        print("VMs after deletion:", manager.list_vms())
    except Exception as e:
        print(f"Error in VMManagement: {e}")