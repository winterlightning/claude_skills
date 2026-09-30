"""Rejected clove became an upright microphone-like stem and dome. Restore the diagonal long stem, rounded bud and pointed calyx.
Plan: SQUARE; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2fe3535b-ed46-49bc-ad15-b91d93556dfe'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__clove-bud-with-pointed-sepals/20260929T132613Z-thuan-mac/reference/cloves_2fe3535b-ed46-49bc-ad15-b91d93556dfe.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='clove-bud-with-pointed-sepals'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('cloves',)
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

        path('clove',(6,38),[('L',(22,22)),('L',(20,10)),('L',(27,14)),('A',(32,6),10,10,True),('A',(42,16),10,10,True),('A',(36,25),10,10,True),('L',(42,28)),('L',(30,28)),('L',(10,42)),('A',(6,38),4,4,True)],True)
