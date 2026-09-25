"""rotate-front: Two overlapping square tiles sit below a double-ended quarter-circle rotation arrow; rounded tile corners and exact shared joins.
Lucide construction: rotate-cw; original and atomic-debug inspected.
Omissions: None
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7dc295ff-87b1-4670-860d-c8009a0aa7e1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rotate-front/20260924T171114Z-thuan-mac/reference/rotate front_7dc295ff-87b1-4670-860d-c8009a0aa7e1.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'rotate-front'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('rotate', 'front')
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

        path('front',(9,18),[('L',(19,18)),('A',(22,21),3,3,True),('L',(22,31)),('A',(19,34),3,3,True),('L',(16,34)),('L',(9,34)),('A',(6,31),3,3,True),('L',(6,21)),('A',(9,18),3,3,True)],True)
        path('back',(22,31),[('L',(39,31)),('A',(42,34),3,3,True),('L',(42,39)),('A',(39,42),3,3,True),('L',(19,42)),('A',(16,39),3,3,True),('L',(16,34))]);join('front','back')
        path('rotation',(26,10),[('A',(38,22),12,12,True)])
        poly('start',(30,6),(26,10),(30,14));poly('end',(34,18),(38,22),(42,18));join('rotation','start');join('rotation','end')
