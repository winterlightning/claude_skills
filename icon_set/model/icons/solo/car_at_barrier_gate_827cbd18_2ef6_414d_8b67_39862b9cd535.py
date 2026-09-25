"""Car at barrier gate; independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '827cbd18-2ef6-414d-8b67-39862b9cd535'
SOURCE_PATH = 'pictographic-primitives/transportation/parking ramp 1_827cbd18-2ef6-414d-8b67-39862b9cd535.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'SOURCE_ICON_ID': '827cbd18-2ef6-414d-8b67-39862b9cd535', 'SOURCE_PATH': 'pictographic-primitives/transportation/parking ramp 1_827cbd18-2ef6-414d-8b67-39862b9cd535.svg', 'AUTHOR': 'gpt-6'}]

class CarAtBarrierGate(Solo48):
    icon_id = 'car-at-barrier-gate'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'at', 'barrier', 'gate')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42). A compact front-view car beside its raised physical barrier.
        self.add_polyline('car-body',(6,30),(28,30),(28,38),(24,38),(10,38),(6,38),closed=True)
        self.add_polyline('windscreen',(6,30),(11,20),(23,20),(28,30))
        self.relate('connect','car-body','windscreen')
        for name,x in [('left',10),('right',24)]:
            self.add_line(name+'-tire',(x,38),(x,42))
            self.relate('connect',name+'-tire','car-body')
        self.add_line('barrier-post',(42,42),(42,22))
        self.add_line('boom',(42,22),(18,6))
        self.relate('connect','boom','barrier-post')
