from base_agent import BaseAgent

class WorkerAgent(BaseAgent):
    def work(self, task):
        print(f"[{self.name}] - Ejecutando tarea asignada: {task}")

if __name__ == "__main__":
    worker = WorkerAgent("Dante-Worker-01")
    worker.run()
    worker.work("Procesamiento de datos del sistema")
