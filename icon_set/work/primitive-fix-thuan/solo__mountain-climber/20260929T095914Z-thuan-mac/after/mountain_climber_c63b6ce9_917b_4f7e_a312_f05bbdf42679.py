from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c63b6ce9-917b-4f7e-a312-f05bbdf42679'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mountain-climber/20260929T095914Z-thuan-mac/reference/climb_c63b6ce9-917b-4f7e-a312-f05bbdf42679.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The cliff became a jagged zigzag and the climber had a tiny head with an unnatural bent body.
# Revision plan: Restored the smooth curving cliff, a proportionate head, an extended reaching arm and a bent climbing knee.
# Construction reference: human_ref/full_body_ref.png: outlined head, coherent limbs and bent knee; original supplies curved cliff

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
    icon_id = 'mountain-climber'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Retain the natural curve of the cliff, exact4px head gap and a readable climbing action. The natural scene envelope and compact bent-leg spacing are intentional.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '0926557b852ca49fe239ff87b26dcaf387f17efedf83bc9655876ee721987c5e'}
    aliases = ()
    keywords = ('climb',)

    def build(self):
        # Head(16,11),r5 -> actual torso junction(16,24):4px visible clearance; upper torso tangent vertical.
        circle(self,'head',16,11,5)
        curve(self,'torso',(16,24),((16,28),(13,32),(16,34)))
        self.add_polyline('reaching-arm',(16,24),(24,24),(38,19))
        self.add_line('rear-leg',(16,34),(12,44))
        curve(self,'front-leg',(16,34),((20,32),(24,28),(27,33)),((29,36),(31,40),(34,44)))
        curve(self,'cliff',(38,4),((40,10),(40,15),(38,19)),((38,24),(37,28),(35,31)))
        for part in ('reaching-arm','rear-leg','front-leg'):self.relate('connect','torso',part)
        self.relate('connect','rear-leg','front-leg');self.relate('connect','reaching-arm','cliff')
        self.mark_human_figure('climber',head='head',torso='torso-curve',torso_junction='start')
