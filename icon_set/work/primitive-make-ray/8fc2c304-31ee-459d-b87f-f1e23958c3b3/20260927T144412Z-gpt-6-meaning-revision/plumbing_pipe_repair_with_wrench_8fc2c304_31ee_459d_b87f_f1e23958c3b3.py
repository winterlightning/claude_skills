"""plumbing-pipe-repair-with-wrench: An elbow pipe, teardrop and diagonal repair wrench retain the three-part composition; rounded elbows and smooth drop replace polygonal bends.
Lucide construction: wrench; original and atomic-debug inspected.
Omissions: Tiny jaw screw and handle outline reduced to clean centerline strokes.
Keyshape HRECT_L: exact contract envelope; 4-unit stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8fc2c304-31ee-459d-b87f-f1e23958c3b3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__plumbing-pipe-repair-with-wrench/20260927T144036Z-thuan-mac-1/reference/home improvement 14_8fc2c304-31ee-459d-b87f-f1e23958c3b3.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'plumbing-pipe-repair-with-wrench'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('plumbing', 'pipe', 'repair', 'with', 'wrench')
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

        path('pipe',(44,12),[('L',(18,12)),('L',(18,8)),('L',(8,8)),('A',(4,12),4,4,False),('L',(4,16)),('A',(8,20),4,4,False),('L',(44,20))])
        path('drop',(10,28),[('C',(16,35),(13,31),(16,33)),('C',(10,40),(16,38),(13,40)),('C',(4,35),(7,40),(4,38)),('C',(10,28),(4,33),(7,31))],True)
        poly('jaw-left',(24,29),(24,31),(28,35),(32,35))
        poly('jaw-right',(36,29),(36,31),(32,35))
        line('handle',(32,35),(44,40))
        join('jaw-left','jaw-right');join('jaw-left','handle');join('jaw-right','handle')
