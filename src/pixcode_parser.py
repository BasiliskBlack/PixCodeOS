# pixcodeos/src/pixcode_parser.py
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsRectItem

class PixCodeParser:
    def __init__(self, pixcode_image):
        """
        Initialize the PixCodeParser with a PixCode image.

        Parameters:
        pixcode_image (list): The PixCode image to be parsed.
        """
        self.pixcode_image = pixcode_image

    def parse(self):
        """
        Parse the PixCode image into Python code.

        Returns:
        str: The parsed Python code.
        """
        code = ""
        try:
            for shape in self.pixcode_image:
                if shape["shape"] == "Red Circle":
                    code += f"{shape['value']}\n"
                elif shape["shape"] == "Blue Square":
                    code += f"for {shape['value']}:\n"
                elif shape["shape"] == "Green Triangle":
                    code += f"if {shape['value']}:\n"
        except Exception as e:
            print(f"Error in parse method: {e}")
        return code

    def parse_with_connections(self):
        """
        Parse the PixCode image into Python code with connections.

        Returns:
        str: The parsed Python code with connections.
        """
        code = ""
        try:
            for shape in self.pixcode_image:
                value = shape["value"]
                if shape["shape"] == "Red Circle":
                    code += f"{value}\n"
                elif shape["shape"] == "Blue Square":
                    if " in " in value:
                        loop_var = value.split(" in ")[0].strip()
                        loop_range = value.split(" in ")[1].strip()
                        code += f"for {loop_var} in {loop_range}:\n"
                    else:
                        code += f"for i in range(3):  # Default loop: {value}\n"  # Fallback
                    for conn in shape.get("connections", []):
                        if isinstance(conn, QGraphicsEllipseItem):
                            code += f"    print({conn.toolTip().split(': ')[1]})\n"
                elif shape["shape"] == "Green Triangle":
                    code += f"if {value}:\n"
                    for conn in shape.get("connections", []):
                        if isinstance(conn, QGraphicsEllipseItem):
                            code += f"    print({conn.toolTip().split(': ')[1]})\n"
        except Exception as e:
            print(f"Error in parse_with_connections method: {e}")
        return code

# Example usage
if __name__ == "__main__":
    try:
        pixcode_image = [
            {"shape": "Red Circle", "value": "print('Hello, World!')"},
            {"shape": "Blue Square", "value": "i in range(5)", "connections": []},
            {"shape": "Green Triangle", "value": "i % 2 == 0", "connections": []}
        ]
        parser = PixCodeParser(pixcode_image)
        code = parser.parse()
        print("Parsed Code:\n", code)
        code_with_connections = parser.parse_with_connections()
        print("Parsed Code with Connections:\n", code_with_connections)
    except Exception as e:
        print(f"Error in PixCodeParser: {e}")
