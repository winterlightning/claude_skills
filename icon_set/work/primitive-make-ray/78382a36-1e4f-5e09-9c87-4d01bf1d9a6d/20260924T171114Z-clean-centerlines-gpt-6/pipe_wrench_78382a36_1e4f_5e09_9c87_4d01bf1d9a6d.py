"""pipe-wrench: A diagonal wrench with a rounded open jaw and broad rounded handle replaces the rejected upright block; diagonal perspective follows the original.
Lucide construction: wrench; original and atomic-debug inspected.
Omissions: Fine screw ridges and jaw seam omitted to leave a readable open jaw and handle.
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '78382a36-1e4f-5e09-9c87-4d01bf1d9a6d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pipe-wrench/20260924T171114Z-thuan-mac/reference/tools vice grip_78382a36-1e4f-5e09-9c87-4d01bf1d9a6d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'pipe-wrench'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('pipe', 'wrench')
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

        path('wrench',(22,22),[('L',(8,36)),('C',(6,39),(6,38),(6,38)),('C',(14,42),(6,41),(10,42)),('C',(19,40),(16,42),(18,41)),('L',(32,27)),('C',(42,16),(37,28),(42,22)),('C',(32,6),(42,10),(38,6)),('C',(25,8),(29,6),(27,7)),('L',(32,15)),('L',(25,22)),('L',(18,15)),('C',(22,22),(17,18),(19,21))],True)
