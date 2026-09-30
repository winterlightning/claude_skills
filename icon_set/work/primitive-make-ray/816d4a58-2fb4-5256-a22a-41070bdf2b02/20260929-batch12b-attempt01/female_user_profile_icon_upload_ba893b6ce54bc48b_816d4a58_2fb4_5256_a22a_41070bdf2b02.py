"""Only the rejected SVG is available. Its head floats far above a blocky torso. Enlarge the circular head, bring it into proper bust contact and soften the shoulders while retaining the tapered female torso.
Plan: SQUARE; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='816d4a58-2fb4-5256-a22a-41070bdf2b02'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__female-user-profile-icon-upload-ba893b6ce54bc48b/20260929T132613Z-thuan-mac/reference/female-user-profile-icon-upload-ba893b6ce54bc48b_816d4a58-2fb4-5256-a22a-41070bdf2b02.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='female-user-profile-icon-upload-ba893b6ce54bc48b'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('female-user-profile-icon-upload-ba893b6ce54bc48b',)
    human_construction='bust'
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                kind,end,*args=step; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end; members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b): self.relate('connect',a,b)

        def box(name,l,t,r,b,rad=0):
            if not rad:self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
            else:path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        circle('head',24,14,8)
        path('body',(6,36),[('L',(12,30)),('A',(24,26),12,4,True),('A',(36,30),12,4,True),('L',(42,36)),('L',(32,36)),('L',(28,42)),('L',(20,42)),('L',(16,36)),('L',(6,36))],True);join('head','body')
