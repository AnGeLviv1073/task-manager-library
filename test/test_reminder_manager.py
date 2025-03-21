import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from task_manager import TaskManager, ReminderManager


class TaskReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas y Recordatorios")
        self.root.geometry("600x400")

        # Inicializar los gestores de tareas y recordatorios
        self.tm = TaskManager()
        self.rm = ReminderManager()

        # Crear widgets
        self.create_widgets()

    def create_widgets(self):
        # Título
        self.title_label = tk.Label(self.root, text="Gestor de Tareas y Recordatorios", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Frame para la lista de tareas
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack()

        # Botón para agregar tarea
        self.add_task_button = tk.Button(self.root, text="Agregar Tarea", command=self.add_task)
        self.add_task_button.pack(pady=10)

        # Botón para mostrar tareas
        self.show_tasks_button = tk.Button(self.root, text="Mostrar Tareas", command=self.show_tasks)
        self.show_tasks_button.pack(pady=5)

        # Lista para mostrar tareas
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Frame para los recordatorios
        self.reminder_frame = tk.Frame(self.root)
        self.reminder_frame.pack(pady=10)

        # Botón para agregar recordatorio
        self.set_reminder_button = tk.Button(self.root, text="Agregar Recordatorio", command=self.set_reminder)
        self.set_reminder_button.pack(pady=10)

    def add_task(self):
        def save_task():
            title = title_entry.get()
            description = description_entry.get()
            priority = int(priority_entry.get())
            due_date_str = due_date_entry.get()

            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                task = self.tm.add_task(title, description, priority, due_date)
                messagebox.showinfo("Éxito", f"Tarea '{title}' añadida exitosamente.")
                add_task_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "La fecha de vencimiento debe estar en formato 'YYYY-MM-DD'.")

        # Ventana emergente para agregar tarea
        add_task_window = tk.Toplevel(self.root)
        add_task_window.title("Agregar Tarea")

        # Campos para la tarea
        tk.Label(add_task_window, text="Título:").pack()
        title_entry = tk.Entry(add_task_window)
        title_entry.pack(pady=5)

        tk.Label(add_task_window, text="Descripción:").pack()
        description_entry = tk.Entry(add_task_window)
        description_entry.pack(pady=5)

        tk.Label(add_task_window, text="Prioridad (1-5):").pack()
        priority_entry = tk.Entry(add_task_window)
        priority_entry.pack(pady=5)

        tk.Label(add_task_window, text="Fecha de vencimiento (YYYY-MM-DD):").pack()
        due_date_entry = tk.Entry(add_task_window)
        due_date_entry.pack(pady=5)

        # Botón para guardar tarea
        save_button = tk.Button(add_task_window, text="Guardar", command=save_task)
        save_button.pack(pady=10)

    def show_tasks(self):
        self.task_listbox.delete(0, tk.END)
        tasks = self.tm.list_tasks()
        for task in tasks:
            due_date = task["due_date"].strftime("%Y-%m-%d")
            self.task_listbox.insert(tk.END, f"{task['title']} - {due_date} - Prioridad: {task['priority']}")

    def set_reminder(self):
        def save_reminder():
            task_id = int(task_id_entry.get())
            reminder_date_str = reminder_date_entry.get()

            try:
                reminder_date = datetime.strptime(reminder_date_str, "%Y-%m-%d %H:%M")
                if self.rm.set_reminder(task_id, reminder_date):
                    messagebox.showinfo("Éxito", f"Recordatorio para tarea ID {task_id} añadido.")
                    set_reminder_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "La fecha del recordatorio debe estar en formato 'YYYY-MM-DD HH:MM'.")

        # Ventana emergente para agregar recordatorio
        set_reminder_window = tk.Toplevel(self.root)
        set_reminder_window.title("Agregar Recordatorio")

        # Campos para el recordatorio
        tk.Label(set_reminder_window, text="ID de tarea:").pack()
        task_id_entry = tk.Entry(set_reminder_window)
        task_id_entry.pack(pady=5)

        tk.Label(set_reminder_window, text="Fecha del recordatorio (YYYY-MM-DD HH:MM):").pack()
        reminder_date_entry = tk.Entry(set_reminder_window)
        reminder_date_entry.pack(pady=5)

        # Botón para guardar recordatorio
        save_button = tk.Button(set_reminder_window, text="Guardar", command=save_reminder)
        save_button.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskReminderApp(root)
    root.mainloop()
