"""Restore a front-view cabin, visible tire ends and two long smooth skidding tracks with equal spacing.
Construction: Lucide car-front: paired front body and tire ends; source wavy tracks retained.
Omissions: Headlamps omitted as absent from source.
Keyshape VRECT_L: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ba9924a-41d3-4ed9-93c5-d475f8bd2fd2'
SOURCE_PATH = 'pictographic-primitives/symbol/car with wave lines_9ba9924a-41d3-4ed9-93c5-d475f8bd2fd2.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'car-skidding'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('car', 'skidding')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*pts,closed=False):self.add_polyline(name,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)

        path('body',(12,14),[('L',(14,14)),('L',(34,14)),('L',(36,14)),('A',(40,18),4,4,True),('L',(40,20)),('A',(36,24),4,4,True),('L',(12,24)),('A',(8,20),4,4,True),('L',(8,18)),('A',(12,14),4,4,True)],True)
        path('cabin',(14,14),[('L',(17,6)),('C',(20,4),(18,4),(19,4)),('L',(28,4)),('C',(31,6),(29,4),(30,4)),('L',(34,14))]);join('cabin','body')
        for x in (14,34):
         line(f'tire-{x}',(x,24),(x,27));join(f'tire-{x}','body')
        for x in (16,32):
         path(f'track-{x}',(x,35),[('C',(x-3,39),(x-6,36),(x-6,38)),('C',(x,44),(x+4,41),(x+4,42))])
