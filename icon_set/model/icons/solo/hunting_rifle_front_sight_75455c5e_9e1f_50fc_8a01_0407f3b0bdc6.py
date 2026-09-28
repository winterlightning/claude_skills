"""Diagonal rifle with rounded stock shoulder and continuous rising barrel. Front sight retained; functional thin barrel is one stroke.
Keyshape HRECT_L. No useful subject-specific Lucide match; supplied original determines the silhouette.
Omissions: Small trigger omitted; thin barrel preserved as a centerline."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '75455c5e-9e1f-50fc-8a01-0407f3b0bdc6'
SOURCE_PATH = 'pictographic-primitives/war/modern weapon rifle_75455c5e-9e1f-50fc-8a01-0407f3b0bdc6.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hunting-rifle-front-sight'
    keyshape = Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "war"
    categories = ("war", "primitives")
    aliases=()
    keywords=('hunting', 'rifle', 'front', 'sight')

    def build(self):

        def path(n, start, steps, closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(steps):
                if here==end: continue
                tag=f'{n}-{i}'
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C': self.add_bezier(tag,here,(a[0],a[1],end))
                members.append(tag); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,q=4):
            path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('stock',(4,40),[('L',(4,29)),('L',(13,25)),('C',(21,18),(16,24),(17,18)),('L',(28,18)),('L',(28,27)),('L',(23,27)),('C',(16,34),(20,28),(19,32)),('L',(4,40))],True)
        poly('barrel',(28,18),(44,13),(44,8));join('stock','barrel')

