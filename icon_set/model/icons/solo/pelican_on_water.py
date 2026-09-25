'pelican-on-water: Long pointed bill with a hanging pouch, small rounded head, sweeping neck and a broad floating body. Original redrawn in place after the nine-icon meaning review.'
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
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ('pelican',)
    keywords = ('pelican', 'water', 'bird', 'pouch', 'beak', 'sea', 'float', 'waterfowl')

    def build(self):
        # Symbol plan: Long pointed bill with a hanging pouch, small rounded head, sweeping neck and a broad floating body.

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
        path('bird',(4,18),[('L',(20,10)),('C',(29,4),(21,6),(25,4)),('C',(39,13),(35,4),(39,8)),('C',(32,24),(39,18),(32,21)),('L',(44,22)),('C',(34,34),(44,30),(40,34)),('L',(26,34)),('C',(20,28),(21,34),(19,31)),('L',(22,18)),('L',(4,18))],True)
        path('pouch',(4,18),[('C',(21,23),(6,28),(14,30))]);join('pouch','bird')
        dot('eye',(29,13))
        path('water',(4,44),[('C',(14,42),(7,44),(11,42)),('C',(24,44),(17,42),(21,44)),('C',(34,42),(27,44),(31,42)),('C',(44,44),(37,42),(41,44))])
