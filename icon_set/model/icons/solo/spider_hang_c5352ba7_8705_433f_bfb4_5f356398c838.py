from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5352ba7-8705-433f-bfb4-5f356398c838'
SOURCE_PATH = 'pictographic-primitives/animals/spider hang_c5352ba7-8705-433f-bfb4-5f356398c838.svg'
AUTHOR = 'gpt-6'


class HangingSpider(Solo48):
    icon_id = 'hanging-spider'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('spider', 'thread', 'hanging', 'web', 'arachnid', 'legs', 'halloween', 'drop')

    def build(self) -> None:
        # Thread and oval body with four leg pairs; extremes (5,2)-(43,46).
        self.add_arc('cap-top', (18, 22), (30, 22), radius_x=6, radius_y=8, sweep=True)
        self.add_line('side-r1', (30, 22), (30, 29))
        self.add_line('side-r2', (30, 29), (30, 36))
        self.add_arc('cap-base', (30, 36), (18, 36), radius_x=6, radius_y=6, sweep=True)
        self.add_line('side-l1', (18, 36), (18, 29))
        self.add_line('side-l2', (18, 29), (18, 22))
        self.add_contour('body', 'cap-top', 'side-r1', 'side-r2', 'cap-base', 'side-l1', 'side-l2', closed=True)
        self.add_line('thread', (24, 2), (24, 14))
        self.relate("connect", "thread", "body")
        self.add_line('l-upper-1', (18, 22), (9, 19))
        self.add_line('l-upper-2', (9, 19), (8, 11))
        self.add_contour('l-upper', 'l-upper-1', 'l-upper-2', closed=False)
        self.add_line('l-middle-1', (18, 29), (5, 26))
        self.add_contour('l-middle', 'l-middle-1', closed=False)
        self.add_line('l-lower-1', (18, 36), (9, 36))
        self.add_line('l-lower-2', (9, 36), (5, 41))
        self.add_contour('l-lower', 'l-lower-1', 'l-lower-2', closed=False)
        self.add_line('l-bottom-1', (18, 36), (15, 46))
        self.add_contour('l-bottom', 'l-bottom-1', closed=False)
        self.add_line('r-upper-1', (30, 22), (39, 19))
        self.add_line('r-upper-2', (39, 19), (40, 11))
        self.add_contour('r-upper', 'r-upper-1', 'r-upper-2', closed=False)
        self.add_line('r-middle-1', (30, 29), (43, 26))
        self.add_contour('r-middle', 'r-middle-1', closed=False)
        self.add_line('r-lower-1', (30, 36), (39, 36))
        self.add_line('r-lower-2', (39, 36), (43, 41))
        self.add_contour('r-lower', 'r-lower-1', 'r-lower-2', closed=False)
        self.add_line('r-bottom-1', (30, 36), (33, 46))
        self.add_contour('r-bottom', 'r-bottom-1', closed=False)
        self.relate("connect", 'body', 'l-upper')
        self.relate("connect", 'body', 'l-middle')
        self.relate("connect", 'body', 'l-lower')
        self.relate("connect", 'body', 'l-bottom')
        self.relate("connect", 'body', 'r-upper')
        self.relate("connect", 'body', 'r-middle')
        self.relate("connect", 'body', 'r-lower')
        self.relate("connect", 'body', 'r-bottom')
        self.relate("connect", 'l-lower', 'l-bottom')
        self.relate("connect", 'r-lower', 'r-bottom')
