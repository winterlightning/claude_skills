"""Market Stall with Fruit.
Plan: Stall root owns a two-scallop canopy, posts and counter; two equal round fruits rest on the counter. Extrema (6,6)-(42,42).
Reference: Lucide store: repeating rounded awning sections.
Reduction: Four awning panels reduced to two; three fruits reduced to two; fruit stems retained, fine canopy stripes omitted for clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b645010b-c143-5fe2-bd8f-7dfe67267cd0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/farmers market kiosk_b645010b-c143-5fe2-bd8f-7dfe67267cd0.svg'
AUTHOR = 'gpt-6'


class Batch26Icon(Solo48):
    icon_id = 'fruit-market-stall'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    categories = ("primitives", "events")
    aliases = ()
    keywords = ('market', 'stall', 'with', 'fruit')

    def build(self):

        self.add_polyline('roof',(6,14),(10,6),(38,6),(42,14))
        for i,x in enumerate((6,24)):
            self.add_arc(f'scallop-{i}',(x,14),(x+18,14),radius_x=9,radius_y=4,sweep=False)
            self.relate('connect','roof',f'scallop-{i}')
        self.relate('connect','scallop-0','scallop-1')
        for side,x in (('left',6),('right',42)):
            self.add_polyline(f'post-{side}',(x,14),(x,37),(x,42))
            self.relate('connect',f'post-{side}','roof')
            self.relate('connect',f'post-{side}',f'scallop-{0 if side=="left" else 1}')
        self.add_polyline('counter',(6,37),(17,37),(31,37),(42,37))
        for side in ('left','right'):self.relate('connect','counter',f'post-{side}')
        for i,x in enumerate((17,31)):
            self.add_arc(f'fruit-{i}-a',(x,31),(x,37),radius_x=3)
            self.add_arc(f'fruit-{i}-b',(x,37),(x,31),radius_x=3)
            self.add_contour(f'fruit-{i}',f'fruit-{i}-a',f'fruit-{i}-b',closed=True)
            self.relate('connect','counter',f'fruit-{i}')
            self.add_line(f'stem-{i}',(x,31),(x+2,27))
            self.relate('connect',f'stem-{i}',f'fruit-{i}')
