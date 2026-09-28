'Standing vulture with rounded head, heavy hooked beak, long tapering wing and two feet.\nPlan: VRECT_L exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: bird: continuous rounded head and pointed folded wing.\nOmissions: Eye and feather lines omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3ca9c99f-67fa-4938-86d8-fb6ec5827812'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__standing-hook-beaked-vulture/20260924T162030Z-thuan-mac/reference/buzzard_3ca9c99f-67fa-4938-86d8-fb6ec5827812.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='standing-hook-beaked-vulture'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('standing', 'hook', 'beaked', 'vulture')
    def build(self):

        def path(name,start,commands,closed=False):
            point=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,point,end)
                elif kind=='A': self.add_arc(member,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,point,(args[0],args[1],end))
                point=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('bird',(8,38),[('C',(18,20),(9,30),(13,24)),('L',(18,14)),('C',(28,4),(18,7),(21,4)),('C',(40,13),(35,4),(40,6)),('L',(40,16)),('L',(32,13)),('C',(32,28),(28,18),(35,22)),('L',(28,32)),('L',(22,38)),('L',(18,38)),('L',(8,38))],True)
        poly('front-leg',(28,32),(31,44),(38,44));join('front-leg','bird')
        poly('rear-leg',(18,38),(14,44));join('rear-leg','bird')
