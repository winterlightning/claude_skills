"""One input square fans out to three output squares. Arrowheads are omitted to protect square openings and branch spacing. Lucide network informs consistent nodes and shared junctions; the asymmetric flow remains left-to-right.
SOLO48 VRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='8a7a4269-ac7b-43d8-893f-a0bbadc777ea'
SOURCE_PATH='pictographic-primitives/programing/elastic load balance_8a7a4269-ac7b-43d8-893f-a0bbadc777ea.svg'
AUTHOR='gpt-6'

class LoadBalancerBranches(Solo48):
    icon_id='load-balancer-branches'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases=()
    keywords=('load-balancer', 'distribute', 'traffic', 'arrows', 'servers', 'network', 'routing', 'split')

    def build(self) -> None:
        def ring(name,x,y,r):
            self.add_arc(name+'-right',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(name+'-left',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(name,name+'-right',name+'-left',closed=True)

        def node(name,x,y,w,h):
            self.add_polyline(name,(x,y),(x+w//2,y),(x+w,y),(x+w,y+h),(x+w//2,y+h),(x,y+h),closed=True)

        def join(*names):
            from itertools import combinations
            for a,b in combinations(names,2): self.relate('connect',a,b)

        self.add_polyline('input',(8,20),(16,20),(16,24),(16,28),(8,28),closed=True)
        self.add_line('feed',(16,24),(24,24))
        join('input','feed')
        self.add_polyline('upper-route',(24,24),(24,8),(32,8))
        self.add_line('middle-route',(24,24),(32,24))
        self.add_polyline('lower-route',(24,24),(24,40),(32,40))
        join('feed','upper-route','middle-route','lower-route')
        for name,y in (('upper',4),('middle',20),('lower',36)):
            self.add_polyline(name+'-server',(32,y),(40,y),(40,y+8),(32,y+8),(32,y+4),closed=True)
            join(name+'-server',name+'-route')
