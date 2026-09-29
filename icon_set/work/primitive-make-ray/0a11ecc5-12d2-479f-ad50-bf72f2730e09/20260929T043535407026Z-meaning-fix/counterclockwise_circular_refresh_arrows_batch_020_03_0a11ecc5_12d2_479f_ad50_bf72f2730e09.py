"""Restored a common circular orbit, counterclockwise direction and tangent arrow tips.
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

        # Two arcs share a circular center; opposite arrowheads are mirrored.
        self.path('upper',(40,12),[('A',(24,4),20,20,False),('A',(4,24),20,20,False)])
        self.add_polyline('upper-tip',(4,16),(4,24),(12,24))
        self.relate('connect','upper','upper-tip')
        self.path('lower',(8,36),[('A',(24,44),20,20,False),('A',(44,24),20,20,False)])
        self.add_polyline('lower-tip',(36,24),(44,24),(44,32))
        self.relate('connect','lower','lower-tip')
