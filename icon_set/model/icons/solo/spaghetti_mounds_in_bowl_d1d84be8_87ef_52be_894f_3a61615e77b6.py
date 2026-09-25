"""Bowl of Spaghetti Noodles."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd1d84be8-87ef-52be-894f-3a61615e77b6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/pasta bowl_d1d84be8-87ef-52be-894f-3a61615e77b6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spaghetti-mounds-in-bowl'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('spaghetti', 'noodle', 'pasta', 'bowl', 'meal', 'food', 'serving')

    def build(self):
        # Plan: Three overlapping pasta mounds in shallow bowl. Lucide salad; tiny nested strokes removed. Natural asymmetric mounds, wide envelope (4,8)-(44,40).
        self.add_polyline('rim',(4,28),(24,28),(44,28))
        self.add_bezier('bowl',(44,28),((44,36),(38,40),(32,40)))
        self.add_line('base',(32,40),(16,40))
        self.add_bezier('left',(16,40),((10,40),(4,36),(4,28)))
        self.relate('connect','rim','bowl');self.relate('connect','bowl','base');self.relate('connect','base','left');self.relate('connect','left','rim')
        self.add_bezier('mound-l',(4,28),((4,20),(9,16),(14,16)),((19,16),(24,21),(24,28)))
        self.add_bezier('mound-r',(24,28),((24,18),(29,14),(34,14)),((40,14),(44,20),(44,28)))
        self.add_bezier('back',(14,16),((14,12),(17,8),(24,8)),((29,8),(32,10),(34,14)))
        for name in ('mound-l','mound-r'):self.relate('connect',name,'rim');self.relate('connect',name,'back')
        self.relate('connect','mound-l','mound-r')
