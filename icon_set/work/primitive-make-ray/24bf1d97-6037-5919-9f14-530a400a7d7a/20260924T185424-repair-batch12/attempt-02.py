"""A 0x coin contains an outlined X and a rising diagonal segment.
Plan: Coin ring encloses the complete outlined X; exposed diagonal pieces remain at opposite corners.
Keyshape CIRCLE: {'center': [24, 24], 'ink_radius': 22, 'centerline_radius': 20}.
References: Supplied SVG rendered and inspected. No useful local Lucide subject match used; geometric reconstruction follows the supplied drawing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '24bf1d97-6037-5919-9f14-530a400a7d7a'
SOURCE_PATH = 'pictographic-primitives/finance/virtual coin crypto 0x zrx_24bf1d97-6037-5919-9f14-530a400a7d7a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'virtual-coin-crypto-0x-zrx'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', '0x', 'zrx')

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
        # Coin circle split at exact 3-4-5 radial nodes for the two exposed slash ends.
        ring=[(24,4),(36,8),(44,24),(24,44),(12,40),(4,24),(24,4)]
        for j,(a,b) in enumerate(zip(ring,ring[1:])):
            self.add_arc('coin-'+str(j),a,b,radius_x=20)
        self.add_contour('coin',*('coin-'+str(j) for j in range(6)),closed=True)
        self.add_polyline('x-outline',(21,13),(24,16),(27,13),(30,16),(35,21),(32,24),(35,27),(27,35),(24,32),(21,35),(18,32),(13,27),(16,24),(13,21),closed=True)
        self.add_line('slash-low',(12,40),(18,32))
        self.add_line('slash-high',(30,16),(36,8))
        for n in ['slash-low','slash-high']:
            self.relate('connect',n,'coin');self.relate('connect',n,'x-outline')
