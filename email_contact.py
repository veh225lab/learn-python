from abc import ABC

from interface.contact_system import ContactSystem


class EmailContact(ContactSystem):
    def send_message(self, recipient, message):
        print(f'Sending email to {recipient}: {message}')