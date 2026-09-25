"""Six matching circular nodes sit at the corners of a hexagonal ring, joined by short straight bonds. The arrangement is evenly spaced around a large open central area.

VRECT_XL visible extremes (6,2)-(42,46); six repeated circular atoms around an open center. Lucide chart-network informed nodes and bonds. All six atoms retained; symmetric structure.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f3c217e-f110-4527-83a4-e1b1e349f29d'
SOURCE_PATH = 'pictographic-primitives/science/cells_9f3c217e-f110-4527-83a4-e1b1e349f29d.svg'
AUTHOR = 'gpt-6'

class SixNodeMolecularRing(Solo48):
    icon_id = 'six-node-molecular-ring'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    categories = ("science", "primitives")
    aliases = ()
    keywords = ('molecule', 'ring', 'node', 'bond', 'chemistry', 'structure')

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        nodes=[(24,7),(37,16),(37,32),(24,41),(11,32),(11,16)]
        for i,(x,y) in enumerate(nodes):
            self.circle(f'atom-{i}',x,y,3)
        for i in range(6):
            x,y=nodes[i];u,v=nodes[(i+1)%6]
            if x==u:
                a=(x,y+3 if v>y else y-3); b=(u,v-3 if v>y else v+3)
            else:
                a=(x+3 if u>x else x-3,y); b=(u-3 if u>x else u+3,v)
            self.add_line(f'bond-{i}',a,b)
            self.relate('connect',f'bond-{i}',f'atom-{i}')
            self.relate('connect',f'bond-{i}',f'atom-{(i+1)%6}')
