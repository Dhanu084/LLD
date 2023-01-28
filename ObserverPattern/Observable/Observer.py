from Observers.IObserver import IObserver
class Observer:
    def __init__(self) -> None:
        self.observers = set()

    def add(self, observer: IObserver):
        self.observers.add(observer)
    
    def remove(self, observer:IObserver):
        self.observers.discard(observer)
    
    def notify(self):
        for observer in self.observers:
            observer.notify()