"""A sailboat on waves is surrounded by two transfer arrows.
Plan: Triangular sail, curved hull and wave form the boat; opposed curved arrows stay separate.
Keyshape SQUARE: exact ink and centerline envelopes ((4, 4, 44, 44), (6, 6, 42, 42)).
References: Supplied SVG, rendered and visually inspected. No useful local Lucide subject match used; shared geometric construction principles applied.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '79b63fb3-53d2-42aa-af62-afdbc09d4964'
SOURCE_PATH = 'icon_set/work/todo-references/transportation ticket boat transfer_79b63fb3-53d2-42aa-af62-afdbc09d4964.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'transportation-ticket-boat-transfer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('transportation', 'ticket', 'boat', 'transfer')

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

        self.add_polyline('sail',(18,6),(6,24),(18,24),(18,30));self.add_line('mast',(18,6),(18,24));self.join('sail','mast')
        self.path('hull',(6,30),[('L',(18,30)),('L',(30,30)),('C',(26,38),(22,36),(18,36)),('C',(14,38),(10,36),(6,30))],True);self.join('sail','hull')
        self.add_bezier('wave',(18,36),((24,40),(28,34),(34,36)),((38,38),(40,34),(42,36)));self.join('hull','wave')
        self.add_bezier('transfer-top',(32,12),((38,14),(40,18),(40,22)))
        self.add_polyline('arrow-top',(36,18),(40,22),(42,18));self.join('transfer-top','arrow-top')
        self.add_bezier('transfer-bottom',(8,34),((10,39),(16,40),(20,40)))
        self.add_polyline('arrow-bottom',(16,36),(20,40),(16,42));self.join('transfer-bottom','arrow-bottom')
