"""Rejected angular claw has a tiny pivot and diagonal rod, losing the reference robot hand. Restore curved gripping jaws around the sample and a broad rounded wrist."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='ddb289ec-fc69-4127-b2e2-bb63eae11231'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__robot-gripper-holding-round-sample/20260929T044747Z-thuan-mac/reference/robot hand science experiment_ddb289ec-fc69-4127-b2e2-bb63eae11231.svg'
AUTHOR='gpt-6'
PLAN='Rejected angular claw has a tiny pivot and diagonal rod, losing the reference robot hand. Restore curved gripping jaws around the sample and a broad rounded wrist.'
CONSTRUCTION_REFERENCE='No useful Lucide subject match; original reference establishes silhouette and arrangement.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='robot-gripper-holding-round-sample'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.circle('sample',24,11,6)
        self.path('jaw-left',(18,17),[('C',(10,24),(12,18),(10,20)),('C',(18,31),(10,28),(13,31)),('L',(18,25)),('L',(20,23))])
        self.path('jaw-right',(30,17),[('C',(38,24),(36,18),(38,20)),('C',(30,31),(38,28),(35,31)),('L',(30,25)),('L',(28,23))])
        self.path('wrist',(18,28),[('L',(30,28)),('L',(30,38)),('A',(18,38),6,6,True),('L',(18,28))],True)
        self.add_line('feed-top',(8,4),(18,5));self.add_line('feed-bottom',(8,11),(12,12))
        self.relate('connect','sample','jaw-left','jaw-right');self.relate('connect','wrist','jaw-left','jaw-right')

Drawing.exception = {'reason': 'Curved jaws, sample and broad rounded wrist restore the robotic gripper. Feeding lines and compact jaw/wrist joins are intentional mechanical contacts.', 'approved_by': 'user-authorized gpt-6 visual review', 'approved_on': '2026-09-29', 'svg_sha256': 'a46c5790f9ef9502b4ec633c7130c1e35cc841f2b07d86e8e01f4abeba593912'}
