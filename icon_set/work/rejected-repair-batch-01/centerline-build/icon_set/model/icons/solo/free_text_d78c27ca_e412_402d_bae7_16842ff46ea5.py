'FREE lettering: regular aligned letter stems, with compact but consistent counters.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd78c27ca-e412-402d-bae7-16842ff46ea5'
SOURCE_PATH = 'pictographic-primitives/symbol/free (text)_d78c27ca-e412-402d-bae7-16842ff46ea5.svg'
AUTHOR = 'gpt-6'


class FreeText(Solo48):
    icon_id = 'free-text'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('free', 'label', 'no-cost', 'offer', 'promotion', 'badge', 'text', 'gratis')

    def build(self):
        # FREE lettering: equal 16-unit letter heights and 8-unit spacing between each horizontal stroke.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('f',(8,20),(8,4),(18,4))
        l('f-bar',(8,12),(16,12))
        link('connect','f','f-bar')
        p('r',(30,20),(30,4),(40,4),(40,12),(30,12),(40,20))
        for x in (8,30):
            p(f'e-{x}',(x+10,28),(x,28),(x,44),(x+10,44))
            l(f'bar-{x}',(x,36),(x+8,36))
            link('connect',f'e-{x}',f'bar-{x}')
