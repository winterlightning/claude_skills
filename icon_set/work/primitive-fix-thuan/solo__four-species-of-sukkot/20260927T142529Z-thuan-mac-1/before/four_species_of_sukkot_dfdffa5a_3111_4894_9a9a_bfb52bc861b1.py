"""Botanical bundle with a straight lulav, paired branching sprig and asymmetric citron. Shared stem attachment nodes and rounded citron outline.
Keyshape SQUARE. Lucide sprout: coherent botanical curves and shared branch nodes.
Omissions: Fine leaf veins and citron dimple omitted to keep clear openings."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dfdffa5a-3111-4894-9a9a-bfb52bc861b1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/sukkot feast of tabernacles_dfdffa5a-3111-4894-9a9a-bfb52bc861b1.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'four-species-of-sukkot'
    keyshape = Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases=()
    keywords=('four', 'species', 'of', 'sukkot')

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

        poly('binding',(6,32),(18,32),(18,42),(6,42),closed=True)
        poly('lulav',(18,32),(18,22),(18,6))
        path('palm',(18,22),[('C',(28,6),(20,14),(24,8))])
        poly('sprig',(6,12),(6,22),(6,32))
        line('branch',(6,22),(11,17))
        join('sprig','branch');join('sprig','binding');join('lulav','binding');join('lulav','palm')
        path('citron',(34,23),[('C',(42,32),(40,23),(42,26)),('C',(34,42),(42,38),(38,42)),('C',(28,34),(28,42),(28,39)),('C',(34,23),(28,28),(29,25))],True)
        path('stem',(34,23),[('C',(40,15),(35,19),(38,17))]);join('stem','citron')

