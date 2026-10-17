from base_agent import BaseAgent

class OptimizadorAgent(BaseAgent):
    def execute(self):
        print(f"[{self.name}] - Operando activamente con la identidad de Optimizador.")
        if "Optimizador" != "CEO":
            self.send("Valentino-CEO", "Reporte de Optimizador: Ajustes de rendimiento asignados a los nodos.")

if __name__ == '__main__':
    agent = OptimizadorAgent("Lucía-Optimizador")
    agent.run()
    agent.execute()
