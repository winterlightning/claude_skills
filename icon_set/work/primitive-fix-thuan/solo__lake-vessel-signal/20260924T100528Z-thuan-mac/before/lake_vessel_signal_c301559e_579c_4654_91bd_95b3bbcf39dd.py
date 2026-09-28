"""A wide vessel carries two nested signal arcs over water. The crowded rear rim is omitted and water reduces to one smooth wave, as visible in the prepared reference. Source establishes the vessel and signal; no useful exact Lucide match. Shared axes and radii produce balanced curves.
SOLO48 SQUARE, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='c301559e-579c-4654-91bd-95b3bbcf39dd'
SOURCE_PATH='pictographic-primitives/programing/lake formation_c301559e-579c-4654-91bd-95b3bbcf39dd.svg'
AUTHOR='gpt-6'

class LakeVesselSignal(Solo48):
    icon_id='lake-vessel-signal'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('lake', 'water', 'vessel', 'signal', 'data', 'formation', 'waves', 'boat')

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

        self.add_arc('signal-outer',(14,12),(34,12),radius_x=10,radius_y=6)
        self.add_arc('signal-inner',(21,18),(27,18),radius_x=3)
        self.add_arc('vessel',(42,20),(6,20),radius_x=18,radius_y=8)
        self.add_arc('water-left',(8,40),(24,40),radius_x=17,sweep=False)
        self.add_arc('water-right',(24,40),(40,40),radius_x=17)
        self.add_contour('water','water-left','water-right')
