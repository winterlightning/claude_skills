"""Front-facing otter with round ears, eyes, broad nose and raised paws. Redrawn for recognition rather than preserving the ambiguous source arch. Paired anatomy is mirrored about x=24."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e348568-3af9-4250-a67d-883882fbc6e6'
SOURCE_PATH = 'pictographic-primitives/animals/otter_4e348568-3af9-4250-a67d-883882fbc6e6.svg'
AUTHOR = 'gpt-6'


class OtterWithPaws(Solo48):
    icon_id = 'otter-with-paws'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('otter', 'with', 'paws')

    def build(self) -> None:
        # SQUARE centerline extremes: (2,2)-(46,46).
        self.add_arc('ear-left',(6,8),(18,8),radius_x=6)
        self.add_line('crown',(18,8),(30,8))
        self.add_arc('ear-right',(30,8),(42,8),radius_x=6)
        self.add_arc('temple-right',(42,8),(46,20),radius_x=4,radius_y=12)
        self.add_arc('cheek-right',(46,20),(36,30),radius_x=10)
        self.add_contour('upper','ear-left','crown','ear-right','temple-right','cheek-right')
        self.add_arc('temple-left',(6,8),(2,20),radius_x=4,radius_y=12,sweep=False)
        self.add_arc('cheek-left',(2,20),(12,30),radius_x=10,sweep=False)
        self.add_contour('left','temple-left','cheek-left')
        self.relate('connect','upper','left')
        for side,cx in [('left',12),('right',36)]:
            self.add_arc(side+'-paw-right',(cx,30),(cx,46),radius_x=8)
            self.add_arc(side+'-paw-left',(cx,46),(cx,30),radius_x=8)
            self.add_contour(side+'-paw',side+'-paw-right',side+'-paw-left',closed=True)
            self.add_line(side+'-toe',(cx,40),(cx,46))
            self.relate('connect',side+'-paw',side+'-toe')
        self.relate('connect','upper','right-paw')
        self.relate('connect','left','left-paw')
        self.add_line('whisker-left',(2,20),(10,23))
        self.add_line('whisker-right',(46,20),(38,23))
        self.relate('connect','left','whisker-left')
        self.relate('connect','upper','whisker-right')
        self.add_dot('eye-left',(15,17))
        self.add_dot('eye-right',(33,17))
        self.add_polyline('nose',(22,23),(24,23),(26,23))
        self.add_line('mouth',(24,23),(24,29))
        self.relate('connect','nose','mouth')
