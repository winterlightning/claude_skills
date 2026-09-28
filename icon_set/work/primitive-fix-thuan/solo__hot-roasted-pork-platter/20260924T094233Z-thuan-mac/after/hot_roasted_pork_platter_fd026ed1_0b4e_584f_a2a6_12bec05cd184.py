"""Pig head and rounded roast body sit on tapered plate; two long steam strokes. Snout and pointed ear preserve pig identity.
Keyshape HRECT_L. Lucide soup: clear separated steam over a vessel.
Omissions: Eye and garnish omitted; smoother roast replaces angular silhouette."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fd026ed1-0b4e-584f-a2a6-12bec05cd184'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hot-roasted-pork-platter/20260924T094233Z-thuan-mac/reference/barbeque sucking pork roasted_fd026ed1-0b4e-584f-a2a6-12bec05cd184.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hot-roasted-pork-platter'
    keyshape = Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('hot', 'roasted', 'pork', 'platter')

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

        path('pig',(12,32),[('C',(8,24),(10,30),(8,27)),('L',(13,22)),('L',(12,15)),('L',(21,22)),('C',(32,21),(25,22),(29,20)),('A',(40,29),8,8,True),('L',(40,32))])
        path('plate',(4,32),[('L',(12,32)),('L',(40,32)),('L',(44,32)),('L',(40,40)),('L',(8,40)),('L',(4,32))],True);join('plate','pig')
        for x in (27,40):path(f'steam-{x}',(x,8),[('C',(x,12),(x-2,9),(x+2,11))])

