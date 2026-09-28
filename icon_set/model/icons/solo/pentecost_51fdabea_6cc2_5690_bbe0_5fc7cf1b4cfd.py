'Pentecost dove: balanced wings and tail with broad open transitions and deliberate corners.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51fdabea-6cc2-5690-bbe0-5fc7cf1b4cfd'
SOURCE_PATH = 'pictographic-primitives/holidays/pentecost_51fdabea-6cc2-5690-bbe0-5fc7cf1b4cfd.svg'
AUTHOR = 'gpt-6'

class Pentecost(Solo48):
    icon_id = 'pentecost'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('pentecost', 'holidays')

    def build(self):
        # Pentecost dove: balanced wings and tail with broad open transitions and deliberate corners.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('dove',(6,22),(18,22),(14,6),(34,6),(30,22),(42,22),(36,32),(28,36),(24,42),(20,36),(12,32),(6,22))
