"""A person sits correctly on a toilet beside a check mark.
Plan: Seated torso axis sets the circular head; an angled shin and folded arm retain the correct-use pose.
Keyshape: SQUARE. Exact envelope: {'ink': [4, 4, 44, 44], 'centerline': [6, 6, 42, 42]}.
Human spacing: Head center (23,11), radius5; neck (18,23), hip (13,35). Center-to-neck vector (5,-12) has length13 and is collinear with the upper torso axis. Outline-to-neck distance13-5=8, leaving exactly4 ink units. The torso continues away from the head, and the arm also moves away. mark_human_figure records the actual torso start.
Construction references: icon_set/references/human_ref/user.svg and full_body_ref.png: circular heads, smooth shoulders, coherent limb strokes and exact detached-head spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2dff611f-5296-466d-ac68-3fd4303496ea'
SOURCE_PATH = 'icon_set/work/todo-references/toilet use right_2dff611f-5296-466d-ac68-3fd4303496ea.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'toilet-use-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('toilet', 'use', 'right')

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

        self.circle('head',23,11,5)
        self.add_line('torso',(18, 23),(13, 35))
        self.add_polyline('leg',(13, 35),(31,35),(37, 42))
        self.join('torso','leg')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.add_polyline('toilet',(6,42),(6,24),(10,24),(10,36),(26,36))
        self.add_bezier('bowl',(26,36),((26,40),(20,40),(20,42)))
        self.join('toilet','bowl')

        self.add_polyline('arm',(18,23),(28,30),(22,32));self.join('torso','arm')
        self.add_polyline('check',(33,12),(37,16),(42,6))
