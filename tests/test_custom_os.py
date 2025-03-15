import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from custom_os import CustomOS

def run_tests():
    """
    Run a series of tests on the CustomOS system.
    """
    try:
        print("\n--- Running Tests ---\n")

        os_system = CustomOS()

        # Test File Operations
        print("Testing File Operations...")
        os_system.load_file_system()
        output = os_system.read_file("/file0")
        print(output)

        # Test AI Enhanced PixCode Operations
        print("\nTesting AI Enhanced PixCode Operations...")
        ai_interpreter = os_system.ai  # Use the AI instance from CustomOS
        ai_interpreter.load_model("path/to/model")
        ai_interpreter.execute(["Loop through List", "Condition with AI enhancement"])
        print(ai_interpreter.enhance_data())

        # Test Cybersecurity Operations
        print("\nTesting Cybersecurity Operations...")
        cybersecurity = os_system.cybersecurity
        vulnerabilities = cybersecurity.scan_system()
        print("Vulnerabilities found:", vulnerabilities)
        cybersecurity.patch_vulnerabilities()

        # Test Tree and Graph Traversal
        print("\nTesting Tree and Graph Traversal...")
        os_system.graphs_interpreter.execute([
            "Tree Traversal",
            "Graph Traversal"
        ])

        # Test VM Management
        print("\nTesting VM Management...")
        vm = os_system.create_vm("TestVM", {"cpu": 1.0, "memory": "512m"})
        if vm:
            print(os_system.run_vms())
            os_system.destroy_vm("TestVM")
        else:
            print("VM creation failed. Ensure Docker is running.")

        print("\n--- All Tests Completed ---\n")
    except Exception as e:
        print(f"Error running tests: {e}")

if __name__ == "__main__":
    run_tests()