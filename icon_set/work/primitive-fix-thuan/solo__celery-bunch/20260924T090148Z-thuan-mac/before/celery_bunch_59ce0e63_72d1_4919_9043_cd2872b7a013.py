"""Celery Stalk with Leaves."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59ce0e63-72d1-4919-9043-cd2872b7a013'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/celery_59ce0e63-72d1-4919-9043-cd2872b7a013.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'celery-bunch'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('celery', 'stalk', 'leaf', 'vegetable', 'bunch', 'produce', 'food')

    def build(self):
        # Plan: Diagonal stalk bunch with scalloped leafy crown. Lucide leafy-green, one internal stalk retained. Envelope (6,6)-(42,42).
        self.add_bezier('body',(14,16),((8,16),(8,8),(16,8)),((20,8),(22,10),(22,12)),((20,8),(22,6),(26,6)),((30,6),(32,9),(30,13)),((32,9),(37,9),(39,12)),((42,12),(42,14),(42,16)),((42,20),(39,22),(36,22)),((40,25),(37,30),(32,26)),((28,32),(23,42),(16,42)),((10,42),(6,39),(6,32)),((6,24),(11,21),(14,16)))
        self.add_contour('celery','body',closed=True)
        self.add_bezier('stalk',(16,42),((18,35),(21,31),(23,27)));self.relate('connect','stalk','celery')
