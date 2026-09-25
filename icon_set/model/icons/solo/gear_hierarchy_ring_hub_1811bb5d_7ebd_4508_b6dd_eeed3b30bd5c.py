"""A six-lobed gear with a hollow hub branches to three ring nodes. The hub centre dot is omitted to keep the central ring clear. Lucide network informs explicit branches and equal child nodes. Bilateral symmetry.
SOLO48 VRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='1811bb5d-7ebd-4508-b6dd-eeed3b30bd5c'
SOURCE_PATH='pictographic-primitives/programing/obs works circle_1811bb5d-7ebd-4508-b6dd-eeed3b30bd5c.svg'
AUTHOR='gpt-6'

class GearHierarchyRingHub(Solo48):
    icon_id='gear-hierarchy-ring-hub'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases=()
    keywords=('gear', 'hierarchy', 'tree', 'settings', 'operations', 'nodes', 'automation', 'structure')

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

        self.add_polyline('gear',(24,4),(30,7),(38,10),(36,17),(38,24),(30,27),(24,30),(18,27),(10,24),(12,17),(10,10),(18,7),closed=True)
        ring('hub',24,17,3)
        self.add_line('root-stem',(24,30),(24,31))
        self.add_line('bus-left',(11,31),(24,31))
        self.add_line('bus-right',(24,31),(37,31))
        join('gear','root-stem')
        join('root-stem','bus-left','bus-right')
        for name,x in (('left',11),('middle',24),('right',37)):
            self.add_line(name+'-stem',(x,31),(x,38))
            ring(name+'-node',x,41,3)
            join(name+'-stem',name+'-node')
            for bus in (('bus-left',) if name=='left' else ('bus-right',) if name=='right' else ('bus-left','bus-right','root-stem')): join(name+'-stem',bus)
