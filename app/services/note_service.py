from django.utils import timezone

from app.utils import setup_cursor


class NoteService:
    """
    Service to manage db notes
    """
    def __init__(self):
        # db notes
        self.cursor = setup_cursor().notes

        if self.cursor is None:
            return

    def create_note(self, user_id, data=dict()):
        data['user_id'] = user_id
        data['created_at'] = timezone.now().isoformat()
        self.cursor.note.insert_one(data)
        return True

    def get_notes_by_user(self, user_id):
        return self.cursor.note.find({'user_id': user_id})
