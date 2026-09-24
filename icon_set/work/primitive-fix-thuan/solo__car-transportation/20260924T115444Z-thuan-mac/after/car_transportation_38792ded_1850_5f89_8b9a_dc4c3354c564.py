"""Restore the broad van-like cabin, short door handle, lower hood and separate circular wheels.
Construction: Lucide car: simplified continuous roof/hood and rounded wheels.
Omissions: None
Keyshape HRECT_M: authored to exact SOLO48 extremes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '38792ded-1850-5f89-8b9a-dc4c3354c564'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-transportation/20260924T115444Z-thuan-mac/reference/car_38792ded-1850-5f89-8b9a-dc4c3354c564.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'car-transportation'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = ('car', 'transportation')
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

        path('body',(7,33),[('A',(4,30),3,3,True),('L',(4,21)),('L',(10,12)),('C',(14,10),(11,10),(12,10)),('L',(25,10)),('C',(29,12),(27,10),(28,11)),('L',(37,20)),('C',(44,25),(42,21),(44,21)),('L',(44,30)),('A',(41,33),3,3,True)])
        line('handle',(18,21),(22,21))

        for x in (12,36):circle(f'wheel-{x}',x,33,5)
        line('sill',(17,33),(31,33));join('sill','wheel-12');join('sill','wheel-36')
        join('body','wheel-12');join('body','wheel-36')
