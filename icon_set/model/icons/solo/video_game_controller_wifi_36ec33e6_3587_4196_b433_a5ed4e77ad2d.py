"""video game controller wifi.
Two Wi-Fi bands above a symmetric controller.
Square; bands share axis24 and cardinal ellipse endpoints.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '36ec33e6-3587-4196-b433-a5ed4e77ad2d'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_39/video game controller wifi_36ec33e6-3587-4196-b433-a5ed4e77ad2d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'video-game-controller-wifi'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('video', 'game', 'controller', 'wifi')

    def path(self, name, start, operations, closed=False):
        # A coherent path owns its members exactly once.
        current=start; members=[]
        for i,op in enumerate(operations):
            n=f'{name}-{i}'
            if op[0]=='L':
                end=op[1]; self.add_line(n,current,end)
            elif op[0]=='A':
                end,rx,ry,sweep=op[1:]; self.add_arc(n,current,end,radius_x=rx,radius_y=ry,sweep=sweep)
            else:
                c1,c2,end=op[1:]; self.add_bezier(n,current,(c1,c2,end))
            members.append(n);current=end
        if closed and current!=start:
            n=f'{name}-close';self.add_line(n,current,start);members.append(n)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

    def rect(self,name,x,y,w,h,r=4,split_x=(),split_y=()):
        ops=[]
        for xx in sorted(v for v in split_x if x+r<v<x+w-r): ops.append(('L',(xx,y)))
        ops += [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True)]
        for yy in sorted(v for v in split_y if y+r<v<y+h-r): ops.append(('L',(x+w,yy)))
        ops += [('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True)]
        for xx in sorted((v for v in split_x if x+r<v<x+w-r),reverse=True): ops.append(('L',(xx,y+h)))
        ops += [('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True)]
        for yy in sorted((v for v in split_y if y+r<v<y+h-r),reverse=True): ops.append(('L',(x,yy)))
        ops += [('L',(x,y+r)),('A',(x+r,y),r,r,True)]
        # Capsules can have zero-length straight runs; omit those.
        cleaned=[];p=(x+r,y)
        for op in ops:
            if op[0]!='L' or op[1]!=p: cleaned.append(op)
            p=op[1]
        self.path(name,(x+r,y),cleaned,True)

    def join(self,*names):
        for i,a in enumerate(names):
            for b in names[i+1:]: self.relate('connect',a,b)

    def cross(self,name,x,y,r,diagonal=False):
        offsets=[(-r,-r),(r,r),(-r,r),(r,-r)] if diagonal else [(-r,0),(r,0),(0,-r),(0,r)]
        names=[]
        for i,(dx,dy) in enumerate(offsets):
            n=f'{name}-{i}';self.add_line(n,(x,y),(x+dx,y+dy));names.append(n)
        self.join(*names)

    def letter_a(self,name,apex,left,right,bar_left,bar_right):
        self.add_polyline(name,left,bar_left,apex,bar_right,right)
        self.add_line(name+'-bar',bar_left,bar_right)
        self.join(name,name+'-bar')

    def build(self) -> None:
        self.add_arc('wifi-outer',(10,12),(38,12),radius_x=14,radius_y=6)
        self.add_arc('wifi-inner',(16,20),(32,20),radius_x=8,radius_y=4)
        self.path('controller',(12,30),[('L',(36,30)),('A',(42,36),6,6,True),('A',(36,42),6,6,True),('L',(32,38)),('L',(16,38)),('L',(12,42)),('A',(6,36),6,6,True),('A',(12,30),6,6,True)],True)

# Repair plan: Two Wi-Fi bands above a symmetric controller.
# Omissions: Third Wi-Fi band and button details omitted.
# Construction references: Lucide gamepad-2 original and atomic-debug: paired grip geometry.
# Keyshape and proportions: Square; bands share axis24 and cardinal ellipse endpoints.
