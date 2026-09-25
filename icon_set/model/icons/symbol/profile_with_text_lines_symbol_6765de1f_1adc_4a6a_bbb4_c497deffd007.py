"""A compact profile layout with a circular head and arched shoulders on the left, and two short horizontal text marks to the right. Exclude the browser frame.

Plan: Left avatar and two right text marks. Head bottom12 and shoulders20 give exact four-unit ink gap. Bounds (2,4)-(30,28).
Construction reference: Shared human_ref/user.svg: round detached head, smooth shoulders; Lucide user-round supports arch construction."""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = '6765de1f-1adc-4a6a-bbb4-c497deffd007'
SOURCE_PATH = 'pictographic-primitives/other/ui webpage social profile_6765de1f-1adc-4a6a-bbb4-c497deffd007.svg'
SOURCE_ICON_IDS = ('6765de1f-1adc-4a6a-bbb4-c497deffd007',)
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


class ProfileWithTextLinesSymbol(Symbol32):
    icon_id = 'profile-with-text-lines-symbol'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('profile', 'with', 'text', 'lines', 'symbol')

    def build(self) -> None:
        circle(self,'head',9,8,4)
        self.add_arc('shoulders',(2,27),(16,27),radius_x=7,radius_y=7)
        self.add_line('left-side',(2,27),(2,28))
        self.add_line('right-side',(16,27),(16,28))
        self.add_contour('body','left-side')
        self.relate('connect','shoulders','left-side')
        self.relate('connect','shoulders','right-side')
        for y in (16,24): self.add_line(f'text-{y}',(23,y),(30,y))
