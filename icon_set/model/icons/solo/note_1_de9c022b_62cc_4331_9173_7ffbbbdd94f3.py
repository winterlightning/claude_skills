"""note-1: A symmetric blank clipboard uses a centered capsule clip and identical tangent board corners.
Lucide construction: clipboard; original and atomic-debug inspected.
Omissions: None
Keyshape VRECT_L: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'de9c022b-62cc-4331-9173-7ffbbbdd94f3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__note-1/20260924T171114Z-thuan-mac/reference/note 1_de9c022b-62cc-4331-9173-7ffbbbdd94f3.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'note-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('note', '1')
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

        path('clip',(20,4),[('L',(28,4)),('A',(32,8),4,4,True),('A',(28,12),4,4,True),('L',(20,12)),('A',(16,8),4,4,True),('A',(20,4),4,4,True)],True)
        path('board',(16,8),[('L',(12,8)),('A',(8,12),4,4,False),('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,12)),('A',(36,8),4,4,False),('L',(32,8))]);join('board','clip')
