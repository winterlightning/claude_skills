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
        for i,(left,cx,right) in enumerate(((4,10,17),(17,24,31),(31,38,44))):
            curve(f'crown-left-{i}',(left,17),(left,12),(cx-4,10),(cx,10))
            curve(f'crown-right-{i}',(cx,10),(cx+4,10),(right,12),(right,17))
            curve(f'lower-left-{i}',(left,19),(left,23),(cx-4,26),(cx,26))
            curve(f'lower-right-{i}',(cx,26),(cx+4,26),(right,23),(right,19))
        for i,x in enumerate((4,17,31,44)):line(f'upper-side-{i}',(x,17),(x,19))
        for i,(left,cx,right) in enumerate(((10,17,24),(24,31,38))):
            curve(f'base-left-{i}',(left,29),(left,34),(cx-4,38),(cx,38))
            curve(f'base-right-{i}',(cx,38),(cx+4,38),(right,34),(right,29))
        for i,x in enumerate((10,24,38)):line(f'lower-side-{i}',(x,26),(x,29))
        for i,(n,a,b) in enumerate(edges):
            for other,c,d in edges[i+1:]:
                if a in (c,d) or b in (c,d):self.relate('connect',n,other)
