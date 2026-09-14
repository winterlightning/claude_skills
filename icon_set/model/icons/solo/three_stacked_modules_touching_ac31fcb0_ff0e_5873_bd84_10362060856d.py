"""Three equal square modules form a touching pyramid. All three squares remain; their physical contact walls are emitted once rather than doubled. Lucide network informs consistent square nodes and shared structure. Exact bilateral symmetry.
SOLO48 SQUARE, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='ac31fcb0-ff0e-5873-bd84-10362060856d'
SOURCE_PATH='pictographic-primitives/programing/module three 1_ac31fcb0-ff0e-5873-bd84-10362060856d.svg'
AUTHOR='gpt-6'

class ThreeStackedModulesTouching(Solo48):
    icon_id='three-stacked-modules-touching'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('modules', 'blocks', 'stack', 'components', 'squares', 'building', 'structure', 'three')

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

        self.add_polyline('stack-outline',(15,6),(33,6),(33,24),(42,24),(42,42),(24,42),(6,42),(6,24),(15,24),closed=True)
        self.add_polyline('upper-contact',(15,24),(24,24),(33,24))
        self.add_line('lower-contact',(24,24),(24,42))
        join('stack-outline','upper-contact','lower-contact')
