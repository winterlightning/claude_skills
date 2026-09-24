"""User drop zone 1.
Symbol plan: Main circle owns P; two equal right nodes share mirrored link placements. Bounds4,8..44,40.
Omissions: Satellite circles reduced to radius2; P descender shortened for clearance.
Construction references: Lucide network: node and link hierarchy; supplied reference for P and circular arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d40b2438-c966-462c-8e4e-d118211694e3'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/user drop zone 1_d40b2438-c966-462c-8e4e-d118211694e3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='user-drop-zone-1'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('user', 'drop', 'zone', '1')

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
        self.circle('main',20,24,16)
        for side,y,sy in [('upper',10,8),('lower',38,40)]:
            self.circle('node-'+side,42,y,2)
            self.add_line('link-'+side,(20,sy),(40,y))
            self.relate('connect','link-'+side,'main');self.relate('connect','link-'+side,'node-'+side)
        self.add_polyline('p-stem',(15,30),(15,26),(15,18),(21,18))
        self.add_arc('p-bowl',(21,18),(21,26),radius_x=4)
        self.add_line('p-return',(21,26),(15,26))
        self.relate('connect','p-stem','p-bowl');self.relate('connect','p-stem','p-return');self.relate('connect','p-bowl','p-return')
