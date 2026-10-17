from base_agent import BaseAgent

class AuditorAgent(BaseAgent):
    def execute(self):
        print(f"[{self.name}] - Operando activamente con la identidad de Auditor.")
        if "Auditor" != "CEO":
            self.send("Valentino-CEO", "Reporte de Auditor: Verificación de seguridad y registros sin anomalías.")

if __name__ == '__main__':
    agent = AuditorAgent("Daniel-Auditor")
    agent.run()
    agent.execute()
