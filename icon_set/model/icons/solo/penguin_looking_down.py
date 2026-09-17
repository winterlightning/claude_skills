'penguin-looking-down: Restore the downturned beak, upright tapered body, belly division and flat feet. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ca363f4-f61f-5da3-a3be-41fa52d1fa3a'
SOURCE_PATH = 'pictographic-primitives/animals/penguin mother_9ca363f4-f61f-5da3-a3be-41fa52d1fa3a.svg'
AUTHOR = 'gpt-6'

class PenguinLookingDown(Solo48):
    icon_id = 'penguin-looking-down'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('penguin', 'bending', 'looking', 'down', 'bird', 'antarctic', 'nurture', 'care')

    def build(self):
        # Symbol plan: Restore the downturned beak, upright tapered body, belly division and flat feet.

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
        path('penguin',(8,22),[('C',(24,4),(8,12),(15,4)),('C',(38,25),(35,4),(38,15)),('L',(38,36)),('L',(40,44)),('L',(20,44)),('C',(18,22),(13,37),(16,28)),('L',(12,28)),('L',(8,22))],True)
        dot('eye',(23,14))
        path('flipper',(27,23),[('C',(26,32),(29,26),(29,28))])
