"""crop-rotate: Two crossing crop corners retain exact right angles; opposite quarter-turn arrows use matched arcs and open chevrons.
Lucide construction: crop; original and atomic-debug inspected.
Omissions: None
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b05e7a98-e0c7-5855-a771-4dc4b12ff639'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crop-rotate/20260924T172457Z-thuan-mac/reference/crop rotate_b05e7a98-e0c7-5855-a771-4dc4b12ff639.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'crop-rotate'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('crop', 'rotate')
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

        poly('crop-left',(20,6),(20,20),(20,28),(28,28),(42,28))
        poly('crop-right',(6,20),(20,20),(28,20),(28,28),(28,42));join('crop-left','crop-right')
        path('top',(42,18),[('A',(30,10),12,8,False)])
        poly('top-head',(34,6),(30,10),(34,14));join('top','top-head')
        path('bottom',(6,30),[('A',(18,38),12,8,False)])
        poly('bottom-head',(14,34),(18,38),(14,42));join('bottom','bottom-head')
