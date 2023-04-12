![logo_kami](assets/icon.png){width="384" .center}

# Kami Messenger

Kami Messenger is a tool for aggregating several messaging platforms into a single package in order to facilitate the task of sending mass messages.

It contains three main classes for this purpose:

- Message(A single message that contains a list of recipients to send);
- Contact(A single contact with a list of addresses for different messaging platforms);
- Messenger(An object that instantiates, connects, and provides message push service of a specific platform)