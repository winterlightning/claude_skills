"""Agricultural Seeder Machine.
Plan: Tall tapered hopper over two vertical wheels and spreading wings. Extrema (4,8)-(44,40).
Reference: Original source silhouette; Lucide geometric construction with shared joints and coherent curves.
Reduction: Two rounded vertical tires and two falling seed strokes retained; nested body panels omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47fb874d-74a6-4cd9-9941-61fa6301ee2a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/seeder_47fb874d-74a6-4cd9-9941-61fa6301ee2a.svg'
AUTHOR = 'gpt-6'

class Batch27Icon(Solo48):
    icon_id = 'seed-spreader-with-two-wheels'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    aliases = ()
    keywords = ('agricultural', 'seeder', 'machine')

    def build(self):

        self.add_polyline('hopper',(16,24),(17,8),(31,8),(32,24))
        self.add_polyline('wings',(4,29),(16,24),(24,24),(32,24),(44,29))
        self.relate('connect','hopper','wings')
        for i,x in enumerate((16,32)):
            self.add_arc(f'wheel-{i}-a',(x,24),(x+4,28),radius_x=4)
            self.add_line(f'wheel-{i}-b',(x+4,28),(x+4,36))
            self.add_arc(f'wheel-{i}-c',(x+4,36),(x-4,36),radius_x=4)
            self.add_line(f'wheel-{i}-d',(x-4,36),(x-4,28))
            self.add_arc(f'wheel-{i}-e',(x-4,28),(x,24),radius_x=4)
            self.add_contour(f'wheel-{i}',*[f'wheel-{i}-{a}' for a in 'abcde'],closed=True)
            self.relate('connect','wings',f'wheel-{i}');self.relate('connect','hopper',f'wheel-{i}')
        for i,x in enumerate((4,44)):self.add_line(f'seed-{i}',(x,38),(x,40))
