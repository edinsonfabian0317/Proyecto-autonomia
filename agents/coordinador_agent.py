from base_agent import BaseAgent

class CoordinadorAgent(BaseAgent):
    def execute(self):
        print(f"[{self.name}] - Operando activamente con la identidad de Coordinador.")
        if "Coordinador" != "CEO":
            self.send("Valentino-CEO", "Reporte de Coordinador: Flujos de trabajo inter-agentes alineados.")

if __name__ == '__main__':
    agent = CoordinadorAgent("Alejandro-Coordinador")
    agent.run()
    agent.execute()
