import unittest
from multithreading import perform_tasks, monitor_tasks

class MultithreadingTests(unittest.TestCase):

    def test_concurrent_task_execution(self):
        self.assertEqual(perform_tasks(), 5050)

    def test_monitoring_during_task_execution(self):
        self.assertIsNone(monitor_tasks())

if __name__ == '__main__':
    unittest.main()
