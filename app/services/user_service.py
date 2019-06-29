from django.utils import timezone

from .note_service import NoteService
from app.utils import setup_cursor


class UserService:
    """
    Service to manage db users
    """
    def __init__(self):
        # db users
        self.cursor = setup_cursor().users

        if self.cursor is None:
            return

    def get_list_users(self):
        return self.cursor.user.find()

    def get_user(self, user_id):
        return self.__get_user_ref(user_id)

    def __get_user_ref(self, user_id):
        return self.cursor.user.find_one({'email': user_id})

    def create_user(self, data=dict()):
        data['date_joined'] = timezone.now().isoformat()
        self.cursor.user.insert_one(data)
        return True

    def delete_user(self, user_id):
        self.cursor.user.delete_one({'email': user_id})
        return True

    def update_user(self, user_id, data):
        self.cursor.user.update_one({'email': user_id}, {
            '$set': {
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'email': data['email'],
                'age': data['age'],
                'sex': data['sex'],
            }
        })
        return True

    def detail_user(self, user_id):
        note_service = NoteService()
        notes = note_service.get_notes_by_user(user_id)
        context = dict(user=self.__get_user_ref(user_id), notes=notes)
        return context
