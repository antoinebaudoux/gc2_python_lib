# Python Module example
import requests


def update_lesson_status(user, lesson, progress):
    data = {'user': user, 'lesson': lesson, 'progress': progress}
    response = requests.post('https://hook.eu1.make.com/lw29fl3xmh32z7975lmhrroceywmvrw2', data=data)
    print(response)
