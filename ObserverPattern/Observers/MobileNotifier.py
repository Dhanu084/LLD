from Observers.IObserver import IObserver

class MobileNotifier(IObserver):

    def notify(self):
        print("Notifiying to mobile")