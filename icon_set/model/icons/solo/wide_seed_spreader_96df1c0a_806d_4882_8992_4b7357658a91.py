"""Agricultural Seed Spreader Machine.
Plan: Mirrored upper hopper meets a wide peaked spreading bar and splayed feet. Extrema (4,8)-(44,40).
Reference: Original source silhouette; Lucide geometric construction with shared joints and coherent curves.
Reduction: Nested body panel and narrow center tab reduced to a single raised spreading bar.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96df1c0a-806d-4882-8992-4b7357658a91'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/seeder_96df1c0a-806d-4882-8992-4b7357658a91.svg'
AUTHOR = 'gpt-6'

class Batch27Icon(Solo48):
    icon_id = 'wide-seed-spreader'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    aliases = ()
    keywords = ('agricultural', 'seed', 'spreader', 'machine')

    def build(self):

        self.add_polyline('hopper',(12,26),(16,8),(32,8),(36,26))
        self.add_polyline('bar',(4,30),(12,26),(24,23),(36,26),(44,30),(44,38),(34,38),(14,38),(4,38),(4,30))
        self.relate('connect','hopper','bar')
        for i,x in enumerate((14,34)):
            self.add_line(f'foot-{i}',(x,38),(x-2 if i==0 else x+2,40));self.relate('connect','bar',f'foot-{i}')
