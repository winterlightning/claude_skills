"""bubble tea 1.
The dome was squat and straw blocky; the liquid mark disappeared. Restore a taller dome, a smoothly bent straw, rounded cup and liquid mark.
Lucide cup-soda: projecting rim, tapered cup and bent straw.
Plan: subject-specific coherent contours; repeated members share dimensions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0183656e-acff-439d-a093-d50df630d258'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__domed-takeaway-cup-with-bent-straw/20260928T164738Z-thuan-mac/reference/bubble tea 1_0183656e-acff-439d-a093-d50df630d258.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'domed-takeaway-cup-with-bent-straw'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'drinks'
    aliases = ()
    keywords = ('domed', 'takeaway', 'cup', 'with', 'bent', 'straw')

    def build(self):

        def path(n,start,*commands,closed=False):
            pt=start; members=[]
            for i,c in enumerate(commands):
                mid=f'{n}-{i}'
                if c[0]=='L': self.add_line(mid,pt,c[1]); end=c[1]
                elif c[0]=='A':
                    _,end,rx,ry,sweep=c
                    self.add_arc(mid,pt,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif c[0]=='C':
                    _,a,b,end=c; self.add_bezier(mid,pt,(a,b,end))
                pt=end;members.append(mid)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)
        def box(n,l,t,r,b,rad=2):
            path(n,(l+rad,t),('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True),closed=True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def bez(n,start,*s): self.add_bezier(n,start,*s)
        def join(a,b): self.relate('connect',a,b)
        path('cup',(10,24),('L',(13,40)),('A',(17,44),4,4,False),('L',(31,44)),('A',(35,40),4,4,False),('L',(38,24)))
        poly('rim',(8,24),(10,24),(24,24),(38,24),(40,24));join('cup','rim')
        path('dome',(10,24),('A',(38,24),14,14,True));join('rim','dome')
        path('straw',(22,29),('L',(26,8)),('C',(27,4),(29,4),(32,4)),('L',(37,4)))
        join('straw','dome');join('straw','rim')
        line('liquid',(20,37),(28,37))
