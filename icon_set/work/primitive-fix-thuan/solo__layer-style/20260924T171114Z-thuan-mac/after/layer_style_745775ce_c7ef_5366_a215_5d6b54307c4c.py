"""layer-style: Italic f with smooth terminal transitions and a separate symmetric x; crossing halves reuse one node.
Lucide construction: none; original and atomic-debug inspected.
Omissions: None
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '745775ce-c7ef-5366-a215-5d6b54307c4c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__layer-style/20260924T171114Z-thuan-mac/reference/layer style_745775ce-c7ef-5366-a215-5d6b54307c4c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'layer-style'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('layer', 'style')
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

        path('f',(6,42),[('C',(14,34),(11,42),(13,39)),('L',(18,18)),('L',(19,14)),('C',(28,6),(20,8),(23,6)),('L',(30,6))])
        poly('bar',(12,18),(18,18),(23,18));join('bar','f')
        # The f stem is split at its actual bar junction below.
        poly('x-down',(30,22),(36,30),(42,38));poly('x-up',(30,38),(36,30),(42,22));join('x-down','x-up')
