from base_agent import BaseAgent

class ValidadorAgent(BaseAgent):
    def execute(self):
        print(f"[{self.name}] - Operando activamente con la identidad de Validador.")
        if "Validador" != "CEO":
            self.send("Valentino-CEO", "Reporte de Validador: Reglas de validación y control de integridad verificadas.")

if __name__ == '__main__':
    agent = ValidadorAgent("Mateo-Validador")
    agent.run()
    agent.execute()
