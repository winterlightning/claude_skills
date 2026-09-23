"""Two seated people wait beneath a clock.
Plan: Paired circular heads align with their torso starts; two distinct seated leg arrangements preserve the scene.
Keyshape SQUARE: {'ink': [4, 4, 44, 44], 'centerline': [6, 6, 42, 42]}.
Human spacing: Both stick figures: heads centered (24,16) and (36,16), radius3, torso starts at (24,27) and (36,27). Each aligned head-to-torso centerline gap is 27-(16+3)=8, leaving exactly4 ink units. The recorded human flags name these actual torso starts. Clock and inter-person clearances fail independently.
References: Supplied SVG rendered and inspected. human-reference.md, human_ref/user.svg and full_body_ref.png: circular heads, consistent limbs, aligned torso and exact 4-unit detached-head ink gap.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '18363920-a131-4703-9250-544ef6984fd4'
SOURCE_PATH = 'icon_set/work/todo-references/waiting room couple_18363920-a131-4703-9250-544ef6984fd4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'waiting-room-couple'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('waiting', 'room', 'couple')

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

        self.circle('clock',12,12,6);self.add_polyline('clock-hands',(12,9),(12,12),(15,12))
        for i,x in enumerate((24,36)):
            self.circle(f'head-{i}',x,16,3)
            self.add_line(f'torso-{i}',(x,27),(x,34))
            self.mark_human_figure(f'person-{i}',head=f'head-{i}',torso=f'torso-{i}',torso_junction='start')
        self.add_polyline('legs-left',(24,34),(20,34),(18,34),(14,42));self.join('torso-0','legs-left')
        self.add_line('lower-left',(20,34),(20,42));self.join('legs-left','lower-left')
        self.add_polyline('legs-right',(36,34),(42,34),(42,42));self.join('torso-1','legs-right')
