"""An isometric cube branches to three circular nodes. Lucide boxes informs the three face junction; network informs the bus and equal leaves. All cube faces and nodes remain; deliberately angled cube faces preserve perspective.
SOLO48 VRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='5c51367a-99e6-4ec3-ae46-92b7c09949ef'
SOURCE_PATH='pictographic-primitives/programing/organizations circle_5c51367a-99e6-4ec3-ae46-92b7c09949ef.svg'
AUTHOR='gpt-6'

class CubeHierarchyRoundNodes(Solo48):
    icon_id='cube-hierarchy-round-nodes'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('cube', 'hierarchy', 'organization', 'tree', 'nodes', 'structure', 'accounts', 'network')

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

        self.add_polyline('cube',(24,4),(34,10),(34,20),(24,26),(14,20),(14,10),closed=True)
        self.add_line('face-left',(14,10),(24,16))
        self.add_line('face-right',(34,10),(24,16))
        self.add_line('face-bottom',(24,16),(24,26))
        join('cube','face-left','face-right','face-bottom')
        self.add_line('root-stem',(24,26),(24,29))
        self.add_line('bus-left',(11,29),(24,29))
        self.add_line('bus-right',(24,29),(37,29))
        join('cube','root-stem')
        join('root-stem','bus-left','bus-right')
        for name,x in (('left',11),('middle',24),('right',37)):
            self.add_line(name+'-stem',(x,29),(x,38))
            ring(name+'-node',x,41,3)
            join(name+'-stem',name+'-node')
            for bus in (('bus-left',) if name=='left' else ('bus-right',) if name=='right' else ('bus-left','bus-right','root-stem')): join(name+'-stem',bus)
