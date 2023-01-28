from Meeting import Meeting

class MeetingRoom:
    meetings = {}
    def __init__(self, meeting_room_id: int, meeting_room_name: str) -> None:
        self.meeting_room_id = meeting_room_id
        self.meeting_room_name = meeting_room_name
        

    @staticmethod
    def book_room(meeting_room_id: int,meeting: Meeting) -> bool:
        if meeting_room_id not in MeetingRoom.meetings.keys():
            MeetingRoom.meetings[meeting_room_id] = [meeting]
            return True

        can_allocate = False
        for current_meeting in MeetingRoom.meetings[meeting_room_id]:
            if current_meeting.meeting_end_time<meeting.meeting_start_time:
                MeetingRoom.meetings[meeting_room_id] = MeetingRoom.meetings[meeting_room_id].append(meeting)
                can_allocate = True
                break
        return can_allocate