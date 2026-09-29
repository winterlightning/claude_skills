"""Restored a common circular orbit, counterclockwise direction and distinct arrow tips.
Plan and comparison: The arrows are distorted into a narrow S rather than following one round cycle.
Construction reference: refresh-ccw: common orbit and tangent arrowhead attachments
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0a11ecc5-12d2-479f-ad50-bf72f2730e09'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__counterclockwise-circular-refresh-arrows-batch-020-03/20260929T043142Z-thuan-mac/reference/repeat_0a11ecc5-12d2-479f-ad50-bf72f2730e09.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='counterclockwise-circular-refresh-arrows-batch-020-03'
    keyshape=Keyshape.HRECT_L
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

        # Two arcs share a circular center; opposite arrowheads are mirrored.
        self.path('upper',(39,16),[('A',(24,7),17,17,False),('A',(7,24),17,17,False)])
        self.add_polyline('upper-tip',(4,18),(7,24),(13,20))
        self.relate('connect','upper','upper-tip')
        self.path('lower',(9,32),[('A',(24,41),17,17,False),('A',(41,24),17,17,False)])
        self.add_polyline('lower-tip',(35,28),(41,24),(44,30))
        self.relate('connect','lower','lower-tip')

Drawing.exception = {'reason': 'The circular orbit extends one unit beyond each horizontal keyshape short-axis edge. Keeping a round cycle and distinct arrow wings is clearer than flattening or merging them. Reviewed against the original and rejected drawing at 48px and enlarged size in light and dark. User explicitly delegated case-specific exceptions for UI/UX quality.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'ea7ce7ab112c4f38cb908760ee4275673e8d6242a07e20f1844b282903babfcf'}
