"""Rounded tilted top handle above circular guard; lower exposed blade with three large teeth. Guard and blade share shoe endpoints.
Keyshape SQUARE. No useful subject-specific Lucide match; supplied original determines the silhouette.
Omissions: Small hub omitted to preserve blade negative space."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6d7f07b0-c4a7-5343-80d4-cc97519098e9'
SOURCE_PATH = 'pictographic-primitives/tools/power tools electric saw_6d7f07b0-c4a7-5343-80d4-cc97519098e9.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'handheld-circular-saw'
    keyshape = Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "tools"
    categories = ("primitives", "tools")
    aliases=()
    keywords=('handheld', 'circular', 'saw')

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

        path('guard',(14,26),[('A',(28,12),14,14,True),('A',(42,26),14,14,True)])
        poly('shoe',(6,26),(14,26),(42,26));join('shoe','guard')
        path('handle',(14,26),[('L',(8,18)),('A',(10,8),7,7,True),('L',(20,6)),('C',(28,12),(25,6),(28,8))]);join('handle','guard');join('handle','shoe')
        path('blade',(42,26),[('L',(40,35)),('L',(34,34)),('L',(31,42)),('L',(26,38)),('L',(19,40)),('L',(18,34)),('L',(14,32)),('L',(14,26))]);join('blade','guard');join('blade','shoe')

