"""A tire-pressure warning outline encloses a vertical warning stroke.
Plan: Mirrored throat caps lead into a broad U-shaped bulb; paired lower stems stay aligned.
Keyshape: VRECT_L. Exact envelope: {'ink': [6, 2, 42, 46], 'centerline': [8, 4, 40, 44]}.
Construction references: No useful local Lucide subject match found; shared geometric construction principles used.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '992df6cb-53a3-42d8-b584-7ec4584f57b0'
SOURCE_PATH = 'icon_set/work/todo-references/tire pressure warning_992df6cb-53a3-42d8-b584-7ec4584f57b0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tire-pressure-warning'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('tire', 'pressure', 'warning')

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

        self.path('tire',(12,8),[('A',(20,8),4,4,True),('L',(20,14)),('C',(20,20),(16,22),(16,27)),('C',(16,32),(19,34),(24,34)),('C',(29,34),(32,32),(32,27)),('C',(32,22),(28,20),(28,14)),('L',(28,8)),('A',(36,8),4,4,True),('C',(36,18),(40,20),(40,28)),('C',(40,36),(34,40),(28,40)),('L',(20,40)),('C',(14,40),(8,36),(8,28)),('C',(8,20),(12,18),(12,8))],True)
        self.add_line('warning',(24,15),(24,23))
        for name,x in [('stem-left',20),('stem-right',28)]:
            self.add_line(name,(x,40),(x,44));self.join('tire',name)
