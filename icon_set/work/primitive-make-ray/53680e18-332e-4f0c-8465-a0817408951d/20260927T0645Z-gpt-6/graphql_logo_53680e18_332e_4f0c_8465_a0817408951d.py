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
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('graphql', 'api', 'query', 'hexagon', 'logo', 'brand', 'developer')

    def build(self) -> None:
        # Six solid junctions and the hexagonal GraphQL ring.
        points=[(24,8),(40,16),(40,32),(24,40),(8,32),(8,16)]
        for j,a in enumerate(points):
            b=points[(j+1)%6]
            self.add_line(f'edge-{j}',a,b)
        for j in (2,4):
            name=f'cross-{j}'
            self.add_line(name,points[0],points[j])
            self.relate('connect',name,'edge-0')
            self.relate('connect',name,'edge-5')
            self.relate('connect',name,f'edge-{j}')
            self.relate('connect',name,f'edge-{(j-1)%6}')
        for j,(x,y) in enumerate(points):
            h=f'node-{j}-h';v=f'node-{j}-v'
            self.add_line(h,(x-2,y),(x+2,y))
            self.add_line(v,(x,y-2),(x,y+2))
            self.relate('connect',h,v)
            for edge in (f'edge-{j}',f'edge-{(j-1)%6}'):
                self.relate('connect',h,edge)
                self.relate('connect',v,edge)
