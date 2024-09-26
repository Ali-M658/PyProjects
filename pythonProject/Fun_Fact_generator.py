import requests as rq
import json
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact():
    clear()
    put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )

    url = 'https://uselessfacts.jsph.pl/api/v2/facts/random?language=en'
    response = rq.get(url)
    data = json.loads(response.text)

    useless_fact = data['text']

    style(put_text(useless_fact), 'color:red; font-size: 30px')
    put_buttons(
        [dict(label='Click this button', value='outline-success', color='Outline-success')],
        onclick=get_fun_fact
    )

if __name__ == '__main__':  # Corrected line
    put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )
    put_buttons(
        [dict(label='Click this button', value='outline-success', color='Outline-success')],
        onclick=get_fun_fact
    )
    hold()
