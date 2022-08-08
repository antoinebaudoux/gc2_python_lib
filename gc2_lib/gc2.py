# Python Module example
import requests


def update_lesson_status():
    """This program adds two
    numbers and return the result"""
    response = requests.post('https://hook.eu1.make.com/lw29fl3xmh32z7975lmhrroceywmvrw2', data={'key': 'value'})
