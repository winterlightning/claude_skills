"""Rounded hose nozzle with rear trigger and long grip; three evenly separated water strokes.
Keyshape SQUARE. No useful subject-specific Lucide match; supplied original determines the silhouette.
Omissions: Thin hose tail omitted; grip and rear trigger integrated."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a3d030d9-b45f-44f5-93c9-5ba1902c725f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/hand sprinkler_a3d030d9-b45f-44f5-93c9-5ba1902c725f.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hose-spray-gun'
    keyshape = Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "farming"
    categories = ("farming", "primitives")
    aliases=()
    keywords=('hose', 'spray', 'gun')

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

        path('body',(6,18),[('A',(10,14),4,4,True),('L',(18,14)),('C',(28,6),(20,9),(24,6)),('L',(28,26)),('C',(18,22),(24,26),(20,25)),('L',(18,38)),('A',(14,42),4,4,True),('L',(10,42)),('L',(10,22)),('L',(6,22)),('L',(6,18))],True)
        for i,(a,b) in enumerate([((38,8),(42,6)),((38,16),(42,16)),((38,24),(42,26))]):line(f'spray-{i}',a,b)

