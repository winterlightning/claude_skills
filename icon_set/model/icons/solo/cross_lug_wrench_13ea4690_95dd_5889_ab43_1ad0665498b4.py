"""A four-way lug wrench with open socket cups. Lucide wrench informed spare tool geometry. Square keyshape supports four equal arms; hub circle and tiny socket slots reduced to shared junctions and open mouths."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13ea4690-95dd-5889-ab43-1ad0665498b4'
SOURCE_PATH = 'pictographic-primitives/transportation/car tool lug wrench_13ea4690-95dd-5889-ab43-1ad0665498b4.svg'
SOURCE_REFERENCES = (('13ea4690-95dd-5889-ab43-1ad0665498b4', 'pictographic-primitives/transportation/car tool lug wrench_13ea4690-95dd-5889-ab43-1ad0665498b4.svg'),)
AUTHOR = 'gpt-6'

class CrossLugWrench(Solo48):
    icon_id = 'cross-lug-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('lug wrench', 'wrench', 'cross wrench', 'tool', 'tyre', 'wheel', 'repair', 'mechanic')

    def build(self) -> None:
        self.add_polyline('vertical',(24,14),(24,24),(24,34))
        self.add_polyline('horizontal',(14,24),(24,24),(34,24))
        self.relate('connect','vertical','horizontal')
        for name,pts,bar in [('top',[(20,6),(20,14),(24,14),(28,14),(28,6)],'vertical'),('bottom',[(20,42),(20,34),(24,34),(28,34),(28,42)],'vertical'),('left',[(6,20),(14,20),(14,24),(14,28),(6,28)],'horizontal'),('right',[(42,20),(34,20),(34,24),(34,28),(42,28)],'horizontal')]:
            self.add_polyline(name,*pts)
            self.relate('connect',name,bar)
