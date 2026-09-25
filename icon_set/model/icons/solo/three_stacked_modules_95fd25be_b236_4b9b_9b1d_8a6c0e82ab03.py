"""Three separated square modules form a pyramid. Lucide network informs equal stroke and corner construction. Both supplied duplicate references map to this one concept. Clear row and column gaps; bilateral symmetry.
SOLO48 SQUARE, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='95fd25be-b236-4b9b-9b1d-8a6c0e82ab03'
SOURCE_PATH='pictographic-primitives/programing/module three_95fd25be-b236-4b9b-9b1d-8a6c0e82ab03.svg'
AUTHOR='gpt-6'
SOURCE_REFERENCES=(('f9fae231-69ce-40f3-ac89-7b4fb7c79dfe', 'pictographic-primitives/programing/module three_f9fae231-69ce-40f3-ac89-7b4fb7c79dfe.svg'),)

class ThreeStackedModules(Solo48):
    icon_id='three-stacked-modules'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "programing"
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

        for name,x,y in (('top',17,6),('left',6,28),('right',28,28)):
            self.add_polyline(name,(x,y),(x+14,y),(x+14,y+14),(x,y+14),closed=True)
