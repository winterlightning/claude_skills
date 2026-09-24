"""eggplant: One broad curved fruit body joins an asymmetric leaf cap and diagonal stalk with shared nodes.
Lucide construction: sprout; original and atomic-debug inspected.
Omissions: None
Keyshape HRECT_L: exact contract envelope; 4-unit stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '37dde66a-a1c3-4b6d-bf1d-a49fc7e5c370'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__eggplant/20260924T165054Z-thuan-mac/reference/eggplant_37dde66a-a1c3-4b6d-bf1d-a49fc7e5c370.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'eggplant'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('eggplant',)
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

        path('body',(28,14),[('C',(14,22),(24,19),(21,22)),('C',(4,31),(8,22),(4,25)),('C',(15,40),(4,37),(9,40)),('C',(39,25),(24,40),(34,32))])
        path('cap',(28,14),[('C',(40,10),(28,8),(36,8)),('C',(40,26),(45,13),(43,20)),('C',(34,16),(36,24),(34,20)),('C',(28,14),(31,17),(29,16))],True)
        line('stalk',(40,10),(44,8));join('stalk','cap');join('body','cap')
