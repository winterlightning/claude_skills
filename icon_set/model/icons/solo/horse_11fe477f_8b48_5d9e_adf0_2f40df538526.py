"""Right-facing horse with curved mane and back, long nose and two broad legs; preserve natural asymmetry.
Keyshape SQUARE. No useful subject-specific Lucide match; supplied original determines the silhouette.
Omissions: Far legs and eye omitted; tail restored."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '11fe477f-8b48-5d9e-adf0-2f40df538526'
SOURCE_PATH = 'pictographic-primitives/animals/symbol cavalry_11fe477f-8b48-5d9e-adf0-2f40df538526.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'horse'
    keyshape = Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="animals"
    aliases=()
    keywords=('horse',)

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

        path('horse',(10,42),[('L',(10,30)),('A',(20,20),10,10,True),('L',(24,20)),('C',(32,6),(26,12),(30,9)),('L',(33,13)),('L',(42,21)),('C',(37,26),(42,25),(40,27)),('L',(33,24)),('L',(31,42)),('L',(23,42)),('L',(22,31)),('C',(18,30),(20,31),(19,30)),('L',(18,42)),('L',(10,42))],True)
        path('tail',(20,20),[('C',(6,32),(10,20),(6,24))]);join('tail','horse')

