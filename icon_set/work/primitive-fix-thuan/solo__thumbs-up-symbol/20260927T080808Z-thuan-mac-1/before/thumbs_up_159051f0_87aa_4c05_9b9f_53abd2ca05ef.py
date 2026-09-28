'Thumbs-up: broad cuff, clean thumb silhouette and smooth finger and palm curves.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '159051f0-87aa-4c05-9b9f-53abd2ca05ef'
SOURCE_PATH = 'pictographic-primitives/symbol/thumbs up_159051f0-87aa-4c05-9b9f-53abd2ca05ef.svg'
AUTHOR = 'gpt-6'

class ThumbsUpSymbol(Solo48):
    icon_id = 'thumbs-up-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('thumbs', 'up', 'symbol')

    def build(self):
        # Thumbs-up: broad cuff, clean thumb silhouette and smooth finger and palm curves.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('cuff',(6,24),(14,24),(14,42),(6,42),(6,24))
        p('thumb',(14,24),(22,14),(22,6),(32,6),(34,12),(30,22),(36,22))
        a('fingers',(36,22),(42,28),6)
        l('right',(42,28),(42,34))
        a('palm',(42,34),(34,42),8)
        l('bottom',(34,42),(14,42))
        link('connect','cuff','thumb')
        link('connect','thumb','fingers')
        link('connect','fingers','right')
        link('connect','right','palm')
        link('connect','palm','bottom')
        link('connect','bottom','cuff')
