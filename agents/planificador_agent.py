from base_agent import BaseAgent

class PlanificadorAgent(BaseAgent):
    def execute(self):
        print(f"[{self.name}] - Operando activamente con la identidad de Planificador.")
        if "Planificador" != "CEO":
            self.send("Valentino-CEO", "Reporte de Planificador: Planes de ejecución iniciales preparados para el ciclo actual.")

if __name__ == '__main__':
    agent = PlanificadorAgent("Sofía-Planificador")
    agent.run()
    agent.execute()
