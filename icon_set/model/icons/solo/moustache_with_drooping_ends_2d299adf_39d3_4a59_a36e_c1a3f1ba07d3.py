'moustache-with-drooping-ends: Flatten the over-tall moustache and restore broad curling lobes with drooping tips. Repaired original in place.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2d299adf-39d3-4a59-a36e-c1a3f1ba07d3'
SOURCE_PATH = 'pictographic-primitives/beauty/mustache_2d299adf-39d3-4a59-a36e-c1a3f1ba07d3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'moustache-with-drooping-ends'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    aliases = ()
    keywords = ('beard', 'moustache', 'facial hair', 'grooming', 'barber', 'style', 'face', 'hair')

    def build(self):
        # Symbol plan: Flatten the over-tall moustache and restore broad curling lobes with drooping tips.

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
        path('moustache',(24,18),[('C',(14,12),(20,12),(18,12)),('C',(4,30),(6,12),(4,22)),('L',(4,36)),('C',(12,28),(10,36),(12,32)),('C',(24,26),(16,30),(21,29)),('C',(36,28),(27,29),(32,30)),('C',(44,36),(36,32),(38,36)),('L',(44,30)),('C',(34,12),(44,22),(42,12)),('C',(24,18),(30,12),(28,12))],True)
