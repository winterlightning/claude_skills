"""Walking forbidden.
Symbol plan: Circle20 with diagonal prohibition slash, walking torso on head axis(3,-4). Head30,16 radius2, torso24,24: distance10 minus2=8. Outer ring/head also exact8.
Omissions: Outlined silhouette reduced to shared stick-figure vocabulary.
Construction references: human_ref/full_body_ref.png for round-headed limbs; Lucide ban for circular sign and shared slash endpoints.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d3d76995-132c-4fd1-ae17-729e5381f6a4'
SOURCE_PATH='pictographic-primitives/_uncategorized_39/walking forbidden_d3d76995-132c-4fd1-ae17-729e5381f6a4.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='walking-forbidden'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('walking', 'forbidden')

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
        self.add_line('sign-top',(10,6),(38,6))
        self.path('sign',(38,6),[('A',(42,10),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)])
        self.relate('connect','sign','sign-top')
        self.add_polyline('slash',(6,10),(8,12),(24,24),(40,36),(42,38));self.relate('connect','slash','sign')
        self.circle('head',30,16,2)
        self.add_line('torso',(24,24),(21,28));self.relate('connect','torso','slash')
        self.add_polyline('arms',(18,24),(24,24));self.relate('connect','arms','torso');self.relate('connect','arms','slash')
        self.add_polyline('legs',(14,32),(21,28),(21,34));self.relate('connect','legs','torso')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
