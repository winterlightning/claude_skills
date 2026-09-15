"""Make the knife’s exposed blade a coherent curved cutting edge instead of a broken polygon, keeping the contact tip fixed on the surface.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f10240f2-3d0b-4bbc-84f3-32d2004d4495'
SOURCE_PATH = 'pictographic-primitives/tools/scratch resistance_f10240f2-3d0b-4bbc-84f3-32d2004d4495.svg'
AUTHOR = 'gpt-6'

class KnifeScratchingSurface(Solo48):
    icon_id = 'knife-scratching-surface-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('scratch', 'resistance', 'knife', 'surface', 'durability', 'hardness', 'test', 'blade')

    def build(self) -> None:
        self.add_polyline('knife-spine', (16, 42), (26, 16), (30, 6), (40, 10), (36, 20))
        self.add_bezier('cutting-edge', (36, 20), ((32, 31), (24, 40), (16, 42)))
        self.relate('connect', 'knife-spine', 'cutting-edge')
        self.add_line('handle-seam', (26, 16), (36, 20))
        self.relate('connect', 'handle-seam', 'knife-spine')
        self.add_polyline('surface', (6, 42), (16, 42), (42, 42))
        self.relate('connect', 'knife-spine', 'surface')
        self.add_line('scratch-left', (6, 28), (10, 32))
        self.add_line('scratch-right', (40, 32), (42, 30))
    variant_of = 'knife-scratching-surface'
    variant_label = 'Batch 01 centerline repair'
