from base_agent import BaseAgent

class InvestigadorAgent(BaseAgent):
    def execute(self):
        print(f"[{self.name}] - Operando activamente con la identidad de Investigador.")
        if "Investigador" != "CEO":
            self.send("Valentino-CEO", "Reporte de Investigador: Recolectando datos contextualmente relevantes.")

if __name__ == '__main__':
    agent = InvestigadorAgent("Lucas-Investigador")
    agent.run()
    agent.execute()
