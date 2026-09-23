"""A raised index finger selects a floating cube.
Plan: Isometric cube at upper left; one coherent pointing-hand silhouette at lower right.
Keyshape: SQUARE. Exact envelope: {'ink': [4, 4, 44, 44], 'centerline': [6, 6, 42, 42]}.
Construction references: icon_set/references/lucide/original/hand.svg and atomic-debug/hand.svg: coherent contours, shared junctions, and consistent rounding; re-authored on SOLO48.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '505403c5-6a6b-4a09-8ee4-eac7ce3a505f'
SOURCE_PATH = 'icon_set/work/todo-references/technology ar searching finger touch_505403c5-6a6b-4a09-8ee4-eac7ce3a505f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'technology-ar-searching-finger-touch'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('technology', 'ar', 'searching', 'finger', 'touch')

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

        self.add_polyline('cube-top',(6,12),(18,6),(30,12),(18,18),(6,12))
        self.add_polyline('cube-left',(6,12),(6,24),(18,30),(18,18))
        self.add_line('cube-right',(30,12),(30,18))
        self.add_line('cube-bottom',(18,30),(22,28))
        self.join('cube-top','cube-left');self.join('cube-top','cube-right');self.join('cube-left','cube-bottom')
        self.path('hand',(24,42),[('L',(19,35)),('C',(17,31),(21,29),(24,32)),('L',(28,36)),('L',(28,24)),('A',(36,24),4,4,True),('L',(36,32)),('L',(38,32)),('A',(42,36),4,4,True),('L',(42,42))])
