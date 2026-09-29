from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '827a6183-d0a3-4c08-a449-f0bddf6114b0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mountain-pose/20260929T095914Z-thuan-mac/reference/yoga mountain pose_827a6183-d0a3-4c08-a449-f0bddf6114b0.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The mountain pose had rigid bent arms and an artificial waist bar instead of relaxed arms and close-set legs.
# Revision plan: Restored a neutral upright torso, gently hanging arms and close-set feet in a calm standing pose.
# Construction reference: human_ref/full_body_ref.png: round head and coherent limbs; original: narrow neutral standing posture

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
    icon_id = 'mountain-pose'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Mountain pose should remain narrow and relaxed with close-set feet; preserve this natural envelope rather than spreading the arms to fill the keyshape.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '037d21d1c040d85a09e602b57bd42537667958af001a56c8af37976f022942a0'}
    aliases = ()
    keywords = ('yoga mountain pose',)

    def build(self):
        # Human reference proportions; head bottom14, upper torso22 ->4px ink gap.
        circle(self,'head',24,9,5)
        self.add_line('torso',(24,22),(24,32))
        curve(self,'left-arm',(24,22),((18,22),(17,29),(17,35)))
        curve(self,'right-arm',(24,22),((30,22),(31,29),(31,35)))
        self.add_line('left-leg',(24,32),(21,44));self.add_line('right-leg',(24,32),(27,44))
        for part in ('left-arm','right-arm','left-leg','right-leg'):self.relate('connect','torso',part)
        self.relate('connect','left-arm','right-arm');self.relate('connect','left-leg','right-leg')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
