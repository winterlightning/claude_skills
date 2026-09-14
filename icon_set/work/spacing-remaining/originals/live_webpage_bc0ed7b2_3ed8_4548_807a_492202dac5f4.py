'LIVE webpage: upright evenly spaced lettering above a simple browser baseline.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc0ed7b2-3ed8-4548-807a-492202dac5f4'
SOURCE_PATH = 'pictographic-primitives/websites/webpage live_bc0ed7b2-3ed8-4548-807a-492202dac5f4.svg'
AUTHOR = 'gpt-6'


class LiveWebpage(Solo48):
    icon_id = 'live-webpage'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface'
    aliases = ()
    keywords = ('live', 'webpage', 'broadcast', 'text', 'website', 'page', 'streaming')

    def build(self):
        # LIVE webpage: upright evenly spaced lettering above a simple browser baseline.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('l',(4,8),(4,24),(10,24))
        l('i',(18,8),(18,24))
        p('v',(26,8),(30,24),(34,8))
        p('e',(44,8),(42,8),(42,24),(44,24))
        l('e-bar',(42,16),(44,16))
        link('connect','e','e-bar')
        p('page',(4,32),(4,40),(44,40),(44,32))
        l('page-line',(14,32),(34,32))
