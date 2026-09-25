'Two nestlings: equal rounded heads remain attached to the broad nest; omit undersized eyes that cannot clear the head outlines.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '86f74b9e-984f-4e95-959a-f8f27b3d1de8'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird nest_86f74b9e-984f-4e95-959a-f8f27b3d1de8.svg'
AUTHOR = 'gpt-6'

class BirdsInNest(Solo48):
    icon_id = 'birds-in-nest'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('nest', 'birds', 'chicks', 'baby', 'hatchling', 'nurture', 'home', 'family')

    def build(self) -> None:
        # Two chicks share the nest rim; tiny eyes are omitted because their heads cannot contain MIC4 detail.
        self.add_arc('bowl',(44,27),(4,27),radius_x=20,radius_y=13)
        self.add_polyline('rim',(4,27),(6,27),(20,27),(28,27),(42,27),(44,27))
        self.relate('connect','bowl','rim')
        for name,l,r in (('left',6,20),('right',28,42)):
            self.add_line(name+'-side-a',(l,27),(l,15))
            self.add_arc(name+'-head',(l,15),(r,15),radius_x=7)
            self.add_line(name+'-side-b',(r,15),(r,27))
            self.add_contour(name,name+'-side-a',name+'-head',name+'-side-b')
            self.relate('connect',name,'rim')
