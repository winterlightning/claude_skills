"A large ear curves around a smaller folded inner contour. A compact hearing aid rests behind its right edge, with a thin curved tube following the ear's outer rim.\n\nConstruction: Ear outline with an external hearing-aid capsule. The inner fold is reduced to one open hook. Bounds (8,4)-(40,44).\nLucide: ear: upper bowl and smaller lobule form a continuous contour."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a5990fb-162b-412c-8e3a-8627f5051f07'
SOURCE_PATH = 'pictographic-primitives/wayfinding/disability hearing aid_7a5990fb-162b-412c-8e3a-8627f5051f07.svg'
AUTHOR = 'gpt-6'

class EarWithHearingAid(Solo48):
    icon_id = 'ear-with-hearing-aid'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('ear', 'hearing', 'aid', 'accessibility', 'audio', 'device')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('ear-top', (8, 16), (32, 16), radius_x=12, radius_y=12, large_arc=False, sweep=True)
        self.add_line('ear-side', (32, 16), (32, 27))
        self.add_arc('ear-lower', (32, 27), (22, 37), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('lobule', (22, 37), (8, 37), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('fold', (17, 18), (23, 24), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('fold-tail', (23, 24), (17, 30))
        self.add_line('aid-1', (32, 16), (40, 16))
        self.add_line('aid-2', (40, 16), (40, 29))
        self.add_line('aid-3', (40, 29), (32, 29))
        self.add_contour('ear', 'ear-top', 'ear-side', 'ear-lower', 'lobule', closed=False)
        self.add_contour('inner-ear', 'fold', 'fold-tail', closed=False)
        self.add_contour('aid', 'aid-1', 'aid-2', 'aid-3', closed=False)
        self.relate('connect', 'aid', 'ear')
