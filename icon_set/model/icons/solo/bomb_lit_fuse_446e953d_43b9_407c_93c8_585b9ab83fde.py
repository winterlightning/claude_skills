"""Bomb with Lit Fuse. Reduces the jagged burst to three broad spark rays and merges the short neck into the diagonal fuse.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide bomb: round body and diagonal fuse attachment; supplied reference determines lit spark.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '446e953d-43b9-407c-93c8-585b9ab83fde'
SOURCE_PATH = 'pictographic-primitives/symbol/boom_446e953d-43b9-407c-93c8-585b9ab83fde.svg'
AUTHOR = 'gpt-6'


class BombLitFuse(Solo48):
    icon_id = 'bomb-lit-fuse'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('bomb', 'boom', 'explosion', 'fuse', 'blast', 'danger', 'detonate', 'spark')

    def build(self) -> None:
        self.add_arc('body-a', (22, 24), (16, 42), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('body-b', (16, 42), (6, 32), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('body-c', (6, 32), (22, 24), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('body', 'body-a', 'body-b', 'body-c', closed=True)
        self.add_line('fuse', (22, 24), (32, 14))
        self.relate("connect", 'body', 'fuse')
        self.add_polyline('spark', (26, 6), (32, 14), (38, 6))
        self.add_line('spark-right', (32, 14), (42, 18))
        self.relate("connect", 'spark', 'fuse')
        self.relate("connect", 'spark', 'spark-right')
        self.relate("connect", 'fuse', 'spark-right')
