# PixCodeOS - Developed by MICAH BLAKE LANGFORD with AI as Co-Developer
# AI tools (e.g., Grok) generated code based on advanced sci-fi and eldritch properties.

import os
import sys
import numpy as np
from time import sleep

# Add the src directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(project_root, 'src'))

from custom_os import CustomOS
from pixcode_interpreter_with_graphs import PixCodeInterpreterWithGraphs
from ai_enhanced_pixcode import AIEnhancedPixCode
from cybersecurity_pixcode import CybersecurityPixCode
from virtualization import Virtualization
from ryoiki_tenkai.ai_engine import AIEngine
from ryoiki_tenkai.ui_generator import UIGenerator
from ryoiki_tenkai.user_profile_manager import UserProfileManager
from ryoiki_tenkai.vm_integration import RyoikiTenkaiVM
from converter import PythonToPixCode
from pixcode_parser import PixCodeParser

def run_tests():
    """
    Run a series of tests on the PixCodeOS system.
    """
    try:
        print("\n--- Running Tests ---\n")

        # Initialize PixCodeOS system
        os_system = CustomOS()

        # Test File Operations
        print("Testing File Operations...")
        os_system.load_file_system()
        output = os_system.read_file("/file0")
        print(output)

        # Test AI Enhanced PixCode Operations with Fractal Shield and Mystic Scaling
        print("\nTesting AI Enhanced PixCode Operations with Fractal Shield and Mystic Scaling...")
        ai_interpreter = os_system.ai  # Use the AI instance from CustomOS
        ai_interpreter.load_model("path/to/model")
        ai_interpreter.execute(["Loop through List", "Condition with AI enhancement"])
        print(ai_interpreter.enhance_data())

        # Test empty data with Fractal Shield and Mystic Scaling
        empty_ai = AIEnhancedPixCode(np.array([]))
        empty_ai.load_model("path/to/model")
        try:
            print(empty_ai.enhance_data())  # Should handle empty data gracefully with curse warning
        except Exception as e:
            print(f"Empty data handled due to curse interference: {e}")

        # Test Cybersecurity Operations
        print("\nTesting Cybersecurity Operations...")
        cybersecurity = CybersecurityPixCode()
        vulnerabilities = cybersecurity.scan_system()
        print("Vulnerabilities found:", vulnerabilities)
        cybersecurity.patch_vulnerabilities()

        # Test VM Operations with Quantum Warp and Eldritch Scaling
        print("\nTesting VM Operations with Quantum Warp and Eldritch Scaling...")
        try:
            vm = os_system.create_vm("TestVM", {"cpu": 1.0, "memory": "512m"})
            if vm:
                print(os_system.run_vms())
                sleep(2 * os_system.vm_manager.mystic_factor)  # Wait scaled by mystic energy
                os_system.destroy_vm("TestVM")
            else:
                print("VM creation failed due to eldritch interference. Ensure Docker and mystic balance are maintained.")
        except Exception as e:
            print(f"VM test failed due to curse backlash: {e}. Ensure Docker and mystic systems are stable.")

        # Test Tree and Graph Traversal (normal case) with Dimensional and Eldritch Scaling
        print("\nTesting Tree and Graph Traversal (Normal) with Dimensional and Eldritch Scaling...")
        os_system.graphs_interpreter.execute([
            "Tree Traversal",
            "Graph Traversal"
        ])

        # Test Tree and Graph Traversal (empty data) with Dimensional and Eldritch Scaling
        print("\nTesting Tree and Graph Traversal (Empty) with Dimensional and Eldritch Scaling...")
        empty_graphs = PixCodeInterpreterWithGraphs([])
        try:
            empty_graphs.execute(["Tree Traversal", "Graph Traversal"])
        except Exception as e:
            print(f"Empty graph data handled due to curse interference: {e}")

    except Exception as e:
        print(f"Error running tests: {e}")

if __name__ == "__main__":
    run_tests()
