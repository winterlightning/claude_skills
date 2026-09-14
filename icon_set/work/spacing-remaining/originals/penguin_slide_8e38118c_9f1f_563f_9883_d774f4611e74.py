"""Belly-sliding penguin with a domed head, eye, pointed beak, flipper and trailing feet. Lucide bird informs rounded head and wing construction. Deliberately faces down-right along a shallow slope for recognition."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e38118c-9f1f-563f-9883-d774f4611e74'
SOURCE_PATH = 'pictographic-primitives/animals/penguin slide_8e38118c-9f1f-563f-9883-d774f4611e74.svg'
AUTHOR = 'gpt-6'


class SlidingPenguin(Solo48):
    icon_id = 'sliding-penguin'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('penguin', 'slide', 'sliding', 'snow', 'slope', 'ice', 'antarctic', 'motion')

    def build(self) -> None:
        # SQUARE centerline extremes: (6,6)-(42,42).
        # Rounded back and separate domed head make the belly-down bird explicit.
        self.add_arc('rump', (6, 14), (14, 6), radius_x=8, radius_y=8)
        self.add_arc('back', (14, 6), (26, 18), radius_x=12, radius_y=12)
        self.add_arc('head-front', (26, 18), (42, 18), radius_x=8, radius_y=8)
        self.add_line('bill-top', (42, 18), (42, 24))
        self.add_line('bill-bottom', (42, 24), (38, 28))
        self.add_arc('belly-front', (38, 28), (22, 30), radius_x=20, radius_y=12)
        self.add_arc('belly-back', (22, 30), (6, 14), radius_x=16, radius_y=16)
        self.add_contour('body', 'rump', 'back', 'head-front', 'bill-top',
                         'bill-bottom', 'belly-front', 'belly-back', closed=True)
        self.add_line('foot-upper', (14, 6), (6, 6))
        self.add_line('foot-lower', (6, 14), (6, 8))
        self.relate('connect', 'body', 'foot-upper')
        self.relate('connect', 'body', 'foot-lower')
        self.add_dot('eye', (34, 19))
        self.add_line('flipper', (15, 16), (20, 22))
        self.add_line('slope', (6, 34), (42, 42))
