'Whale tail with spout: preserve the curved rising back and forked fluke; exact SQUARE silhouette and an open spray.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0260567b-c418-4fea-8c5b-1928bc8c2566'
SOURCE_PATH = 'pictographic-primitives/animals/whale water_0260567b-c418-4fea-8c5b-1928bc8c2566.svg'
AUTHOR = 'gpt-6'


class WhaleTailWithSpout(Solo48):
    icon_id = 'whale-tail-with-spout'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('whale', 'tail', 'spout', 'water', 'sea', 'ocean', 'marine', 'minimal')

    def build(self) -> None:
        self.add_bezier('head',(6,42),((6,37),(10,31),(14,31)))
        self.add_bezier('back',(14,31),((20,31),(22,36),(27,36)),((32,36),(33,31),(33,25)))
        self.add_bezier('fluke-left',(33,25),((29,22),(27,18),(27,14)))
        self.add_polyline('notch',(27,14),(35,18),(42,14))
        self.add_bezier('fluke-right',(42,14),((42,18),(42,22),(42,25)))
        self.add_line('tail-stem',(42,25),(40,39))
        self.add_contour('whale-a','head','back','fluke-left')
        self.add_contour('whale-b','fluke-right','tail-stem')
        self.relate('connect','notch','whale-a')
        self.relate('connect','notch','whale-b')
        self.add_bezier('spray-left',(6,14),((6,11),(8,10),(10,14)))
        self.add_arc('spray-right',(10,14),(18,14),radius_x=4,radius_y=8)
        self.add_contour('spray','spray-left','spray-right')
        self.add_line('spout',(10,14),(10,23))
        self.relate('connect','spray','spout')
