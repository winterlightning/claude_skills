"""User cash scale.
Symbol plan: Left standing figure balances currency on a beam; shared head/torso x12, exact gap20-(9+3)=8; open triangular support. Bounds6,6..42,42.
Omissions: Coin ring, lower dollar tick and fulcrum baseline removed; outline person reduced to shared stick vocabulary.
Construction references: human_ref/full_body_ref.png and user.svg: circular head, aligned torso; Lucide scale: beam and triangular support.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='fca396e7-351b-4b96-8ac4-233b3625135c'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/user cash scale_fca396e7-351b-4b96-8ac4-233b3625135c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='user-cash-scale'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('user', 'cash', 'scale')

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
        self.circle('head',12,9,3)
        self.add_line('torso',(12,20),(12,26))
        self.add_polyline('arms',(6,22),(12,20),(18,22));self.relate('connect','arms','torso')
        self.add_polyline('legs',(6,34),(12,26),(18,34));self.relate('connect','legs','torso')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.add_polyline('cash',(42,10),(37,10),(32,10),(32,18),(42,18),(42,26),(32,26))
        self.add_line('dollar-tick',(37,6),(37,10));self.relate('connect','dollar-tick','cash')
        self.add_polyline('beam',(6,34),(18,34),(24,34),(42,34));self.relate('connect','legs','beam')
        self.add_polyline('fulcrum',(18,42),(24,34),(30,42));self.relate('connect','fulcrum','beam')
