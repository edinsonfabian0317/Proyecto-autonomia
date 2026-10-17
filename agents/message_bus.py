import os
import json
from datetime import datetime

class MessageBus:
    def __init__(self, storage_dir="/app/agents/data"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)
        self.inbox_file = os.path.join(self.storage_dir, "messages.json")
        self._init_storage()

    def _init_storage(self):
        if not os.path.exists(self.inbox_file):
            with open(self.inbox_file, "w") as f:
                json.dump([], f)

    def send_message(self, sender, receiver, content):
        message = {
            "timestamp": datetime.now().isoformat(),
            "sender": sender,
            "receiver": receiver,
            "content": content
        }
        try:
            with open(self.inbox_file, "r+") as f:
                messages = json.load(f)
                messages.append(message)
                f.seek(0)
                json.dump(messages, f, indent=4)
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")

    def get_messages_for(self, receiver_name):
        if not os.path.exists(self.inbox_file):
            return []
        with open(self.inbox_file, "r") as f:
            messages = json.load(f)
        return [m for m in messages if m["receiver"] == receiver_name or m["receiver"] == "ALL"]
