from base_agent import BaseAgent

class EvaluadorAgent(BaseAgent):
    def execute(self):
        print(f"[{self.name}] - Operando activamente con la identidad de Evaluador.")
        if "Evaluador" != "CEO":
            self.send("Valentino-CEO", "Reporte de Evaluador: Criterios de evaluación y rendimiento listos.")

if __name__ == '__main__':
    agent = EvaluadorAgent("Santiago-Evaluador")
    agent.run()
    agent.execute()
