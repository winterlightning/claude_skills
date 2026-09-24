"""Restore a camper window and sloped windshield, rounded cabin corners and distinct equal circular wheels.
Construction: Lucide caravan/truck: rounded chassis and separate circular wheels.
Omissions: Interior furnishing omitted.
Keyshape SQUARE: authored to exact SOLO48 extremes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '67545933-613d-5320-bb66-9887235b5423'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__camper-van/20260924T115444Z-thuan-mac/reference/camping rv_67545933-613d-5320-bb66-9887235b5423.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'camper-van'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = ('camper', 'van')
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

        path('body',(10,38),[('A',(6,34),4,4,True),('L',(6,10)),('A',(10,6),4,4,True),('L',(32,6)),('C',(36,11),(34,6),(35,8)),('L',(40,23)),('C',(42,28),(42,24),(42,25)),('L',(42,34)),('A',(38,38),4,4,True)])
        for x in (14,34):circle(f'wheel-{x}',x,38,4);join('body',f'wheel-{x}')
        line('sill',(18,38),(30,38));join('sill','wheel-14');join('sill','wheel-34')
        poly('window',(15,15),(23,15),(23,23),(15,23),closed=True)
        poly('windshield',(32,6),(32,23),(40,23));join('windshield','body')
