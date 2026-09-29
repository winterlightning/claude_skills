"""diagram fall fast dash.
Before review: The terminal arrowhead was cramped and the dash rhythm was irregular, making the route hard to follow.
Feedback: Manual fix request
Revision: Rebuilt regular dash gaps, rounded elbows and a longer final descending arrow with a clear open head.
Construction: Lucide arrow-right and move-up: shaft-to-tip junction and open arrowhead.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 SQUARE; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bbf2e798-ba5c-4bc7-87e9-f2cfec970694'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arrow-dashed-offset-downward-route/20260928T164556Z-thuan-mac/reference/diagram fall fast dash_bbf2e798-ba5c-4bc7-87e9-f2cfec970694.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'arrow-dashed-offset-downward-route'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('diagram', 'fall', 'fast', 'dash')
    def build(self):

        def path(name, start, steps, closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                ident=f'{name}-{i}'
                if len(step)==2:
                    self.add_line(ident,here,step); end=step
                elif step[0]=='C':
                    _,end,c1,c2=step
                    self.add_bezier(ident,here,(c1,c2,end))
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def rounded(name,l,t,r,b,k):
            path(name,(l+k,t),[(r-k,t),((r,t+k),k,k,True),(r,b-k),((r-k,b),k,k,True),(l+k,b),((l,b-k),k,k,True),(l,t+k),((l+k,t),k,k,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        line('start',(6,6),(6,12))
        path('first-elbow',(6,20),[((10,24),4,4,False),(14,24)])
        line('middle',(22,24),(26,24))
        path('second-elbow',(34,24),[((38,28),4,4,True)])
        line('last-dash',(38,36),(38,42))
        poly('head',(32,36),(38,42),(44,36));join('head','last-dash')
