"""Two people face off above a game controller.
Plan: Identical head and shoulder definitions flank a centered controller.
Keyshape: SQUARE. Exact envelope: {'ink': [4, 4, 44, 44], 'centerline': [6, 6, 42, 42]}.
Human spacing: Two detached bust heads: centers (13,11) and (35,11), radius5; lower head centerline y16 and shoulder apex y24 give exactly 8 centerline units /4 ink units. Equal circular shoulder quarters preserve paired proportions. These are bust contours, not stick figures.
Construction references: icon_set/references/human_ref/user.svg and full_body_ref.png: circular heads, smooth shoulders, coherent limb strokes and exact detached-head spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5bac2074-ad7e-4c93-acd8-d73142b163b6'
SOURCE_PATH = 'icon_set/work/todo-references/team vs team mode_5bac2074-ad7e-4c93-acd8-d73142b163b6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'team-vs-team-mode'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('team', 'vs', 'team', 'mode')

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

        for i,x in enumerate((13,35)):
            self.circle(f'head-{i}',x,11,5)
            # Head lower y16, shoulder apex y24: exact detached 4-unit ink gap.
            self.path(f'body-{i}',(x-7,31),[('A',(x,24),7,7,True),('A',(x+7,31),7,7,True)])
        self.path('controller',(18,32),[('L',(30,32)),('C',(33,32),(33,34),(34,37)),('L',(36,40)),('C',(36,43),(32,42),(30,39)),('L',(18,39)),('C',(16,42),(12,43),(12,40)),('L',(14,35)),('C',(15,32),(16,32),(18,32))],True)
        self.add_polyline('controller-v',(21,34),(24,38),(27,34))
