"""Burning Fire Torch."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c793c630-04f7-5b74-b01d-96741e815d08'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/torch_c793c630-04f7-5b74-b01d-96741e815d08.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'torch-with-tall-flame'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    categories = ('fire', 'primitives')
    aliases = ()
    keywords = ('torch', 'flame', 'fire', 'handle', 'bowl', 'light', 'burning')

    def build(self):
        # Plan: Centered handle and bowl support asymmetric tall flame. Lucide flame suggests coherent curved silhouette. Interior tongue omitted to preserve air. Bounds (10,4)-(38,44).
        self.add_bezier('flame',(17,18),((14,14),(23,10),(23,4)),((28,7),(30,11),(29,15)),((32,16),(36,14),(38,13)),((38,15),(37,17),(35,18)))
        self.add_polyline('bowl',(10,27),(14,33),(24,33),(34,33),(38,27))
        self.add_line('handle',(24,33),(24,44))
        self.relate('connect','handle','bowl')
