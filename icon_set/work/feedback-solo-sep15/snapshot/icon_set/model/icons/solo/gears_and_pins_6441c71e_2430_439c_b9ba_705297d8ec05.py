"""Two six-lobed gears above four signal pins of varying height. Gear centre dots are omitted to keep the cog openings clear; all gears and all four pins remain. Lucide network informs repeated rings; gear outlines use a shared six-lobe pattern. Intentional pin-height variation.
SOLO48 HRECT_L, designed directly against the live contract bounds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='6441c71e-2430-439c-b9ba-705297d8ec05'
SOURCE_PATH='pictographic-primitives/programing/internet of thing graph service setting_6441c71e-2430-439c-b9ba-705297d8ec05.svg'
AUTHOR='gpt-6'

class GearsAndPins(Solo48):
    icon_id='gears-and-pins'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/programming"
    aliases=()
    keywords=('gears', 'pins', 'settings', 'iot', 'sensors', 'configuration', 'devices', 'graph')

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

        cog=((0,-8),(3,-5),(8,-4),(6,0),(8,4),(3,5),(0,8),(-3,5),(-8,4),(-6,0),(-8,-4),(-3,-5))
        for name,cx in (('left',12),('right',36)):
            self.add_polyline(name+'-gear',*((cx+x,16+y) for x,y in cog),closed=True)
        for i,(x,y) in enumerate(((6,34),(18,36),(30,33),(42,34))):
            ring(f'pin-{i}-ring',x,y,2)
            self.add_line(f'pin-{i}-stem',(x,y+2),(x,40))
            join(f'pin-{i}-ring',f'pin-{i}-stem')
