from base_agent import BaseAgent

class EstrategaAgent(BaseAgent):
    def execute(self):
        print(f"[{self.name}] - Operando activamente con la identidad de Estratega.")
        if "Estratega" != "CEO":
            self.send("Valentino-CEO", "Reporte de Estratega: Estrategia general sincronizada con la visión directiva.")

if __name__ == '__main__':
    agent = EstrategaAgent("Isabella-Estratega")
    agent.run()
    agent.execute()
