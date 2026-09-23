"""A companion cube face has four corner blocks and a central heart medallion.
Plan: Four identical corner blocks, four narrow connector blocks and a circular heart center form a square assembly.
Keyshape SQUARE: {'ink': [4, 4, 44, 44], 'centerline': [6, 6, 42, 42]}.
References: Supplied SVG rendered and inspected. No useful local Lucide subject match used; geometric reconstruction follows the supplied drawing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6e798969-b8c1-4108-aa25-07455cf19213'
SOURCE_PATH = 'icon_set/work/todo-references/video game logo companion cube_6e798969-b8c1-4108-aa25-07455cf19213.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'video-game-logo-companion-cube'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('video', 'game', 'logo', 'companion', 'cube')

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

        for i,(x,y) in enumerate(((6,6),(32,6),(6,32),(32,32))):self.rect(f'corner-{i}',x,y,10,10,2)
        self.rect('top-connector',20,8,8,4,1);self.rect('bottom-connector',20,36,8,4,1)
        self.rect('left-connector',8,20,4,8,1);self.rect('right-connector',36,20,4,8,1)
        for name,a,b in [('top-left',(16,10),(20,10)),('top-right',(28,10),(32,10)),('bottom-left',(16,38),(20,38)),('bottom-right',(28,38),(32,38)),('left-top',(10,16),(10,20)),('left-bottom',(10,28),(10,32)),('right-top',(38,16),(38,20)),('right-bottom',(38,28),(38,32))]:self.add_line(name,a,b)
        self.circle('medallion',24,24,9)
        self.path('heart',(24,29),[('L',(20,25)),('C',(17,22),(21,19),(24,22)),('C',(27,19),(31,22),(28,25)),('L',(24,29))],True)
