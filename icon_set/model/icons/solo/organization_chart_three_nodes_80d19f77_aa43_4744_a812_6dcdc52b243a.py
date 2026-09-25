"""One square parent branches to three square children. Lucide network informs the orthogonal tree and consistent node proportions. All four nodes remain; round stroke joins simplify the tiny corner arcs. Exact bilateral symmetry.
SOLO48 HRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='80d19f77-aa43-4744-a812-6dcdc52b243a'
SOURCE_PATH='pictographic-primitives/programing/organizations_80d19f77-aa43-4744-a812-6dcdc52b243a.svg'
AUTHOR='gpt-6'

class OrganizationChartThreeNodes(Solo48):
    icon_id='organization-chart-three-nodes'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    aliases=()
    keywords=('organization', 'chart', 'hierarchy', 'tree', 'structure', 'team', 'nodes', 'diagram')

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

        self.add_polyline('root',(20,8),(28,8),(28,16),(24,16),(20,16),closed=True)
        self.add_line('root-stem',(24,16),(24,24))
        self.add_line('bus-left',(8,24),(24,24))
        self.add_line('bus-right',(24,24),(40,24))
        join('root','root-stem')
        join('root-stem','bus-left','bus-right')
        for name,x in (('left',8),('middle',24),('right',40)):
            self.add_line(name+'-stem',(x,24),(x,32))
            self.add_polyline(name+'-node',(x,32),(x+4,32),(x+4,40),(x-4,40),(x-4,32),closed=True)
            join(name+'-stem',name+'-node')
            for bus in (('bus-left',) if name=='left' else ('bus-right',) if name=='right' else ('bus-left','bus-right','root-stem')): join(name+'-stem',bus)
