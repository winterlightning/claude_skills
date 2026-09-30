"""Only the rejected SVG is available. Its code marks are cramped thick parentheses. Use clear angled code chevrons, a balanced screen and aligned stand.
Plan: SQUARE; coherent source-specific contours with shared physical joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='dffb3652-f762-58d5-b070-7bb403a64329'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__computer-monitor-with-code-upload-a3ccb7c42eee5d1f/20260929T132613Z-thuan-mac/reference/computer-monitor-with-code-upload-a3ccb7c42eee5d1f_dffb3652-f762-58d5-b070-7bb403a64329.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='computer-monitor-with-code-upload-a3ccb7c42eee5d1f'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('computer-monitor-with-code-upload-a3ccb7c42eee5d1f',)
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

        path('screen',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,30)),('A',(38,34),4,4,True),('L',(24,34)),('L',(10,34)),('A',(6,30),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        self.add_polyline('code-left',(19,15),(15,20),(19,25))
        self.add_polyline('code-right',(29,15),(33,20),(29,25))
        self.add_line('stand',(24,34),(24,42));join('stand','screen')
        self.add_polyline('foot',(16,42),(24,42),(32,42));join('foot','stand')
