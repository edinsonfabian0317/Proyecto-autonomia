import time
from message_bus import MessageBus

class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.bus = MessageBus()

    def send(self, receiver, content):
        self.bus.send_message(self.name, receiver, content)
        print(f"[{self.name}] -> Mensaje enviado a {receiver}: {content}")

    def check_inbox(self):
        messages = self.bus.get_messages_for(self.name)
        for msg in messages:
            print(f"[{self.name}] Mensaje recibido de {msg['sender']}: {msg['content']}")

    def run(self):
        print(f"[{self.name}] - Nodo de agente activo y operando en la nube.")
        self.check_inbox()

    def execute(self):
        raise NotImplementedError("Cada agente debe implementar su propio método execute.")
