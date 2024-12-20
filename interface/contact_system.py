from abc import abstractmethod

class ContactSystem:
    @abstractmethod
    def send_message(self, recipient, message):
        pass