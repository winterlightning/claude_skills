"""Six round nodes form a hexagon joined by straight edges, with a triangle inscribed inside connecting alternate nodes.

Plan: Six-junction hexagon and inscribed triangle share three integer vertices.
Keyshape: VRECT_L; exact SOLO48 envelope from the contract.
Construction reference: hexagon: shared polygon vertices.
Simplification: Six outlined node circles reduce to rounded junctions; all six vertices and triangle retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53680e18-332e-4f0c-8465-a0817408951d'
SOURCE_PATH = 'pictographic-primitives/logos/graphql logo_53680e18-332e-4f0c-8465-a0817408951d.svg'
AUTHOR = 'gpt-6'


class GraphqlLogo(Solo48):
    icon_id = 'graphql-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('graphql', 'api', 'query', 'hexagon', 'logo', 'brand', 'developer')

    def build(self):
        top=(24,4); right_top=(40,14); right_bottom=(40,34)
        bottom=(24,44); left_bottom=(8,34); left_top=(8,14)
        self.add_polyline('hexagon',top,right_top,right_bottom,bottom,left_bottom,left_top,closed=True)
        self.add_polyline('triangle',top,right_bottom,left_bottom,closed=True)
        self.relate('connect','hexagon','triangle')
