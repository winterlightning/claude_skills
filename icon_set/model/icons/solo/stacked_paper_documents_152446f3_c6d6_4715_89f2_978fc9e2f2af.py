"""stacked-paper-documents-solo: Two staggered sheets with straight diagonal cut corners and matching rounded outer corners; rear outline stops at the front sheet.
Lucide construction: files; original and atomic-debug inspected.
Omissions: None
Keyshape VRECT_L: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '152446f3-c6d6-4715-89f2-978fc9e2f2af'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__stacked-paper-documents-solo/20260924T171114Z-thuan-mac/reference/files_152446f3-c6d6-4715-89f2-978fc9e2f2af.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'stacked-paper-documents-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('stacked', 'paper', 'documents', 'solo')
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

        path('front',(11,14),[('L',(24,14)),('L',(32,22)),('L',(32,34)),('L',(32,41)),('A',(29,44),3,3,True),('L',(11,44)),('A',(8,41),3,3,True),('L',(8,17)),('A',(11,14),3,3,True)],True)
        path('back',(16,14),[('L',(16,7)),('A',(19,4),3,3,True),('L',(31,4)),('L',(40,13)),('L',(40,31)),('A',(37,34),3,3,True),('L',(32,34))]);join('front','back')
