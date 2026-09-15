"""A six-lobed gear branches to three square nodes. The central ring and dot are omitted to preserve room for the square leaves. Lucide network informs the equal nodes and shared bus. Bilateral symmetry.
SOLO48 HRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='7c5fddd0-2422-4e22-b179-5596f4845f71'
SOURCE_PATH='pictographic-primitives/programing/obs works_7c5fddd0-2422-4e22-b179-5596f4845f71.svg'
AUTHOR='gpt-6'

class GearHierarchySquareNodes(Solo48):
    icon_id='gear-hierarchy-square-nodes'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('gear', 'hierarchy', 'tree', 'settings', 'operations', 'nodes', 'workflow', 'structure')

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

        self.add_polyline('gear',(24,8),(27,11),(32,12),(30,16),(32,20),(27,21),(24,24),(21,21),(16,20),(18,16),(16,12),(21,11),closed=True)
        # Omit the small hub to keep the gear opening clear.
        self.add_line('bus-left',(8,24),(24,24))
        self.add_line('bus-right',(24,24),(40,24))
        join('gear','bus-left','bus-right')
        for name,x in (('left',8),('middle',24),('right',40)):
            self.add_line(name+'-stem',(x,24),(x,32))
            self.add_polyline(name+'-node',(x,32),(x+4,32),(x+4,40),(x-4,40),(x-4,32),closed=True)
            join(name+'-stem',name+'-node')
            for bus in (('bus-left',) if name=='left' else ('bus-right',) if name=='right' else ('bus-left','bus-right','gear')): join(name+'-stem',bus)
