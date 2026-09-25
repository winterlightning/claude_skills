"""open-paper-booklet: A rounded front cover and raised back leaf with a smooth upper corner share the binding nodes.
Lucide construction: book-open; original and atomic-debug inspected.
Omissions: None
Keyshape VRECT_M: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ee58df5-c0c8-43b8-ac76-5d6d676e8615'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-paper-booklet/20260924T171114Z-thuan-mac/reference/booklet_9ee58df5-c0c8-43b8-ac76-5d6d676e8615.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'open-paper-booklet'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('open', 'paper', 'booklet')
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

        path('front',(10,16),[('L',(34,16)),('A',(38,20),4,4,True),('L',(38,40)),('A',(34,44),4,4,True),('L',(14,44)),('A',(10,40),4,4,True),('L',(10,16))],True)
        path('back',(10,16),[('L',(28,5)),('C',(32,4),(30,4),(31,4)),('C',(34,8),(34,4),(34,6)),('L',(34,16))]);join('front','back')
