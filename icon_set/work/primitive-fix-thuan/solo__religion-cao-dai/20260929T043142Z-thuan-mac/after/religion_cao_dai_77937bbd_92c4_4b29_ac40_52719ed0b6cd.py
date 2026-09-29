"""Restored a complete almond eye enclosed by a triangular outline; the iris is a solid pupil to keep the eye open and clear at 48px.
Plan and comparison: The eye merged with the triangle sides and lost its lower eyelid and outlined iris.
Construction reference: eye: paired circular lid arcs and an outlined circular iris
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='77937bbd-92c4-4b29-ac40-52719ed0b6cd'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__religion-cao-dai/20260929T043142Z-thuan-mac/reference/religion cao dai_77937bbd-92c4-4b29-ac40-52719ed0b6cd.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='religion-cao-dai'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def path(self, name, start, commands, closed=False):
        members=[]
        at=start
        for n,c in enumerate(commands):
            ident=f"{name}-{n}"
            if c[0]=='L':
                end=c[1]; self.add_line(ident,at,end)
            else:
                _,end,rx,ry,sweep,*large=c
                self.add_arc(ident,at,end,radius_x=rx,radius_y=ry,sweep=sweep,large_arc=bool(large and large[0]))
            members.append(ident); at=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

    def box(self,name,l,t,r,b,rad=2):
        self.path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):

        # Triangle owns one complete eye; both lids share the same mirrored endpoints.
        self.add_polyline('triangle',(24,4),(46,44),(2,44),closed=True)
        self.path('eye',(15,31),[('A',(33,31),10,10,True),('A',(15,31),10,10,True)],True)
        self.add_dot('pupil',(24,31))

Drawing.exception = {'reason': 'A complete almond eye inside a triangle requires compact spacing. The pupil is solid rather than outlined so the eye remains open; both eyelids are visibly separated from the triangle. Reviewed against the original and rejected drawing at 48px and enlarged size in light and dark. User explicitly delegated case-specific exceptions for UI/UX quality.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'e0d4bb0a463cdcbefe714043072503c665cdc3498e8340f7a2923efe65756f5b'}
