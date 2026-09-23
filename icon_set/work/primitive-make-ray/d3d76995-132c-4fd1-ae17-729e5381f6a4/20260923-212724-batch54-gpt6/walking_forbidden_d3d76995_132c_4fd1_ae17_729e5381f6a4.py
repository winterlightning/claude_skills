"""A walking figure is crossed by a prohibition slash inside a circle.
Plan: A circular sign owns its diagonal slash; the figure uses an aligned circular head and segmented torso.
Keyshape CIRCLE: {'center': [24, 24], 'ink_radius': 22, 'centerline_radius': 20}.
Human spacing: Walking figure: head (24,12), radius3, upper torso starts (24,23), giving 23-(12+3)=8 centerline /4 ink units at the aligned torso junction. However, the arm segment (20,22)-(24,23) is closer: center-to-segment distance44/sqrt(17), so the head-to-arm ink gap is44/sqrt(17)-3-4 = approximately3.672 units. Thus the full head-to-body requirement is NOT met; no human visual approval is claimed. The figure flag records the torso junction, not a clearance waiver.
References: Supplied SVG rendered and inspected. human-reference.md, human_ref/user.svg and full_body_ref.png: circular heads, consistent limbs, aligned torso and exact 4-unit detached-head ink gap.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd3d76995-132c-4fd1-ae17-729e5381f6a4'
SOURCE_PATH = 'icon_set/work/todo-references/walking forbidden_d3d76995-132c-4fd1-ae17-729e5381f6a4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'walking-forbidden'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('walking', 'forbidden')

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

        self.path('sign',(12,8),[('A',(36,40),20,20,True),('A',(12,8),20,20,True)],True)
        self.add_line('slash',(12,8),(36,40));self.join('sign','slash')
        self.circle('head',24,12,3)
        self.add_line('torso',(24,23),(24,27))
        self.add_line('hip',(24,27),(22,30));self.join('torso','hip')
        self.add_polyline('arms',(18,25),(20,22),(24,23),(30,26),(34,26));self.join('arms','torso')
        self.add_polyline('legs',(18,36),(22,30),(28,32),(30,38));self.join('hip','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
