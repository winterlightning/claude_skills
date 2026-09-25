"""Agricultural Seed Planter Machine.
Plan: Mirrored tapered hoppers share a top support; central stems above and below. Extrema (4,8)-(44,40).
Reference: Original source silhouette; Lucide geometric construction with shared joints and coherent curves.
Reduction: Narrow double rims reduced to one top edge; two equal hoppers and stems retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'db6cc599-13eb-44e2-ab18-835632658080'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/seeder_db6cc599-13eb-44e2-ab18-835632658080.svg'
AUTHOR = 'gpt-6'

class Batch27Icon(Solo48):
    icon_id = 'twin-hopper-seed-planter'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    aliases = ()
    keywords = ('agricultural', 'seed', 'planter', 'machine')

    def build(self):

        self.add_polyline('support',(4,8),(12,8),(36,8),(44,8))
        for i,x in enumerate((12,36)):
            self.add_line(f'stem-{i}',(x,8),(x,16))
            self.add_polyline(f'hopper-{i}',(x,16),(x+8,16),(x+5,32),(x,32),(x-5,32),(x-8,16),(x,16))
            self.add_line(f'tube-{i}',(x,32),(x,40))
            self.relate('connect','support',f'stem-{i}')
            self.relate('connect',f'stem-{i}',f'hopper-{i}')
            self.relate('connect',f'tube-{i}',f'hopper-{i}')
