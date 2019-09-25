from kivy.logger import Logger
from pypercard import Inputs, Card, CardApp


costs = {
    'stone': 10,
    'food': 10,
    'product': 10,
    'window': 10,
}

state = {
    'hair': 100,
    'strength': 0,
    'contentment': 50,
    'tower': 0,
    'funds': 0,
    'rapunzel': 0,
    'time': 0,
}


def move(data_store, form_value):
    Logger.info(f'Rapunzel: {data_store}')

    data_store['tower'] += form_value
    data_store['time'] += 1
    data_store['hair'] -= 10

    # the prince shows up at the beginning of the week
    if data_store['time'] >= 52:
        return 'TimeRanOut'

    if data_store['tower'] >= 100:
        return 'TowerFinished'
    if data_store['hair'] <= 0:
        return 'Hairpocalypse'
    return 'Move'


def end(data_store, form_value):
    app.stop()


app = CardApp(name='Rapunzel, Rapunzel …', data_store=state, stack=[
    Card(
        'TheStorySoFar',
        text='Parents, blah, salad, foo …',
        buttons=[{'label': 'Next', 'target': 'Move'}],
    ),
    Card(
        'Move',
        text='Build me a tower!\nCompletion: {tower}%',
        form=Inputs.SLIDER,
        options=(0, 10, 1),
        buttons=[{'label': 'Next', 'target': move}],
    ),
    Card(
        'TowerFinished',
        text='The tower is built, Rapunzel is safe.',
        buttons=[{'label': 'Yay?', 'target': 'Thanks'}],
    ),
    Card(
        'Hairpocalypse',
        text='Life is pointless.',
        buttons=[{'label': '…', 'target': 'Thanks'}],
    ),
    Card(
        'TimeRanOut',
        text='Oh noes! The prince came and married Rapunzel.',
        buttons=[{'label': 'o.O', 'target': 'Thanks'}],
    ),
    Card(
        'Thanks',
        text='Thank you for playing\nRapunzel, Rapunzel',
        buttons=[{'label': 'Bye!', 'target': end}],
    ),
])

app.run()
