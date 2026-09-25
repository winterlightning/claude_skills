"""Three hollow hexagonal nuts form a staggered cluster, two at left and one at right. Nested outlines reduce to one hexagonal ring per nut, keeping all three holes visibly open. No useful exact Lucide hardware-nut match was found; the supplied source determines the hexagonal construction. Deliberate staggered arrangement.
SOLO48 SQUARE, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='e9326841-b6b1-432e-a99d-c2065849139b'
SOURCE_PATH='pictographic-primitives/programing/well architected tools_e9326841-b6b1-432e-a99d-c2065849139b.svg'
AUTHOR='gpt-6'

class HexNutCluster(Solo48):
    icon_id='hex-nut-cluster'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases=()
    keywords=('nuts', 'hexagon', 'tools', 'hardware', 'settings', 'bolts', 'architecture', 'engineering')

    def build(self) -> None:
        def ring(name,x,y,r):
            points=((x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r))
            members=[]
            for i,(a,b) in enumerate(zip(points,points[1:])):
                member=f'{name}-{i}'
                self.add_arc(member,a,b,radius_x=r)
                members.append(member)
            self.add_contour(name,*members,closed=True)

        def join(*names):
            from itertools import combinations
            for a,b in combinations(names,2): self.relate('connect',a,b)

        for name,x,y in (('upper',13,12),('lower',13,36),('right',35,24)):
            self.add_polyline(name+'-nut',(x-7,y),(x-3,y-6),(x+3,y-6),(x+7,y),(x+3,y+6),(x-3,y+6),closed=True)
