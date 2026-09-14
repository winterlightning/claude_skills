"""A seated person faces right toward an open laptop, with a circular head and rounded shoulder. A bent arm rests at the keyboard while the angled screen rises from a flat base.
Lucide user and laptop construction. Seated body, circular head, bent arm and open screen retained. Facial detail and keyboard marks omitted; deliberate right-facing side view.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f8bbcf0f-7e74-456e-ae21-1dda0d706972'
SOURCE_PATH = 'pictographic-primitives/work/working remotely_f8bbcf0f-7e74-456e-ae21-1dda0d706972.svg'
AUTHOR = 'gpt-6'


class PersonUsingLaptop(Solo48):
    icon_id = 'person-using-laptop'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('person', 'laptop', 'computer', 'remote', 'work', 'seated')

    def build(self) -> None:
        self.add_arc('head-top', (9, 11), (19, 11), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (19, 11), (9, 11), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('shoulder', (14, 26), (6, 32), radius_x=8, radius_y=6, sweep=False, large_arc=False)
        self.add_line('back', (6, 32), (6, 36))
        self.add_arc('seat', (6, 36), (12, 42), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_line('base', (12, 42), (24, 42))
        self.add_contour('body', 'shoulder', 'back', 'seat', 'base', closed=False)
        self.add_polyline('laptop', (24, 42), (28, 30), (30, 24), (42, 24), (36, 42), closed=True)
        self.relate("connect", 'laptop', 'body')
        self.add_polyline('arm', (14, 26), (18, 30), (28, 30), closed=False)
        self.relate("connect", 'arm', 'body')
        self.relate("connect", 'arm', 'laptop')
