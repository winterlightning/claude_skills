"""veterinarian.
Plan: Restore stethoscope tube and circular bell from shoulder endpoint. Shared human user.svg proportions: circular head bottom18, shoulders top26, exact four-unit ink gap. Omit collar, body baseline and badge rim; retain clinician and cat.
Fresh SOLO48 repair. Shared human reference applies to people.
Lucide trash-2 informs simple lid and rounded bin construction where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='16ebf22c-f2dd-4834-bf5b-3033fd6dbd8a'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/veterinarian_16ebf22c-f2dd-4834-bf5b-3033fd6dbd8a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='veterinarian'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('veterinarian',)
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
        self.circle('head',14,12,6)
        self.path('shoulders',(6,42),[('L',(6,34)),('A',(14,26),8,8,True),('L',(18,26))])
        self.add_line('stethoscope-tube',(18,26),(17,34));self.join('shoulders','stethoscope-tube')
        self.path('stethoscope-bell',(17,34),[('A',(19,36),2,2,True),('A',(17,38),2,2,True),('A',(15,36),2,2,True),('A',(17,34),2,2,True)],True);self.join('stethoscope-tube','stethoscope-bell')
        self.path('cat',(28,32),[('L',(28,24)),('L',(34,28)),('L',(36,28)),('L',(42,24)),('L',(42,35)),('C',(42,39),(40,42),(35,42)),('C',(30,42),(28,39),(28,35)),('L',(28,32))],True)
