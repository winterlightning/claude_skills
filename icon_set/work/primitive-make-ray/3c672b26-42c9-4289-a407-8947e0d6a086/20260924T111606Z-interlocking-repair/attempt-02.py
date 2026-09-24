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
    keyshape=Keyshape.HRECT_M
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
        for i,(left,cx,right) in enumerate(((4,11,18),(18,24,30),(30,37,44))):
            # End tangents open toward shared junctions instead of grazing a neighbor.
            curve(f'crown-left-{i}',(left,16),(left+2,12),(cx-3,10),(cx,10))
            curve(f'crown-right-{i}',(cx,10),(cx+3,10),(right-2,12),(right,16))
            curve(f'lower-left-{i}',(left,20),(left+2,22),(cx-3,26),(cx,26))
            curve(f'lower-right-{i}',(cx,26),(cx+3,26),(right-2,22),(right,20))
        for i,x in enumerate((4,18,30,44)):line(f'upper-side-{i}',(x,16),(x,20))
        for i,(left,cx,right) in enumerate(((11,18,24),(24,30,37))):
            curve(f'base-left-{i}',(left,30),(left+2,34),(cx-3,38),(cx,38))
            curve(f'base-right-{i}',(cx,38),(cx+3,38),(right-2,34),(right,30))
        for i,x in enumerate((11,24,37)):line(f'lower-side-{i}',(x,26),(x,30))
        for i,(n,a,b) in enumerate(edges):
            for other,c,d in edges[i+1:]:
                if a in (c,d) or b in (c,d):self.relate('connect',n,other)
