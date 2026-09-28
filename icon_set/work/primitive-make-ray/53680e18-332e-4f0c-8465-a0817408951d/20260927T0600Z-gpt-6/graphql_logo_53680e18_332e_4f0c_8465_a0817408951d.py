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
AUTHOR = 'gpt-6'


class GraphqlLogo(Solo48):
    icon_id = 'graphql-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('graphql', 'api', 'query', 'hexagon', 'logo', 'brand', 'developer')

    def build(self) -> None:
        # Six branded nodes, hexagonal perimeter and the triangular cross links.
        pts=[(24,9),(39,17),(39,31),(24,39),(9,31),(9,17)]
        for j,a in enumerate(pts):
            b=pts[(j+1)%6]
            self.add_line(f'edge-{j}',a,b)
        self.add_line('cross-left',pts[0],pts[4])
        self.add_line('cross-right',pts[0],pts[2])
        self.add_line('cross-base',pts[4],pts[2])
        for j,(x,y) in enumerate(pts):
            self.add_arc(f'node-{j}-a',(x-3,y),(x+3,y),radius_x=3)
            self.add_arc(f'node-{j}-b',(x+3,y),(x-3,y),radius_x=3)
            self.add_contour(f'node-{j}',f'node-{j}-a',f'node-{j}-b',closed=True)
            for edge in (f'edge-{j}',f'edge-{(j-1)%6}'):
                self.relate('connect',f'node-{j}',edge)
        for name,a,b in [('cross-left',0,4),('cross-right',0,2),('cross-base',4,2)]:
            self.relate('connect',name,f'node-{a}')
            self.relate('connect',name,f'node-{b}')
