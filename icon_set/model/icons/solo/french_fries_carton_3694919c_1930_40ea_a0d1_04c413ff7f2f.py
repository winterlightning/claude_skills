"""Box of French Fries."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3694919c-1930-40ea-a0d1-04c413ff7f2f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/french fries_3694919c-1930-40ea-a0d1-04c413ff7f2f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'french-fries-carton'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('fries', 'potato', 'carton', 'fast food', 'takeaway', 'snack', 'food')

    def build(self):
        # Plan: Repeated fries in stepped silhouette joined to scooped carton. Shared eight-unit fry pitch. No exact Lucide match. Envelope (8,4)-(40,44).
        self.add_polyline('fries',(8,24),(8,10),(16,10),(16,4),(24,4),(24,8),(32,8),(32,12),(40,12),(40,24))
        self.add_bezier('scoop',(8,24),((10,26),(13,28),(16,28)),((19,28),(21,30),(24,30)),((27,30),(29,28),(32,28)),((35,28),(38,26),(40,24)))
        self.add_polyline('carton',(40,24),(40,32),(36,44),(12,44),(8,32),(8,24))
        for a,b in (('fries','scoop'),('carton','scoop'),('fries','carton')):self.relate('connect',a,b)
        for x,t,b in ((16,10,28),(24,8,30),(32,12,28)):
         self.add_line(f'fry-{x}',(x,t),(x,b));self.relate('connect',f'fry-{x}','fries');self.relate('connect',f'fry-{x}','scoop')
