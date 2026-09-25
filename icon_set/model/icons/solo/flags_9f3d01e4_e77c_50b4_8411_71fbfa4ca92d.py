'Flags: straight fabric edges and a balanced trailing flag with an open overlap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f3d01e4-e77c-50b4-8411-71fbfa4ca92d'
SOURCE_PATH = 'pictographic-primitives/social/flags_9f3d01e4-e77c-50b4-8411-71fbfa4ca92d.svg'
AUTHOR = 'gpt-6'

class Flags(Solo48):
    icon_id = 'flags'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    categories = ('social', 'primitives')
    aliases = ()
    keywords = ('flags', 'social')

    def build(self):
        # Flags: straight fabric edges and a balanced trailing flag with an open overlap.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        l('pole',(6,6),(6,42))
        p('front',(6,10),(30,10),(30,28),(6,28))
        p('back',(30,18),(42,18),(38,28),(42,38),(18,38),(18,28))
        link('connect','pole','front')
        link('connect','front','back')
