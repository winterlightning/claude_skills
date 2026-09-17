'perched-songbird: Give the rounded songbird a distinct projecting beak, small eye, folded wing and branch perch. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '761d7259-88bd-5947-bce8-85a1bc2f5d98'
SOURCE_PATH = 'pictographic-primitives/animals/bird_761d7259-88bd-5947-bce8-85a1bc2f5d98.svg'
AUTHOR = 'gpt-6'


class PerchedSongbird(Solo48):
    icon_id = 'perched-songbird'
    keyshape = Keyshape.FREE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('bird', 'songbird', 'sparrow', 'robin', 'perched', 'wildlife', 'wing', 'garden')

    def build(self):
        # Symbol plan: Give the rounded songbird a distinct projecting beak, small eye, folded wing and branch perch.

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
        path('bird',(4,32),[('L',(20,16)),('C',(30,4),(19,8),(24,4)),('C',(38,12),(35,4),(38,7)),('L',(44,16)),('L',(38,20)),('C',(24,36),(38,32),(34,36)),('L',(4,32))],True)
        path('wing',(20,16),[('C',(14,34),(24,24),(14,26))]);join('wing','bird')
        dot('eye',(30,13));line('leg',(25,36),(25,44));line('branch',(12,44),(38,44));join('leg','bird');join('leg','branch')
