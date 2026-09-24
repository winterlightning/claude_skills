"""workflow data table increasing arrow. Plan: Rising zigzag above data grid. Two rows replace four and table top is level; shared row spacing8 and column widths10/9/9 preserve legibility.
Keyshape SQUARE; shared parameters own repeated elements and genuine junctions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bd44c072-c5cf-4191-b2b0-3681a58f3a3a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_40/workflow data table increasing arrow_bd44c072-c5cf-4191-b2b0-3681a58f3a3a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'workflow-data-table-increasing-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('workflow', 'data', 'table', 'increasing', 'arrow')
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
        self.add_polyline('growth',(6,24),(14,14),(22,18),(30,10),(34,14),(42,6))
        self.add_polyline('arrow-head',(34,6),(42,6),(42,14));self.join('growth','arrow-head')
        self.add_polyline('table',(14,26),(24,26),(33,26),(42,26),(42,34),(42,42),(33,42),(24,42),(14,42),(14,34),closed=True)
        for x in (24,33):
            self.add_polyline(f'column-{x}',(x,26),(x,34),(x,42));self.join('table',f'column-{x}')
        self.add_polyline('row',(14,34),(24,34),(33,34),(42,34));self.join('table','row');self.join('column-24','row');self.join('column-33','row')
