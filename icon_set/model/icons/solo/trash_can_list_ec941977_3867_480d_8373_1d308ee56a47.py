"""Trash can list.
Symbol plan: Shared axis x24; handle and lid join above rounded bin; two identical rows. Centerline extremes (8,4)-(40,44).
Omissions: Third list row and double lid outline removed to give the list air.
Construction references: Lucide trash-2 original and atomic-debug: open handle, simple lid and rounded bin.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ec941977-3867-480d-8373-1d308ee56a47'
SOURCE_PATH='pictographic-primitives/_uncategorized_38/trash can list_ec941977-3867-480d-8373-1d308ee56a47.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='trash-can-list'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('trash', 'can', 'list')

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
        self.add_polyline('lid',(8,12),(16,12),(32,12),(40,12))
        self.path('handle',(16,12),[('L',(16,8)),('A',(20,4),4,4,True),('L',(28,4)),('A',(32,8),4,4,True),('L',(32,12))])
        self.relate('connect','handle','lid')
        self.path('bin',(10,12),[('L',(10,40)),('A',(14,44),4,4,False),('L',(34,44)),('A',(38,40),4,4,False),('L',(38,12))])
        self.relate('connect','bin','lid')
        for j,y in enumerate((24,32)):self.add_line(f'list-{j}',(19,y),(29,y))
