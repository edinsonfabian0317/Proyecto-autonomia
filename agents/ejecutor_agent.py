from base_agent import BaseAgent

class EjecutorAgent(BaseAgent):
    def execute(self):
        print(f"[{self.name}] - Operando activamente con la identidad de Ejecutor.")
        if "Ejecutor" != "CEO":
            self.send("Valentino-CEO", "Reporte de Ejecutor: Tareas del sistema listas para procesamiento continuo.")

if __name__ == '__main__':
    agent = EjecutorAgent("Camila-Ejecutor")
    agent.run()
    agent.execute()
