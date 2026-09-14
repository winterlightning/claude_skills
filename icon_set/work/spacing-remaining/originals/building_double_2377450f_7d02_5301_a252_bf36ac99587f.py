'Two buildings: consistent verticals, an 8-unit doorway and aligned foundation.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2377450f-7d02-5301-a252-bf36ac99587f'
SOURCE_PATH = 'icons-json/office/building double_2377450f-7d02-5301-a252-bf36ac99587f.json'
AUTHOR = 'gpt-6'

class BuildingDouble(Solo48):
    icon_id = 'building-double'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('building', 'double', 'office')

    def build(self):
        # Two buildings: consistent verticals, an 8-unit doorway and aligned foundation.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('main',(6,42),(6,6),(30,6),(30,42),(6,42))
        p('annex',(30,22),(42,22),(42,42),(30,42))
        link('connect','annex','main')
        for x in (14,22):
            l(f'window-{x}',(x,14),(x,18))
        p('door',(14,42),(14,30),(22,30),(22,42))
        link('connect','door','main')
