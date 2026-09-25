"""A circular network with three connections fanning from a lower-left junction to upper-right rim points. Small ring markers reduce to rim junctions to avoid split tiny holes; all three fan links remain. Lucide network informs shared nodes; circular arcs use exact integer circle points. Intentional directional asymmetry.
SOLO48 CIRCLE, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='904d0466-8146-5c60-a35f-f40e27fd454e'
SOURCE_PATH='pictographic-primitives/programing/internet of thing analytics_904d0466-8146-5c60-a35f-f40e27fd454e.svg'
AUTHOR='gpt-6'

class FanNetworkCircle(Solo48):
    icon_id='fan-network-circle'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases=()
    keywords=('network', 'nodes', 'fan', 'graph', 'analytics', 'iot', 'connections', 'circle')

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

        points=((24,4),(40,12),(44,24),(24,44),(12,40),(4,24),(24,4))
        members=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            member=f'rim-{i}'
            self.add_arc(member,a,b,radius_x=20)
            members.append(member)
        self.add_contour('rim',*members,closed=True)
        for i,tip in enumerate(((24,4),(40,12),(44,24))):
            self.add_line(f'fan-{i}',(12,40),tip)
            join('rim',f'fan-{i}')
        join('fan-0','fan-1','fan-2')
