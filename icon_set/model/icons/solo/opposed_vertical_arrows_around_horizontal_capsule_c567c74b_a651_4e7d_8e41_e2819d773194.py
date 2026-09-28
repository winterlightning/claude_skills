"""Vertical Compression Arrows.

Symbol plan: One compression diagram: capsule with detached mirrored inward arrows. Capsule owns its semicircular ends; arrows share x=24 and reflect around y=24.
Keyshape SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c567c74b-a651-4e7d-8e41-e2819d773194'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/shorten horizontal_c567c74b-a651-4e7d-8e41-e2819d773194.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'opposed-vertical-arrows-around-horizontal-capsule'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('vertical', 'compression', 'arrows')

    def build(self):
        self.rect('capsule',6,20,36,8,4)
        for i in range(2):
            def point(x,y):return (x,y if i==0 else 48-y)
            self.graph([(f'shaft-{i}',point(24,6),point(24,11)),(f'left-{i}',point(18,6),point(24,11)),(f'right-{i}',point(24,11),point(30,6))])

    def rect(self,name,x,y,w,h,r=2):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,start in enumerate(points):
            end=points[(i+1)%8];part=f'{name}-{i}'
            if start==end: continue
            if i%2:self.add_arc(part,start,end,radius_x=r)
            else:self.add_line(part,start,end)
            names.append(part)
        self.add_contour(name,*names,closed=True)

    def graph(self,edges):
        for name,a,b in edges:self.add_line(name,a,b)
        for i,(name,a,b) in enumerate(edges):
            for other,c,d in edges[i+1:]:
                if {a,b}&{c,d}:self.relate('connect',name,other)
