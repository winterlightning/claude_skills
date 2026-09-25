"""simple-home-icon: A symmetric closed home-like upward outline has matching 45-degree roof slopes, a smooth rounded apex and equal lower corner radii.
Lucide construction: house; original and atomic-debug inspected.
Omissions: None
Keyshape VRECT_L: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5cb31408-59f1-4f35-b964-02c5190426a4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__simple-home-icon/20260924T171114Z-thuan-mac/reference/arrow up 3_5cb31408-59f1-4f35-b964-02c5190426a4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'simple-home-icon'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('simple', 'home', 'icon')
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

        path('home',(8,20),[('L',(22,6)),('C',(24,4),(23,5),(23,4)),('C',(26,6),(25,4),(25,5)),('L',(40,20)),('L',(40,41)),('A',(37,44),3,3,True),('L',(11,44)),('A',(8,41),3,3,True),('L',(8,20))],True)
