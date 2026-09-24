"""A Thaipusam spearhead contains a scalloped central emblem and triangular base.
Plan: The outer teardrop and center emblem mirror about x24; the base forms a deliberate angular junction.
Keyshape: VRECT_L. Exact envelope: {'ink': [6, 2, 42, 46], 'centerline': [8, 4, 40, 44]}.
Construction references: No useful local Lucide subject match found; shared geometric construction principles used.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd6a78037-29f1-4227-a0c5-2e4158ef4f53'
SOURCE_PATH = 'icon_set/work/todo-references/thaipusam 1_d6a78037-29f1-4227-a0c5-2e4158ef4f53.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'thaipusam-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('thaipusam', '1')

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

        self.path('spearhead',(24,4),[('C',(32,10),(40,20),(40,28)),('C',(40,36),(34,41),(30,44)),('L',(18,44)),('C',(14,41),(8,36),(8,28)),('C',(8,20),(16,10),(24,4))],True)
        self.add_polyline('base-triangle',(18,44),(24,38),(30,44));self.join('spearhead','base-triangle')
        self.path('emblem',(20,18),[('L',(28,18)),('A',(31,21),3,3,True),('C',(31,23),(29,23),(31,26)),('C',(29,29),(31,29),(31,31)),('A',(28,34),3,3,True),('L',(20,34)),('A',(17,31),3,3,True),('C',(17,29),(19,29),(17,26)),('C',(19,23),(17,23),(17,21)),('A',(20,18),3,3,True)],True)
