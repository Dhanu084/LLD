from Observable.Observer import Observer
from Observers.EmailObserver import EmailObserver
from Observers.MobileNotifier import MobileNotifier

if __name__== "__main__":
    em_notify1 = EmailObserver()
    mob_notify1 = MobileNotifier()
    observer = Observer()
    observer.add(em_notify1)
    observer.add(mob_notify1)
    em_notify2 = EmailObserver()
    mob_notify2 = MobileNotifier()
    observer.add(em_notify2)
    observer.add(mob_notify2)
    observer.notify()
