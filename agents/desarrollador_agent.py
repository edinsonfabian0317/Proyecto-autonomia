from base_agent import BaseAgent

class DesarrolladorAgent(BaseAgent):
    def execute(self):
        print(f"[{self.name}] - Operando activamente con la identidad de Desarrollador.")
        if "Desarrollador" != "CEO":
            self.send("Valentino-CEO", "Reporte de Desarrollador: Módulos y componentes del sistema estables.")

if __name__ == '__main__':
    agent = DesarrolladorAgent("Mariana-Desarrollador")
    agent.run()
    agent.execute()
