"""seated-teddy-bear: A vertically symmetric teddy with rounded ears, broad head and paired seated feet is built from mirrored curves.
Lucide construction: none; original and atomic-debug inspected.
Omissions: Inner ear loops and finger seams omitted; two rounded feet retained.
Keyshape VRECT_L: exact contract envelope; 4-unit stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd06262b9-37c7-4bc4-9fe3-489ad5036090'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-teddy-bear/20260924T171114Z-thuan-mac/reference/teddy bear_d06262b9-37c7-4bc4-9fe3-489ad5036090.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'seated-teddy-bear'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('seated', 'teddy', 'bear')
    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,start,end)
                elif kind=='A': self.add_arc(ident,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,start,(args[0],args[1],end))
                members.append(ident);start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx,cy-ry),[('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True),('A',(cx,cy-ry),rx,ry,True)],True)
        def rect(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('head',(14,14),[('C',(10,8),(11,14),(10,11)),('C',(14,4),(10,6),(12,4)),('C',(18,8),(16,4),(18,6)),('C',(30,8),(22,7),(26,7)),('C',(34,4),(30,6),(32,4)),('C',(38,8),(36,4),(38,6)),('C',(34,14),(38,11),(37,14)),('C',(24,26),(34,21),(30,26)),('C',(14,14),(18,26),(14,21))],True)
        path('body',(24,26),[('L',(34,26)),('C',(40,34),(38,26),(40,30)),('L',(40,38)),('A',(28,38),6,6,True),('L',(28,36)),('L',(20,36)),('L',(20,38)),('A',(8,38),6,6,True),('L',(8,34)),('C',(14,26),(8,30),(10,26)),('L',(24,26))],True);join('body','head')
