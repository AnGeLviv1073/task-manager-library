from datetime import datetime

class ReminderManager:
    def __init__(self):
        """Inicializa el gestor de recordatorios."""
        self.reminders = {}

    def set_reminder(self, task_id, reminder_date):
        """Establece un recordatorio para una tarea."""
        if not isinstance(reminder_date, datetime):
            raise ValueError("La fecha del recordatorio debe ser un objeto datetime")

        self.reminders[task_id] = reminder_date
        return True

    def remove_reminder(self, task_id):
        """Elimina el recordatorio para una tarea."""
        if task_id in self.reminders:
            del self.reminders[task_id]
            return True
        raise KeyError(f"No hay recordatorio para la tarea con ID {task_id}")

    def list_reminders(self):
        """Lista todos los recordatorios activos."""
        return self.reminders
