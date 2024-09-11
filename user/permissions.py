
def is_author(self, CustomUser):
    username = self.kwargs.get('username')
    user_id = CustomUser.objects.get(username=username).id
    user_id2 = self.request.user.id
    print(user_id, user_id2)
    return user_id == user_id2