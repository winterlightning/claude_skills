"""Walking forbidden.
Symbol plan: Rounded square prohibition sign with vertical head/upper-torso axis x30; head16 radius2, torso starts26 gives exact8 centerline gap. Bent diagonal slash joins actual limb endpoints. Bounds6..42.
Omissions: Circular border changed to rounded square to enlarge head space; far arm hidden by slash; person uses stick construction.
Construction references: Shared human_ref/full_body_ref.png and user.svg; Lucide ban for a sign and genuine slash junctions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='d3d76995-132c-4fd1-ae17-729e5381f6a4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__walking-forbidden/20260927T140835Z-thuan-mac-1/reference/walking forbidden_d3d76995-132c-4fd1-ae17-729e5381f6a4.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id='walking-forbidden'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
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
        # Circular prohibition ring crossed over a compact walking figure.
        self.circle('sign',24,24,20)
        self.add_polyline('slash',(8,12),(28,28),(40,36))
        self.relate('connect','sign','slash')
        self.circle('head',28,15,2)
        self.add_line('torso-upper',(28,25),(28,28))
        self.add_line('torso-lower',(28,28),(28,31))
        self.add_line('walking-leg',(28,31),(20,34))
        self.relate('connect','slash','torso-upper','torso-lower')
        self.relate('connect','torso-lower','walking-leg')
        self.mark_human_figure('person',head='head',torso='torso-upper',torso_junction='start')
