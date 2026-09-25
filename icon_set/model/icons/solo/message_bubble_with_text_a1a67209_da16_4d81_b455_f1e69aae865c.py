"""message-bubble-with-text: A smooth oval chat bubble owns a lower-left tail and three evenly spaced centered text lines.
Lucide construction: message-circle; original and atomic-debug inspected.
Omissions: None
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a1a67209-da16-4d81-b455-f1e69aae865c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__message-bubble-with-text/20260924T171114Z-thuan-mac/reference/messages bubble text 1_a1a67209-da16-4d81-b455-f1e69aae865c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'message-bubble-with-text'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('message', 'bubble', 'with', 'text')
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

        path('outline',(6,23),[('A',(24,6),18,17,True),('A',(42,23),18,17,True),('A',(24,40),18,17,True),('C',(15,38),(20,40),(17,39)),('L',(7,42)),('L',(10,32)),('C',(6,23),(7,29),(6,26))],True)
        for name,y,x0,x1 in [('top',15,20,28),('middle',23,16,32),('bottom',31,20,28)]:line('text-'+name,(x0,y),(x1,y))
