"""A clipped-corner test sheet contains A and B answer rows.
Plan: One page outline encloses two hand-authored letters and repeated answer rules.
Keyshape: VRECT_L. Exact envelope: {'ink': [6, 2, 42, 46], 'centerline': [8, 4, 40, 44]}.
Construction references: icon_set/references/lucide/original/file.svg and atomic-debug/file.svg: coherent contours, shared junctions, and consistent rounding; re-authored on SOLO48.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f799a4bf-12e6-4111-a7f7-3023b0c48446'
SOURCE_PATH = 'pictographic-primitives/other/test file_f799a4bf-12e6-4111-a7f7-3023b0c48446.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'test-file'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('test', 'file')

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
        # Round-topped A and full-size B counters repair the tiny holes.
        self.rect('page',8,4,32,40,4)
        self.add_polyline('a-left',(17,22),(17,18),(17,14))
        self.add_arc('a-cap',(17,14),(25,14),radius_x=4)
        self.add_polyline('a-right',(25,14),(25,18),(25,22))
        self.add_line('a-bar',(17,18),(25,18))
        for n in ['a-left','a-right']:
            self.relate('connect',n,'a-cap');self.relate('connect',n,'a-bar')
        self.add_polyline('b-stem',(17,28),(17,36),(17,44))
        self.add_arc('b-upper',(17,28),(17,36),radius_x=8,radius_y=4)
        self.add_arc('b-lower',(17,36),(17,44),radius_x=8,radius_y=4)
        self.relate('connect','b-stem','b-upper','b-lower')
        for i,y in enumerate((20,32)):self.add_line(f'answer-{i}',(31,y),(32,y))
