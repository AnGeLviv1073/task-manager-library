import unittest
from task_manager.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tm = TaskManager()

    def test_add_task(self):
        task = self.tm.add_task("Estudiar", "Preparar para examen", 2, "2025-03-20")
        self.assertEqual(task["title"], "Estudiar")

    def test_edit_task(self):
        self.tm.add_task("Leer", "Leer libro", 1, "2025-03-21")
        self.tm.edit_task(1, title="Leer novela")
        self.assertEqual(self.tm.tasks[0]["title"], "Leer novela")

    def test_delete_task(self):
        self.tm.add_task("Ejercicio", "Hacer ejercicio", 3, "2025-03-22")
        self.tm.delete_task(1)
        self.assertEqual(len(self.tm.tasks), 0)

if __name__ == "__main__":
    unittest.main()
