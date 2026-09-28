"""More natural meaty diagonal taper, rounded bone and two clear bite scallops.
Plan: coherent named contours and repeated dimensions. SQUARE natural subject envelope.
Construction reference: Lucide drumstick: broad meat and rounded bone.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9a208e68-7ddc-4cbb-b3ca-7480f19c88c8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chicken-drumstick-with-bitten-upper-edge/20260925T070532Z-thuan-mac/reference/drumstick bite_9a208e68-7ddc-4cbb-b3ca-7480f19c88c8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chicken-drumstick-with-bitten-upper-edge'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('drumstick', 'bite')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=3):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('drumstick',(8,33),[('C',(17,21),(13,31),(14,26)),('C',(29,6),(21,14),(24,6)),('L',(34,6)),('C',(36,15),(32,11),(32,15)),('C',(42,22),(34,20),(37,24)),('C',(23,33),(38,28),(28,30)),('C',(15,42),(19,36),(19,42)),('C',(10,40),(12,42),(11,42)),('C',(6,36),(6,40),(6,38)),('C',(8,33),(6,34),(7,33))],True)
