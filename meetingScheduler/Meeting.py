from datetime import datetime
import User
import MeetingRoom


class Meeting:
    def __init__(self, meeting_id: int,meeting_start_time: datetime, meeting_end_time: datetime,organizer: User, attendees: list, meeting_room: MeetingRoom) -> None:
        self.meeting_id = meeting_id
        self.meeting_start_time = meeting_start_time
        self.meeting_end_time = meeting_end_time
        self.organizer = organizer
        self.attendees = attendees
        self.meeting_room = meeting_room

    def getOrganizer(self):
        return self.organizer

    def getAttendees(self):
        return self.attendees

