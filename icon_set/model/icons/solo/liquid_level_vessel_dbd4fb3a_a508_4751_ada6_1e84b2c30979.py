"""An upright rounded rectangular vessel containing two curved liquid-level boundaries running from one side to the other. Keep the boundaries attached to the vessel as shown.

Plan: Rounded vessel and two repeated rising liquid boundaries attached to its walls. Bounds (10,4)-(38,44).
Construction reference: Lucide briefcase-business: equal tangent rounded corners; source supplies flowing level lines."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dbd4fb3a-a508-4751-ada6-1e84b2c30979'
SOURCE_PATH = 'pictographic-primitives/other/rectangle with waves_dbd4fb3a-a508-4751-ada6-1e84b2c30979.svg'
SOURCE_ICON_IDS = ('dbd4fb3a-a508-4751-ada6-1e84b2c30979',)
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


class LiquidLevelVessel(Solo48):
    icon_id = 'liquid-level-vessel'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('liquid', 'level', 'vessel')

    def build(self) -> None:
        rounded(self,'vessel',10,4,38,44,4)
        for i,y in enumerate((22,36)):
            self.add_bezier(f'level-{i}',(10,y),((20,y-8),(28,y),(38,y-8)))
            self.relate('connect','vessel',f'level-{i}')
