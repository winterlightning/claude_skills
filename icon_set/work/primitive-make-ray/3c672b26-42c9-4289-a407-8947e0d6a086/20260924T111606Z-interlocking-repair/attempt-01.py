"""Five connected ring cells, three above two, with broad shared junctions.
Plan: eliminate incidental overlap lenses by using one shared edge at each linked pair.
The loops remain individually readable. All shared junctions are emitted once.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3c672b26-42c9-4289-a407-8947e0d6a086'
SOURCE_PATH='pictographic-primitives/_uncategorized_29/olympic rings_3c672b26-42c9-4289-a407-8947e0d6a086.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='five-interlocking-olympic-rings'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='symbols/sport'
    aliases=('olympic rings',)
    keywords=('olympics','five','rings','sport')
    def build(self):
        edges=[]
        def line(n,a,b):
            self.add_line(n,a,b);edges.append((n,a,b))
        def curve(n,a,b,c,d):
            self.add_bezier(n,a,(b,c,d));edges.append((n,a,d))
        for i,cx in enumerate((12,24,36)):
            curve(f'crown-left-{i}',(cx-6,12),(cx-4,8),(cx-3,6),(cx,6))
            curve(f'crown-right-{i}',(cx,6),(cx+3,6),(cx+4,8),(cx+6,12))
            curve(f'lower-left-{i}',(cx-6,22),(cx-4,24),(cx-2,28),(cx,28))
            curve(f'lower-right-{i}',(cx,28),(cx+2,28),(cx+4,24),(cx+6,22))
        for i,x in enumerate((6,18,30,42)):line(f'upper-side-{i}',(x,12),(x,22))
        for i,cx in enumerate((18,30)):
            curve(f'base-left-{i}',(cx-6,36),(cx-4,40),(cx-3,42),(cx,42))
            curve(f'base-right-{i}',(cx,42),(cx+3,42),(cx+4,40),(cx+6,36))
        for i,x in enumerate((12,24,36)):line(f'lower-side-{i}',(x,28),(x,36))
        for i,(n,a,b) in enumerate(edges):
            for other,c,d in edges[i+1:]:
                if a in (c,d) or b in (c,d):self.relate('connect',n,other)
