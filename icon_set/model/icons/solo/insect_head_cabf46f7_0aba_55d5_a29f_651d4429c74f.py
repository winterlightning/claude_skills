"""Ant face; centerline extremes (8,2)-(40,46). Mirrored long antennae and circular eyes; broad mouth block retained. Oval eyes simplified to small circles for clear holes. Lucide bug informs symmetric arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cabf46f7-0aba-55d5-a29f-651d4429c74f'
SOURCE_PATH = 'pictographic-primitives/animals/insect head_cabf46f7-0aba-55d5-a29f-651d4429c74f.svg'
AUTHOR = 'gpt-6'


class AntHead(Solo48):
    icon_id = 'ant-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('ant', 'insect', 'head', 'face', 'antennae', 'eyes', 'bug', 'mandible')

    def build(self) -> None:
        # Ant face; centerline extremes (8,2)-(40,46). Mirrored long antennae and circular eyes; broad mouth block retained. Oval eyes simplified to small circles for clear holes. Lucide bug informs symmetric arcs.
        self.add_arc('brow-left', (14, 27), (20, 18), radius_x=6, radius_y=9, sweep=True)
        self.add_line('brow-top', (20, 18), (28, 18))
        self.add_arc('brow-right', (28, 18), (34, 27), radius_x=6, radius_y=9, sweep=True)
        self.add_line('cheek-right', (34, 27), (34, 34))
        self.add_arc('jaw-right', (34, 34), (29, 39), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('jaw-left', (19, 39), (14, 34), radius_x=5, radius_y=5, sweep=True)
        self.add_line('cheek-left', (14, 34), (14, 27))
        self.add_line('mouth-bottom-1', (29, 39), (29, 46))
        self.add_line('mouth-bottom-2', (29, 46), (19, 46))
        self.add_line('mouth-bottom-3', (19, 46), (19, 39))
        self.add_contour('face', 'brow-left', 'brow-top', 'brow-right', 'cheek-right', 'jaw-right', 'mouth-bottom-1', 'mouth-bottom-2', 'mouth-bottom-3', 'jaw-left', 'cheek-left', closed=True)
        self.add_polyline('antenna-left', (20, 18), (20, 8), (14, 2), closed=False)
        self.relate("connect", 'face', 'antenna-left')
        self.add_arc('eye-left-0', (11, 24), (14, 27), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('eye-left-1', (14, 27), (11, 30), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('eye-left-2', (11, 30), (8, 27), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('eye-left-3', (8, 27), (11, 24), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('eye-left', 'eye-left-0', 'eye-left-1', 'eye-left-2', 'eye-left-3', closed=True)
        self.relate("connect", 'face', 'eye-left')
        self.add_polyline('antenna-right', (28, 18), (28, 8), (34, 2), closed=False)
        self.relate("connect", 'face', 'antenna-right')
        self.add_arc('eye-right-0', (37, 24), (40, 27), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('eye-right-1', (40, 27), (37, 30), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('eye-right-2', (37, 30), (34, 27), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('eye-right-3', (34, 27), (37, 24), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('eye-right', 'eye-right-0', 'eye-right-1', 'eye-right-2', 'eye-right-3', closed=True)
        self.relate("connect", 'face', 'eye-right')
        self.add_polyline('mouth', (19, 39), (19, 34), (29, 34), (29, 39), closed=False)
        self.relate("connect", 'mouth', 'face')
