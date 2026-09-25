"""A detached round head above a complete compact human torso with short shoulder sleeves and a tapered lower body. Preserve the full torso; exclude any chamber or surrounding frame.

Plan: Detached round head and compact tapered torso with sleeves. Head bottom 10, shoulder top 18: exact 4-unit ink gap. Bounds (6,2)-(26,30).
Construction reference: Shared human_ref/user.svg and full_body_ref.png: circular head, coherent shoulders, exact detached gap."""
from ...keyshapes import Keyshape
from ._base import Symbol32

SOURCE_ICON_ID = 'ce4b7b2a-6a18-47a7-8b6e-f8db025755b5'
SOURCE_PATH = 'pictographic-primitives/science/human tube_ce4b7b2a-6a18-47a7-8b6e-f8db025755b5.svg'
SOURCE_ICON_IDS = ('ce4b7b2a-6a18-47a7-8b6e-f8db025755b5', '53c3e6a6-c8a3-4333-b0db-0f7f9d33f82c')
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


class FullTorsoPersonSub(Symbol32):
    icon_id = 'full-torso-person-sub'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'science'
    categories = ('science', 'primitives')
    aliases = ()
    keywords = ('full', 'torso', 'person', 'sub')

    def build(self) -> None:
        circle(self,'head',16,6,4)
        self.add_bezier('shoulders',(6,24),((6,18),(9,18),(16,18)),((23,18),(26,18),(26,24)))
        self.add_polyline('body',(26,24),(22,24),(21,30),(11,30),(10,24),(6,24))
        self.add_contour('torso','shoulders',*[f'body-{i}' for i in range(1,6)],closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='body']
