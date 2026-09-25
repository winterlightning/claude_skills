"""Vector Shape Anchor Points.

Symbol plan: Four equal circular nodes form an irregular quadrilateral. All edge endpoints are cardinal node points; vertical sides and deliberately sloping top/bottom retained.
Keyshape SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a726d668-4a98-4e99-93a4-32413dcb13b2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/vectors anchor rectangle_a726d668-4a98-4e99-93a4-32413dcb13b2.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'quadrilateral-vector-path-with-round-anchor-nodes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('vector', 'shape', 'anchor', 'points')

    def build(self):
        nodes=[(10,10),(38,14),(38,34),(10,38)]
        for i,(x,y) in enumerate(nodes):self.circle(f'node-{i}',x,y,4)
        edges=[('top',(14,10),(34,14),0,1),('right',(38,18),(38,30),1,2),('bottom',(34,34),(14,38),2,3),('left',(10,34),(10,14),3,0)]
        for name,a,b,i,j in edges:
            self.add_line(name,a,b)
            for k in (i,j):self.relate('connect',name,f'node-{k}')

    def circle(self,name,cx,cy,r):
        points=[(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        names=[]
        for i,start in enumerate(points):
            part=f'{name}-{i}';self.add_arc(part,start,points[(i+1)%4],radius_x=r);names.append(part)
        self.add_contour(name,*names,closed=True)
