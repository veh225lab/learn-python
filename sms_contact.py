from interface.contact_system import ContactSystem


class SmsContact(ContactSystem):
    def send_message(self, recipient, message):
        print(f'Sending sms to {recipient}: {message}')