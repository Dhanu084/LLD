from User import User
def Notification(mode: bool, organizer: User, attendees: list) -> bool:
    if mode:
        attendees_emails = [attendee.getEmail() for attendee in attendees]
        print(f'Sending success mail to {organizer.getEmail()}')
        print(attendees_emails)
        
    else:
        print(f'Sending failure mail to {organizer.getEmail()}')

