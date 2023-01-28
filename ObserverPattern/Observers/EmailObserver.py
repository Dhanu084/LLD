from Observers.IObserver import IObserver

class EmailObserver(IObserver):
    def notify(self):
        print("Notifying to email")
    