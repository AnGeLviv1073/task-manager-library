class TaskManager:
    def __init__(self):
        """Inicializa el gestor de tareas con una lista vacía."""
        self.tasks = []
        self.task_id = 1

    def add_task(self, title, description, priority, due_date):
        """Agrega una nueva tarea a la lista."""
        task = {
            "id": self.task_id,
            "title": title,
            "description": description,
            "priority": priority,
            "due_date": due_date,
            "completed": False
        }
        self.tasks.append(task)
        self.task_id += 1
        return task

    def edit_task(self, task_id, **kwargs):
        """Edita una tarea existente si el ID es válido."""
        for task in self.tasks:
            if task["id"] == task_id:
                task.update(kwargs)
                return task
        raise KeyError(f"Tarea con ID {task_id} no encontrada")

    def delete_task(self, task_id):
        """Elimina una tarea por su ID."""
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        return True

    def list_tasks(self, sort_by="priority"):
        """Lista las tareas ordenadas por prioridad o fecha."""
        if sort_by == "priority":
            return sorted(self.tasks, key=lambda x: x["priority"])
        elif sort_by == "due_date":
            return sorted(self.tasks, key=lambda x: x["due_date"])
        return self.tasks
