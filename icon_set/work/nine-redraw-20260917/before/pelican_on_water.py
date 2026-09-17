# Review revision; previous candidates preserved.
"""A pelican floating on water with the short underline beneath its folded wing removed. SQUARE extremes (6,6)-(42,42) preserve the bill, neck and water. Lucide bird informs the sparse curved profile. Left-facing asymmetry is intentional."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a64f3ff4-3dac-4e77-9941-a21f45a74c31'
SOURCE_PATH = 'pictographic-primitives/animals/pelican_a64f3ff4-3dac-4e77-9941-a21f45a74c31.svg'
AUTHOR = 'gpt-6'

class PelicanOnWater(Solo48):
    icon_id = 'pelican-on-water'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ('pelican',)
    keywords = ('pelican', 'water', 'bird', 'pouch', 'beak', 'sea', 'float', 'waterfowl')

    def build(self):
        # Symbol plan: Restore the long bill with throat pouch, curved neck, rounded floating body and water line.

        def path(name,start,commands,closed=False):
            members=[];here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r): ellipse(name,x,y,r,r)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('bird',(18,14),[('C',(27,4),(18,8),(21,4)),('C',(34,14),(35,4),(35,10)),('C',(25,29),(33,21),(23,23)),('C',(44,26),(30,35),(40,30)),('C',(24,36),(44,34),(32,36))])
        path('bill',(18,14),[('L',(4,16)),('C',(18,24),(5,25),(13,28)),('L',(18,14))],True)
        join('bill','bird')
        path('water',(4,44),[('C',(24,44),(11,44),(17,44)),('C',(44,44),(31,44),(37,44))])
