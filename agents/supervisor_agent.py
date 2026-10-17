from base_agent import BaseAgent

class SupervisorAgent(BaseAgent):
    def execute(self):
        print(f"[{self.name}] - Operando activamente con la identidad de Supervisor.")
        if "Supervisor" != "CEO":
            self.send("Valentino-CEO", "Reporte de Supervisor: Monitoreo de estado y métricas de salud en marcha.")

if __name__ == '__main__':
    agent = SupervisorAgent("Valeria-Supervisor")
    agent.run()
    agent.execute()
