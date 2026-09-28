"""Six round nodes form a hexagon joined by straight edges, with a triangle inscribed inside connecting alternate nodes.

Plan: Six-junction hexagon and inscribed triangle share three integer vertices.
Keyshape: VRECT_L; exact SOLO48 envelope from the contract.
Construction reference: hexagon: shared polygon vertices.
Simplification: Six outlined node circles reduce to rounded junctions; all six vertices and triangle retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '53680e18-332e-4f0c-8465-a0817408951d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__graphql-logo/20260927T055712Z-thuan-mac-1/reference/graphql logo_53680e18-332e-4f0c-8465-a0817408951d.svg'
AUTHOR = "gpt-6"


class GraphqlLogo(Solo48):
    icon_id = 'graphql-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('graphql', 'api', 'query', 'hexagon', 'logo', 'brand', 'developer')

    def build(self) -> None:
        # Six joint dots on the hexagon and its defining inner triangle.
        pts=[(24,4),(40,14),(40,34),(24,44),(8,34),(8,14)]
        self.add_polyline('hexagon',*pts,closed=True)
        self.add_polyline('triangle',pts[0],pts[2],pts[4],closed=True)
        self.relate('connect','hexagon','triangle')
        for j,p in enumerate(pts):
            self.add_dot(f'node-{j}',p)
            self.relate('connect',f'node-{j}','hexagon')
            if j in (0,2,4):self.relate('connect',f'node-{j}','triangle')
