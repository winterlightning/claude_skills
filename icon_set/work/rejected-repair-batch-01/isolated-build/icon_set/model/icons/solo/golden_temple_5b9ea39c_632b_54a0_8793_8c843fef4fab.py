'Golden Temple with central pointed dome, corner spires and arched entrance. SQUARE centerlines (6,6)-(42,42). Small side domes reduced to spires and cornice bands omitted for clearance. Shared axis and sparse facade informed by Lucide landmark.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b9ea39c-632b-54a0-8793-8c843fef4fab'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/golden temple_5b9ea39c-632b-54a0-8793-8c843fef4fab.svg'
AUTHOR = 'gpt-6'

class GoldenTemple(Solo48):
    icon_id = 'golden-temple'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('golden temple', 'amritsar', 'india', 'sikh', 'gurdwara', 'dome', 'landmark', 'religion')

    def build(self) -> None:
        axis, left, right, bottom = 24, 6, 42, 42
        self.add_arc('dome-left',(axis,6),(16,24),radius_x=12,radius_y=15,sweep=False)
        self.add_arc('dome-right',(32,24),(axis,6),radius_x=12,radius_y=15,sweep=False)
        self.add_polyline('body',(left,24),(16,24),(32,24),(right,24),(right,bottom),(28,bottom),(20,bottom),(left,bottom),closed=True)
        for side,x in [('left',left),('right',right)]:
            self.add_line(side+'-spire',(x,14),(x,24))
            self.relate('connect',side+'-spire','body')
        self.add_line('door-left',(20,bottom),(20,37))
        self.add_arc('door-arch',(20,37),(28,37),radius_x=4,sweep=True)
        self.add_line('door-right',(28,37),(28,bottom))
        self.add_contour('door','door-left','door-arch','door-right')
        for a,b in [('dome-left','dome-right'),('dome-left','body'),('dome-right','body'),('body','door')]:
            self.relate('connect',a,b)
