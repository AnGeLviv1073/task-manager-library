import json

class TaskSerializer:
    def __init__(self, task_manager):
        """Inicializa el serializador con una instancia de TaskManager."""
        self.task_manager = task_manager

    def save_tasks_to_file(self, filename):
        """Guarda las tareas en un archivo JSON."""
        with open(filename, "w") as file:
            json.dump(self.task_manager.tasks, file)
        return True

    def load_tasks_from_file(self, filename):
        """Carga tareas desde un archivo JSON."""
        with open(filename, "r") as file:
            self.task_manager.tasks = json.load(file)
        return True
