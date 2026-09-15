'Cog: symmetric broad teeth and a centered axle replace uneven micro-segments.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1e82d117-570c-41ee-9217-7031427f5fea'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cog_1e82d117-570c-41ee-9217-7031427f5fea.svg'
AUTHOR = 'gpt-6'

class Cog(Solo48):
    icon_id = 'cog'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cog', 'interface-essential')

    def build(self):
        # Cog: symmetric broad teeth and a centered axle replace uneven micro-segments.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        # Six broad teeth leave open valleys; opposite points share the centre.
        points=[(20,6),(28,6),(30,14),(38,12),(42,20),(36,26),
                (42,32),(38,40),(30,38),(28,42),(20,42),(18,38),
                (10,40),(6,32),(12,26),(6,20),(10,12),(18,14),(20,6)]
        p('gear',*points)
        self.add_dot('axle',(24,24))
