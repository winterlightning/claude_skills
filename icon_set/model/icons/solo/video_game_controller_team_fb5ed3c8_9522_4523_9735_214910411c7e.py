"""Three teammates stand above a game controller.
Plan: Repeated circular heads and shallow shoulder curves precede a shared controller outline.
Keyshape SQUARE: {'ink': [4, 4, 44, 44], 'centerline': [6, 6, 42, 42]}.
Human spacing: Three detached busts: head centers (12,9), (24,9), (36,9), radius3; lower head centerline y12 and own shoulder apex y20 give exactly8 centerline /4 ink units. Neighboring heads remain too close (6 centerline units). These are shoulder busts rather than stick figures.
References: Supplied SVG rendered and inspected. Lucide original/gamepad-2.svg and atomic-debug/gamepad-2.svg: coherent contours, repeated radii and explicit shared junctions, freshly authored for SOLO48. human-reference.md, human_ref/user.svg and full_body_ref.png: circular heads, consistent limbs, aligned torso and exact 4-unit detached-head ink gap.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fb5ed3c8-9522-4523-9735-214910411c7e'
SOURCE_PATH = 'icon_set/work/todo-references/video game controller team_fb5ed3c8-9522-4523-9735-214910411c7e.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'video-game-controller-team'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('video', 'game', 'controller', 'team')

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

        for i,x in enumerate((12,24,36)):
            self.circle(f'head-{i}',x,9,3)
            self.add_bezier(f'shoulders-{i}',(x-6,23),((x-4,20),(x-2,20),(x,20)),((x+2,20),(x+4,20),(x+6,23)))

        self.path('controller',(14,28),[('L',(34,28)),('A',(42,36),8,8,True),('L',(42,38)),('C',(42,42),(38,42),(35,39)),('L',(31,36)),('L',(17,36)),('L',(13,39)),('C',(10,42),(6,42),(6,38)),('L',(6,36)),('A',(14,28),8,8,True)],True)
        self.cross('d-pad',14,33,3)
        self.add_dot('button',(34,32))
