from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7531c3ff-b529-46cd-ad18-210cb444c4fb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__warrior-pose-raised-arms/20260929T090411Z-thuan-mac/reference/yoga warrior pose_7531c3ff-b529-46cd-ad18-210cb444c4fb.svg'
AUTHOR = "gpt-6"

# Original/current comparison: A tiny head, disconnected-looking diagonal trunk and squat stance obscure the upright raised-arm warrior pose.
# Revision plan: Restored the upright raised arm, proportionate head, curved torso and a long rear leg with bent forward knee.
# Construction reference: human_ref/full_body_ref.png: head proportion, round-ended limbs; supplied original: raised arm and lunge

def circle(icon, name, cx, cy, r):
    icon.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
    icon.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
    icon.add_contour(name,name+'-top',name+'-bottom',closed=True)

def rounded(icon,name,x0,y0,x1,y1,r):
    points=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
    ids=[]
    for j,a in enumerate(points):
        b=points[(j+1)%8];n=f'{name}-{j}';ids.append(n)
        if j%2: icon.add_arc(n,a,b,radius_x=r)
        else: icon.add_line(n,a,b)
    icon.add_contour(name,*ids,closed=True)

def curve(icon,name,start,*segments,closed=False):
    icon.add_bezier(name+'-curve',start,*segments)
    icon.add_contour(name,name+'-curve',closed=closed)

class Drawing(Solo48):
    icon_id = 'warrior-pose-raised-arms'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('yoga warrior pose',)

    def build(self):
        # Human reference: full_body_ref.png. (23,22)-(18,10)=(5,12); distance13 minus r5=8 centerline gap.
        circle(self,'head',18,10,5)
        curve(self,'torso',(23,22),((25,27),(24,29),(24,31)))
        self.add_polyline('raised-arm',(23,22),(32,22),(32,4))
        self.add_line('rear-leg',(24,31),(10,44))
        self.add_polyline('front-leg',(24,31),(36,34),(38,44))
        self.relate('connect','torso','raised-arm','rear-leg','front-leg')
        self.mark_human_figure('person',head='head',torso='torso-curve',torso_junction='start')
