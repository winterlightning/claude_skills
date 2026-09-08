from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '380869ce-057f-4cbf-be51-92de0ec1f4e3'
SOURCE_PATH = 'pictographic-primitives/animals/spider_380869ce-057f-4cbf-be51-92de0ec1f4e3.svg'
AUTHOR = 'gpt-6'


class SpiderOnThread(Solo48):
    icon_id = 'spider-on-thread'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('spider', 'thread', 'web', 'arachnid', 'legs', 'hanging', 'halloween', 'bug')

    def build(self) -> None:
        # Round abdomen and smaller head with six legs; extremes (2,2)-(46,46).
        self.add_arc('body0', (14, 26), (24, 16), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('body1', (24, 16), (34, 26), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('body2', (34, 26), (24, 36), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('body3', (24, 36), (14, 26), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('body', 'body0', 'body1', 'body2', 'body3', closed=True)
        self.add_arc('head0', (19, 41), (24, 36), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('head1', (24, 36), (29, 41), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('head2', (29, 41), (24, 46), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('head3', (24, 46), (19, 41), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('head', 'head0', 'head1', 'head2', 'head3', closed=True)
        self.add_line('thread', (24, 2), (24, 16))
        self.add_line('l-upper-1', (14, 26), (8, 18))
        self.add_line('l-upper-2', (8, 18), (2, 20))
        self.add_contour('l-upper', 'l-upper-1', 'l-upper-2', closed=False)
        self.add_line('l-middle-1', (14, 26), (2, 29))
        self.add_contour('l-middle', 'l-middle-1', closed=False)
        self.add_line('l-lower-1', (24, 36), (10, 37))
        self.add_line('l-lower-2', (10, 37), (6, 43))
        self.add_contour('l-lower', 'l-lower-1', 'l-lower-2', closed=False)
        self.add_line('r-upper-1', (34, 26), (40, 18))
        self.add_line('r-upper-2', (40, 18), (46, 20))
        self.add_contour('r-upper', 'r-upper-1', 'r-upper-2', closed=False)
        self.add_line('r-middle-1', (34, 26), (46, 29))
        self.add_contour('r-middle', 'r-middle-1', closed=False)
        self.add_line('r-lower-1', (24, 36), (38, 37))
        self.add_line('r-lower-2', (38, 37), (42, 43))
        self.add_contour('r-lower', 'r-lower-1', 'r-lower-2', closed=False)
        self.relate("connect", 'body', 'head')
        self.relate("connect", 'body', 'thread')
        self.relate("connect", 'body', 'l-upper')
        self.relate("connect", 'body', 'l-middle')
        self.relate("connect", 'body', 'l-lower')
        self.relate("connect", 'body', 'r-upper')
        self.relate("connect", 'body', 'r-middle')
        self.relate("connect", 'body', 'r-lower')
        self.relate("connect", 'head', 'l-lower')
        self.relate("connect", 'head', 'r-lower')
        self.relate("connect", 'l-upper', 'l-middle')
        self.relate("connect", 'l-lower', 'r-lower')
        self.relate("connect", 'r-upper', 'r-middle')
