'Tapered basket: symmetric sides, a clear handle and a single clean rim.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e0c6d19-547e-46f0-8ec6-c837972fb3f0'
SOURCE_PATH = 'pictographic-primitives/state/trash_5e0c6d19-547e-46f0-8ec6-c837972fb3f0.svg'
AUTHOR = 'gpt-6'

class TrashState(Solo48):
    icon_id = 'trash-state'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('trash', 'state')

    def build(self):
        # Tapered basket: symmetric sides, a clear handle and a single clean rim.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('body',(8,16),(12,42),(36,42),(40,16))
        l('rim',(6,16),(42,16))
        p('handle',(16,16),(16,6),(32,6),(32,16))
        link('connect','body','rim')
        link('connect','handle','rim')
