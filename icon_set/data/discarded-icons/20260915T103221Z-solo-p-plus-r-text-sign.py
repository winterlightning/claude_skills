"""P plus r text sign; independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '672045df-37a3-5dc6-a6d4-80e71269be1b'
SOURCE_PATH = 'pictographic-primitives/transportation/park and ride_672045df-37a3-5dc6-a6d4-80e71269be1b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'SOURCE_ICON_ID': '672045df-37a3-5dc6-a6d4-80e71269be1b', 'SOURCE_PATH': 'pictographic-primitives/transportation/park and ride_672045df-37a3-5dc6-a6d4-80e71269be1b.svg', 'AUTHOR': 'gpt-6'}]

class PPlusRTextSign(Solo48):
    icon_id = 'p-plus-r-text-sign'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('p', 'plus', 'r', 'text', 'sign')

    def build(self) -> None:
        # HRECT_L centerline (6,8)-(42,40). P and R share their bowl construction.
        for name,x in [('p',4),('r',36)]:
            self.add_line(name+'-stem',(x,40),(x,24))
            self.add_line(name+'-upright',(x,24),(x,8))
            self.add_arc(name+'-bowl',(x,8),(x,24),radius_x=8)
            self.add_contour(name+'-loop',name+'-upright',name+'-bowl',closed=True)
            self.relate('connect',name+'-stem',name+'-loop')
        self.add_line('r-leg',(36,24),(42,40))
        self.relate('connect','r-leg','r-loop')
        self.relate('connect','r-leg','r-stem')
        self.add_polyline('plus-bar',(21,24),(24,24),(27,24))
        self.add_polyline('plus-stem',(24,19),(24,24),(24,29))
        self.relate('connect','plus-bar','plus-stem')
