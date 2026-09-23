"""An eye sheds a tear above a tear-gas canister and drifting gas.
Plan: Four semantic groups retain the source positions: eye, tear, horizontal canister, and two-part gas cloud.
Keyshape: SQUARE. Exact envelope: {'ink': [4, 4, 44, 44], 'centerline': [6, 6, 42, 42]}.
Construction references: No useful local Lucide subject match found; shared geometric construction principles used.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8f58894e-3584-4d7e-9183-ffe9e81333d8'
SOURCE_PATH = 'icon_set/work/todo-references/tools tear gas_8f58894e-3584-4d7e-9183-ffe9e81333d8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tools-tear-gas'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('tools', 'tear', 'gas')

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

    def build(self):

        self.add_arc('eye-upper',(6,14),(28,14),radius_x=11,radius_y=8)
        self.add_bezier('eye-lower',(28,14),((26,19),(22,22),(18,22)));self.join('eye-upper','eye-lower')
        self.circle('pupil',16,13,3)
        self.path('tear',(11,19),[('C',(9,23),(7,25),(7,28)),('A',(15,28),4,4,False),('C',(15,25),(13,23),(11,19))],True)
        self.rect('canister',6,32,18,10,3,split_y=(35,39))
        self.add_polyline('nozzle',(24,35),(28,35),(28,39),(24,39));self.join('canister','nozzle')
        self.path('gas',(34,26),[('C',(30,26),(28,24),(30,21)),('C',(27,18),(29,12),(34,10)),('C',(38,8),(42,12),(42,16)),('C',(42,20),(38,22),(36,22)),('C',(36,25),(35,26),(34,26))],True)
        self.circle('gas-dot',32,31,2)
