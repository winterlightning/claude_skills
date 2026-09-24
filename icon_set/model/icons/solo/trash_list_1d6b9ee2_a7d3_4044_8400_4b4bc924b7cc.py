"""Trash list.
Symbol plan: Wide bin provides separate bullets and rules at pitch8; axis24 handle. Centerline (4,8)-(44,40).
Omissions: Third row and doubled lid removed.
Construction references: Lucide trash-2: rounded bin with simple handle and single lid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1d6b9ee2-a7d3-4044-8400-4b4bc924b7cc'
SOURCE_PATH='pictographic-primitives/_uncategorized_38/trash list_1d6b9ee2-a7d3-4044-8400-4b4bc924b7cc.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='trash-list'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('trash', 'list')

    def path(self,n,start,ops,closed=False):
        at=start; members=[]
        for i,op in enumerate(ops):
            kind,end,*args=op
            if at==end: continue
            m=f'{n}-{i}'
            if kind=='L': self.add_line(m,at,end)
            elif kind=='A': self.add_arc(m,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            else: self.add_bezier(m,at,(args[0],args[1],end))
            members.append(m);at=end
        if closed and at!=start:
            self.add_line(n+'-close',at,start);members.append(n+'-close')
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def rect(self,n,l,t,r,b,k=4,top=(),right=(),bottom=(),left=()):
        ops=[('L',(x,t)) for x in sorted(top) if l+k<x<r-k]
        ops += [('L',(r-k,t)),('A',(r,t+k),k,k,True)]
        ops += [('L',(r,y)) for y in sorted(right) if t+k<y<b-k]
        ops += [('L',(r,b-k)),('A',(r-k,b),k,k,True)]
        ops += [('L',(x,b)) for x in sorted(bottom,reverse=True) if l+k<x<r-k]
        ops += [('L',(l+k,b)),('A',(l,b-k),k,k,True)]
        ops += [('L',(l,y)) for y in sorted(left,reverse=True) if t+k<y<b-k]
        ops += [('L',(l,t+k)),('A',(l+k,t),k,k,True)]
        self.path(n,(l+k,t),ops,True)

    def build(self):
        # Lid is one stroke; the broad bin owns two list rows at pitch 8.
        self.add_polyline('lid',(4,16),(16,16),(32,16),(44,16))
        self.path('handle',(16,16),[('L',(16,12)),('A',(20,8),4,4,True),('L',(28,8)),('A',(32,12),4,4,True),('L',(32,16))])
        self.relate('connect','handle','lid')
        self.path('bin-left',(4,16),[('L',(4,36)),('A',(8,40),4,4,False)])
        self.add_line('bin-bottom',(8,40),(40,40))
        self.path('bin-right',(40,40),[('A',(44,36),4,4,False),('L',(44,16))])
        self.relate('connect','bin-left','bin-bottom');self.relate('connect','bin-right','bin-bottom')
        self.relate('connect','bin-left','lid');self.relate('connect','bin-right','lid')
        for j,y in enumerate((24,32)):
            self.add_dot(f'bullet-{j}',(13,y));self.add_line(f'list-{j}',(23,y),(35,y))
