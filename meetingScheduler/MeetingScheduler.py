
from datetime import datetime, timedelta
from MeetingRoom import MeetingRoom
from Meeting import Meeting
from User import User
from Notification import Notification


class MeetingSchedulerApp:

    def __init__(self) -> None:
        self.__rooms = []
    
    def add_room(self,room) -> bool:
        self.__rooms.append(room)

    def remove_room(self, room) -> bool:
        self.__rooms.remove(room)

    def book_room(self, meetingRoom):
        self.__rooms.append(meetingRoom)
    
    def schedule_room(self,meeting_room_id, meeting):
        return MeetingRoom.book_room(meeting_room_id, meeting)
    
    def getRooms(self):
        return self.__rooms

if __name__ == "__main__":
    meeting_scheduler = MeetingSchedulerApp()
    
    meeting_room1 = MeetingRoom(1, 'hall1')
    meeting_room2 = MeetingRoom(2, 'hall2')

    meeting_scheduler.add_room(meeting_room1)
    meeting_scheduler.add_room(meeting_room2)

    organizer1 = User(1, 'Dhanush', 'dhanuu@gmail.com')
    organizer2 = User(2, 'Monu', 'monuu@gmail.com')

    attendees = []
    for i in range(0,5):
        attendee = User(i+10, f'random{i}', f'random{i}@gmail.com')
        attendees.append(attendee)
    

    # for meetingRoom in meeting_scheduler.getRooms():
    #     print(meetingRoom.meeting_room_id, meetingRoom.meeting_room_name)

    meeting1 = Meeting(1, datetime.now(), datetime.now()+timedelta(minutes=60),organizer1, attendees, meeting_room1)
    meeting2 = Meeting(2, datetime.now(), datetime.now()+timedelta(minutes=60),organizer2, attendees, meeting_room2)
    
    booking_status = meeting_scheduler.schedule_room(meeting_room1.meeting_room_id,meeting1)
    Notification(booking_status, meeting1.getOrganizer(),meeting1.getAttendees())
    print('*'*20)

    booking_status = meeting_scheduler.schedule_room(meeting_room2.meeting_room_id,meeting2)
    Notification(booking_status, meeting2.getOrganizer(),meeting2.getAttendees())
    print('*'*20)

    meeting_conflict = Meeting(2, datetime.now(), datetime.now()+timedelta(minutes=60),organizer1, attendees, meeting_room1)
    booking_status = meeting_scheduler.schedule_room(meeting_room1.meeting_room_id, meeting_conflict)
    Notification(booking_status, meeting_conflict.getOrganizer(),meeting_conflict.getAttendees())
    print('*'*20)


    meeting_success = Meeting(3, datetime.now()+timedelta(minutes=60), datetime.now()+timedelta(minutes=120),organizer1, attendees, meeting_room1)
    booking_status = meeting_scheduler.schedule_room(meeting_room1.meeting_room_id, meeting_success)
    Notification(booking_status, meeting_success.getOrganizer(),meeting_success.getAttendees())
    # print('*'*20)

    