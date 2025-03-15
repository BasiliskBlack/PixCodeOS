import sys
import os
import json
from PyQt5.QtWidgets import (QApplication, QMainWindow, QGraphicsView, QGraphicsScene, 
                             QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QTextEdit, 
                             QLabel, QToolBar, QLineEdit, QFileDialog, QMessageBox,
                             QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsPathItem, QGraphicsLineItem)
from PyQt5.QtGui import QPen, QColor, QPainterPath, QPainter
from PyQt5.QtCore import Qt, QRectF, QPointF, QEvent

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)
from src.custom_os import CustomOS
from src.pixcode_parser import PixCodeParser
from src.pixcode_interpreter_with_graphs import PixCodeInterpreterWithGraphs
from src.ryoiki_tenkai.ai_engine import AIEngine

class PixCodeIDE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PixCode IDE - Visual Programming")
        self.setGeometry(100, 100, 1200, 800)
        self.os_instance = CustomOS()
        self.parser = PixCodeParser([])
        self.interpreter = PixCodeInterpreterWithGraphs([1, 2, 3])
        self.ai_engine = AIEngine()
        self.user_id = "User123"
        self.init_ui()
        self.selected_item = None
        self.shape_usage = {"circle": 0, "square": 0, "triangle": 0}
        self.drag_offset = None
        self.lines = []
        self.action_history = []  # For undo
        self.redo_history = []    # For redo

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setSceneRect(0, 0, 600, 600)
        self.view.setRenderHint(QPainter.Antialiasing)
        main_layout.addWidget(self.view)
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        main_layout.addWidget(right_panel)
        toolbar = QToolBar("Tools")
        self.addToolBar(Qt.TopToolBarArea, toolbar)
        toolbar.addAction("Circle (Variable)", lambda: self.add_shape("circle"))
        toolbar.addAction("Square (Loop)", lambda: self.add_shape("square"))
        toolbar.addAction("Triangle (If)", lambda: self.add_shape("triangle"))
        toolbar.addAction("Line (Connection)", self.start_connection)
        toolbar.addAction("Undo", self.undo_action)
        toolbar.addAction("Redo", self.redo_action)  # Redo button added
        toolbar.addAction("Clear Canvas", self.clear_canvas)
        toolbar.addSeparator()
        toolbar.addAction("Save .pixcode", self.save_pixcode)
        toolbar.addAction("Load .pixcode", self.load_pixcode)
        self.prop_label = QLabel("Properties:")
        right_layout.addWidget(self.prop_label)
        self.prop_value = QLineEdit("x = 5")
        self.prop_value.textChanged.connect(self.update_selected_shape)
        right_layout.addWidget(self.prop_value)
        self.code_label = QLabel("Generated Python Code:")
        right_layout.addWidget(self.code_label)
        self.code_text = QTextEdit()
        self.code_text.setReadOnly(True)
        right_layout.addWidget(self.code_text)
        self.ai_suggestion = QLabel("AI Suggestion: None")
        right_layout.addWidget(self.ai_suggestion)
        run_button = QPushButton("Run PixCode")
        run_button.clicked.connect(self.run_code)
        right_layout.addWidget(run_button)
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        right_layout.addWidget(self.output_text)
        self.view.setMouseTracking(True)
        self.view.viewport().installEventFilter(self)
        self.connecting = False
        self.start_item = None

    def add_shape(self, shape_type):
        self.shape_usage[shape_type] += 1
        x = 50 + (len(self.scene.items()) % 5) * 50
        y = 50 + (len(self.scene.items()) // 5) * 50
        if shape_type == "circle":
            item = self.scene.addEllipse(x, y, 40, 40, QPen(Qt.black), QColor("#FF5555"))
            item.setToolTip(f"Variable: {self.prop_value.text()}")
        elif shape_type == "square":
            item = self.scene.addRect(x, y, 40, 40, QPen(Qt.black), QColor("#5555FF"))
            item.setToolTip(f"Loop: {self.prop_value.text()}")
        elif shape_type == "triangle":
            path = QPainterPath()
            path.moveTo(x + 20, y)
            path.lineTo(x + 40, y + 40)
            path.lineTo(x, y + 40)
            path.closeSubpath()
            item = self.scene.addPath(path, QPen(Qt.black), QColor("#55FF55"))
            item.setToolTip(f"If: {self.prop_value.text()}")
        item.setFlag(item.ItemIsMovable)
        item.setFlag(item.ItemIsSelectable)
        item.setData(0, [])
        self.action_history.append(("add_shape", item))
        self.redo_history.clear()  # Clear redo history on new action
        self.update_code_preview()

    def start_connection(self):
        self.connecting = not self.connecting
        if self.connecting:
            self.start_item = None
            self.statusBar().showMessage("Connection mode: Click first shape")
            print("Connection mode started")
        else:
            self.statusBar().clearMessage()
            print("Connection mode canceled")

    def eventFilter(self, obj, event):
        if obj is self.view.viewport() and event.type() == QEvent.MouseButtonPress:
            pos = self.view.mapToScene(event.pos())
            items = self.scene.items(pos)
            item = next((i for i in items if isinstance(i, (QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsPathItem))), None)
            print(f"Clicked at {pos}, item: {item}")

            if self.connecting:
                if not item:
                    self.statusBar().showMessage("Clicked empty space - select a shape")
                elif not self.start_item:
                    self.start_item = item
                    self.statusBar().showMessage(f"Selected {item.toolTip()} - now click second shape")
                    print(f"Start item set: {item.toolTip()}")
                elif item == self.start_item:
                    self.statusBar().showMessage("Cannot connect shape to itself - select a different shape")
                    print("Clicked same item, waiting for second shape")
                else:
                    line = self.scene.addLine(
                        self.start_item.pos().x() + 20, self.start_item.pos().y() + 20,
                        item.pos().x() + 20, item.pos().y() + 20, QPen(Qt.black, 2)
                    )
                    line.setZValue(-1)  # Lines behind shapes
                    line.setData(0, [self.start_item, item])
                    self.start_item.data(0).append(item)
                    self.lines.append(line)
                    self.action_history.append(("add_connection", line))
                    self.redo_history.clear()  # Clear redo history on new action
                    print(f"Connected {self.start_item.toolTip()} to {item.toolTip()}")
                    self.connecting = False
                    self.start_item = None
                    self.statusBar().clearMessage()
                    self.scene.update()
                    self.view.viewport().update()  # Force redraw
                    self.update_code_preview()
            elif item:
                self.selected_item = item
                self.prop_value.setText(item.toolTip().split(": ")[1])
                self.drag_offset = pos - item.pos()

        elif obj is self.view.viewport() and event.type() == QEvent.MouseMove and self.selected_item and not self.connecting:
            pos = self.view.mapToScene(event.pos())
            self.selected_item.setPos(pos - self.drag_offset)
            self.update_lines()
            self.update_code_preview()

        elif obj is self.view.viewport() and event.type() == QEvent.MouseButtonRelease:
            self.selected_item = None
            self.drag_offset = None

        return super().eventFilter(obj, event)

    def update_lines(self):
        for line in self.lines:
            start_item, end_item = line.data(0)
            line.setLine(start_item.pos().x() + 20, start_item.pos().y() + 20,
                         end_item.pos().x() + 20, end_item.pos().y() + 20)
        self.scene.update()

    def undo_action(self):
        if not self.action_history:
            QMessageBox.information(self, "Undo", "Nothing to undo!")
            return
        action_type, item = self.action_history.pop()
        self.redo_history.append((action_type, item))  # Add to redo history
        if action_type == "add_shape":
            self.scene.removeItem(item)
            shape_type = "circle" if isinstance(item, QGraphicsEllipseItem) else \
                         "square" if isinstance(item, QGraphicsRectItem) else "triangle"
            self.shape_usage[shape_type] -= 1
        elif action_type == "add_connection":
            self.scene.removeItem(item)
            self.lines.remove(item)
            start_item, end_item = item.data(0)
            start_item.data(0).remove(end_item)
        self.scene.update()
        self.view.viewport().update()
        self.update_code_preview()
        print(f"Undid {action_type}")

    def redo_action(self):
        if not self.redo_history:
            QMessageBox.information(self, "Redo", "Nothing to redo!")
            return
        action_type, item = self.redo_history.pop()
        self.action_history.append((action_type, item))  # Add back to action history
        if action_type == "add_shape":
            self.scene.addItem(item)
            shape_type = "circle" if isinstance(item, QGraphicsEllipseItem) else \
                         "square" if isinstance(item, QGraphicsRectItem) else "triangle"
            self.shape_usage[shape_type] += 1
        elif action_type == "add_connection":
            self.scene.addItem(item)
            self.lines.append(item)
            start_item, end_item = item.data(0)
            start_item.data(0).append(end_item)
        self.scene.update()
        self.view.viewport().update()
        self.update_code_preview()
        print(f"Redid {action_type}")

    def clear_canvas(self):
        self.scene.clear()
        self.lines = []
        self.shape_usage = {"circle": 0, "square": 0, "triangle": 0}
        self.action_history = []
        self.redo_history = []
        self.update_code_preview()
        print("Canvas cleared")

    def update_selected_shape(self):
        if self.selected_item:
            shape_type = "Variable" if isinstance(self.selected_item, QGraphicsEllipseItem) else \
                         "Loop" if isinstance(self.selected_item, QGraphicsRectItem) else "If"
            self.selected_item.setToolTip(f"{shape_type}: {self.prop_value.text()}")
            self.update_code_preview()

    def update_code_preview(self):
        shapes = []
        for item in self.scene.items():
            if isinstance(item, (QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsPathItem)):
                shape_type = "Red Circle" if isinstance(item, QGraphicsEllipseItem) else \
                             "Blue Square" if isinstance(item, QGraphicsRectItem) else "Green Triangle"
                value = item.toolTip().split(": ")[1]
                connections = [i.toolTip() for i in item.data(0)]
                shapes.append({"shape": shape_type, "value": value, "connections": connections})
        self.parser.pixcode_image = shapes
        code = self.parser.parse_with_connections()
        self.code_text.setText(code)

    def run_code(self):
        code = self.code_text.toPlainText()
        try:
            exec(code, globals())
            self.interpreter.data = [1, 2, 3]
            self.interpreter.execute(["Tree Traversal"])
            self.output_text.setText(f"Result: {self.interpreter.data}")
        except Exception as e:
            self.output_text.setText(f"Error: {e}")

    def save_pixcode(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save PixCode", "", "PixCode Files (*.pixcode)")
        if filename:
            data = [
                {"type": "circle" if isinstance(item, QGraphicsEllipseItem) else 
                         "square" if isinstance(item, QGraphicsRectItem) else 
                         "triangle" if isinstance(item, QGraphicsPathItem) else "line",
                 "x": item.pos().x(), "y": item.pos().y(),
                 "value": item.toolTip().split(": ")[1] if not isinstance(item, QGraphicsLineItem) else None}
                for item in self.scene.items()
            ]
            with open(filename, "w") as f:
                json.dump(data, f)

    def load_pixcode(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Load PixCode", "", "PixCode Files (*.pixcode)")
        if filename:
            self.clear_canvas()
            with open(filename, "r") as f:
                data = json.load(f)
            for item in data:
                if item["type"] == "circle":
                    shape = self.scene.addEllipse(item["x"], item["y"], 40, 40, QPen(Qt.black), QColor("#FF5555"))
                    shape.setToolTip(f"Variable: {item['value']}")
                elif item["type"] == "square":
                    shape = self.scene.addRect(item["x"], item["y"], 40, 40, QPen(Qt.black), QColor("#5555FF"))
                    shape.setToolTip(f"Loop: {item['value']}")
                elif item["type"] == "triangle":
                    path = QPainterPath()
                    path.moveTo(item["x"] + 20, item["y"])
                    path.lineTo(item["x"] + 40, item["y"] + 40)
                    path.lineTo(item["x"], item["y"] + 40)
                    path.closeSubpath()
                    shape = self.scene.addPath(path, QPen(Qt.black), QColor("#55FF55"))
                    shape.setToolTip(f"If: {item['value']}")
                elif item["type"] == "line":
                    self.scene.addLine(item["x"], item["y"], item["x"] + 40, item["y"] + 40, QPen(Qt.black))
                if item["type"] != "line":
                    shape.setFlag(shape.ItemIsMovable)
                    shape.setFlag(shape.ItemIsSelectable)
                    shape.setData(0, [])
            self.update_code_preview()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ide = PixCodeIDE()
    ide.show()
    sys.exit(app.exec_())
