"""Fried Egg in Frying Pan."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3ddff631-620c-4c4c-8ee1-e6f8d0e88303'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/fried egg pan_3ddff631-620c-4c4c-8ee1-e6f8d0e88303.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fried-egg-in-round-pan'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('egg', 'frying pan', 'yolk', 'breakfast', 'cooking', 'food', 'skillet')

    def build(self):
        # Plan: Top-view frying pan with irregular egg white and central yolk dot. Lucide egg-fried nested curves. Short solid handle replaces narrow outline. Envelope (6,6)-(42,42).
        self.add_bezier('pan',(24,6),((34,6),(42,14),(42,24)),((42,34),(34,42),(24,42)),((19,42),(15,39),(12,36)),((8,32),(6,29),(6,24)),((6,14),(14,6),(24,6)))
        self.add_contour('skillet','pan',closed=True)
        self.add_line('handle',(12,36),(6,42));self.relate('connect','handle','skillet')
        self.add_bezier('white',(24,15),((29,15),(33,19),(33,24)),((33,30),(28,33),(24,33)),((20,33),(15,29),(15,24)),((15,20),(20,15),(24,15)))
        self.add_contour('egg','white',closed=True);self.add_dot('yolk',(24,24))
