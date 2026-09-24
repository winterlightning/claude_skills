"""Broaden the cabin and lower the roof proportions; smooth the hood and trunk into a body with separate full circular wheels.
Construction: Lucide car: continuous roof/hood contour and separate round wheel outlines.
Omissions: None
Keyshape HRECT_M: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1d48915e-d0dd-4c2f-b660-e1fc2f54ced4'
SOURCE_PATH = 'pictographic-primitives/transportation/car_1d48915e-d0dd-4c2f-b660-e1fc2f54ced4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'car'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car',)
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

        path('body',(7,33),[('A',(4,30),3,3,True),('L',(4,25)),('A',(8,21),4,4,True),('L',(10,21)),('L',(17,12)),('C',(21,10),(18,10),(19,10)),('L',(27,10)),('C',(31,12),(29,10),(30,11)),('L',(36,19)),('L',(40,20)),('C',(44,25),(43,21),(44,22)),('L',(44,30)),('A',(41,33),3,3,True)])

        for x in (12,36):circle(f'wheel-{x}',x,33,5)
        line('sill',(17,33),(31,33));join('sill','wheel-12');join('sill','wheel-36')
        join('body','wheel-12');join('body','wheel-36')
