"""An empty upright chamber bounded by two straight sides and rounded horizontal caps at top and bottom. Exclude the human figure.

Plan: Two equal rounded cap rails share their side attachment coordinates with the upright walls. Bounds (6,2)-(58,62).
Hosting at the standard slot: add-sub32: valid, heart-state-63: review, check-mark: valid.
Construction reference: Lucide briefcase-business: shared attachment points and equal rounded corners."""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'ce4b7b2a-6a18-47a7-8b6e-f8db025755b5'
SOURCE_PATH = 'pictographic-primitives/science/human tube_ce4b7b2a-6a18-47a7-8b6e-f8db025755b5.svg'
SOURCE_ICON_IDS = ('ce4b7b2a-6a18-47a7-8b6e-f8db025755b5',)
AUTHOR = 'gpt-6'

def circle(m, name, cx, cy, r):
    # A single circular loop owns its radius and shared antipodal endpoints.
    m.add_arc(name+"-top", (cx-r,cy), (cx+r,cy), radius_x=r)
    m.add_arc(name+"-bottom", (cx+r,cy), (cx-r,cy), radius_x=r)
    m.add_contour(name,name+"-top",name+"-bottom",closed=True)


def rounded(m, name, left, top, right, bottom, r):
    # One rectangle owns all four equal tangent quarter-circle corners.
    points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
            (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
    for i,start in enumerate(points):
        end=points[(i+1)%8]
        if i%2: m.add_arc(f"{name}-{i}",start,end,radius_x=r)
        else: m.add_line(f"{name}-{i}",start,end)
    m.add_contour(name,*(f"{name}-{i}" for i in range(8)),closed=True)


class CryogenicChamberContainer(Container64):
    icon_id = 'cryogenic-chamber-container'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'containers'
    aliases = ()
    keywords = ('cryogenic', 'chamber', 'container')

    def build(self) -> None:
        for name,top in (('top-cap',2),('bottom-cap',54)):
            rounded(self,name,6,top,58,top+8,4)
        for x in (12,52):
            self.add_line(f'wall-{x}',(x,10),(x,54))
            for cap in ('top-cap','bottom-cap'): self.relate('connect',f'wall-{x}',cap)
