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
        self.circle('sample',24,12,6)
        self.path('jaw-left',(19,14),[('C',(9,24),(12,14),(8,18)),('C',(18,32),(9,28),(14,32)),('L',(18,26)),('C',(19,20),(13,24),(14,21))])
        self.path('jaw-right',(29,14),[('C',(39,24),(36,14),(40,18)),('C',(30,32),(39,28),(34,32)),('L',(30,26)),('C',(29,20),(35,24),(34,21))])
        self.path('wrist',(18,28),[('L',(30,28)),('L',(30,38)),('A',(18,38),6,6,True),('L',(18,28))],True)
        self.add_line('feed-top',(8,4),(20,6));self.add_line('feed-bottom',(8,11),(13,12))
        self.relate('connect','sample','jaw-left','jaw-right');self.relate('connect','wrist','jaw-left','jaw-right')
