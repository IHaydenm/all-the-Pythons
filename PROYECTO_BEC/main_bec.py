##SCREEN
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
class PyQtWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de materias.")
        self.setGeometry(100, 100, 1080, 1280)
        self.label = QLabel("Welcome,", self)
        self.button = QPushButton("Hellaw,", self)
        self.button.clicked.connect(self.on_click)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)
    def on_click(self):
        self.label.setText("A")

app = QApplication(sys.argv)
window = PyQtWindow()
window.show()
sys.exit(app.exec_())

##SCREEN

class UniversitySystem:
    def __init__(self): # CREANDO USUARIOS A PARTIR DE UN CONSTRUCTOR
        self.teachers = {}  # ESTO ES UN DICCIONARIO
    def add_user(self, username):
        if username in self.teachers:
            print(f"El maestro {username} ya se encuentra en el sistema.")
        else:
            self.teachers[username] = []
            print(f"User '{username}' added.")

    def register_course(self, username, course_name):
        if username not in self.teachers:
            print(f"User '{username}' does not exist.")
        else:
            if course_name in self.teachers[username]:
                print(f"User '{username}' is already registered in '{course_name}'.")
            else:
                self.teachers[username].append(course_name)
                print(f"Course '{course_name}' registered to user '{username}'.")

    def list_courses(self, username):
        if username not in self.teachers:
            print(f"User '{username}' does not exist.")
        else:
            courses = self.teachers[username]
            if courses:
                print(f"{username} is registered in: {', '.join(courses)}")
            else:
                print(f"{username} is not registered in any courses.")

    def list_users(self):
        if not self.teachers:
            print("No teachers registered yet.")
        else:
            print("Registered teachers:")
            for user in self.teachers:
                print(f"- {user}")
def main():
    uni_sys = UniversitySystem()

    while True:
        print("\n--- University Course Registration ---")
        print("1. Add User")
        print("2. Register Course")
        print("3. List User Courses")
        print("4. List All Users")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter username: ")
            uni_sys.add_user(name)
        elif choice == '2':
            name = input("Enter username: ")
            course = input("Enter course name: ")
            uni_sys.register_course(name, course)
        elif choice == '3':
            name = input("Enter username: ")
            uni_sys.list_courses(name)
        elif choice == '4':
            uni_sys.list_users()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
