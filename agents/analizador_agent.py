from base_agent import BaseAgent

class AnalizadorAgent(BaseAgent):
    def __init__(self, name):
        super().__init__(name)

    def execute(self):
        print(f"[{self.name}] - CEO en funciones. Revisando buzón de entrada...")
        messages = self.bus.get_messages_for(self.name)
        if messages:
            print("\n===========================================================")
            print(f"=== REPORTES RECIBIDOS EN LA DIRECCIÓN ({len(messages)}) ===")
            for msg in messages:
                print(f"- [{msg['timestamp']}] De {msg['sender']}: {msg['content']}")
            print("===========================================================\n")
        else:
            print(f"[{self.name}] No hay nuevos reportes en la bandeja de entrada.")

if __name__ == "__main__":
    agent = AnalizadorAgent("Valentino-CEO")
    agent.run()
    agent.execute()
