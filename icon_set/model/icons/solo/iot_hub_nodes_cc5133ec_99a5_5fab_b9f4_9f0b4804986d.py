"""A large IoT ring hub branches to three small ring nodes. Side branches leave the hub tangentially; the central marker diamond becomes a short pin stem. Lucide network informs equal child rings and explicit junctions. Bilateral symmetry retains the hub hierarchy.
SOLO48 CIRCLE, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='cc5133ec-99a5-5fab-b9f4-9f0b4804986d'
SOURCE_PATH='pictographic-primitives/programing/internet of thing analytics services_cc5133ec-99a5-5fab-b9f4-9f0b4804986d.svg'
AUTHOR='gpt-6'

class IotHubNodes(Solo48):
    icon_id='iot-hub-nodes'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases=()
    keywords=('iot', 'hub', 'nodes', 'network', 'branches', 'devices', 'analytics', 'connection')

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

        ring('hub',24,14,10)
        self.add_line('left-branch',(14,14),(10,30))
        self.add_line('right-branch',(34,14),(38,30))
        self.add_line('central-branch',(24,24),(24,34))
        for branch in ('left-branch','right-branch','central-branch'): join('hub',branch)
        for name,x,y,branch in (('left',10,33,'left-branch'),('right',38,33,'right-branch'),('central',24,37,'central-branch')):
            ring(name+'-node',x,y,3)
            join(name+'-node',branch)
        self.add_line('marker-pin',(24,40),(24,44))
        join('marker-pin','central-node')
