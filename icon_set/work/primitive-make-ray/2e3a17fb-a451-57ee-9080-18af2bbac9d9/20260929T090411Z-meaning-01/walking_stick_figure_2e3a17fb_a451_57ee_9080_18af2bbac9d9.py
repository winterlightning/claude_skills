from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2e3a17fb-a451-57ee-9080-18af2bbac9d9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__walking-stick-figure/20260929T090411Z-thuan-mac/reference/walking_2e3a17fb-a451-57ee-9080-18af2bbac9d9.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The rejected figure has a tiny head and an exaggerated wide stride; its straight angular arms read as running.
# Revision plan: Restored a proportionate circular head, gently leaning torso, relaxed opposite arm swing and natural walking step.
# Construction reference: human_ref/full_body_ref.png: circular outlined head and coherent round-ended torso/limbs

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
    icon_id = 'walking-stick-figure'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'A relaxed walking pose has a narrower natural envelope than the prescribed rectangle. Preserve 4px human strokes and the exact 4px detached head gap.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '5451f174a4077c84f6edd012a2dc4f8f8e425b38702be88a8c2c6afa57cfa92e'}
    aliases = ()
    keywords = ('walking',)

    def build(self):
        # Human reference: full_body_ref.png. Head r5; junction (27,22): 22-(9+5)=8 centerline, 4 ink.
        circle(self,'head',27,9,5)
        curve(self,'torso',(27,22),((27,27),(23,29),(23,32)))
        self.add_polyline('back-arm',(27,22),(20,25),(15,33))
        self.add_polyline('front-arm',(27,22),(32,28),(37,31))
        self.add_line('rear-leg',(23,32),(13,44))
        self.add_polyline('front-leg',(23,32),(31,43),(35,43))
        for part in ('back-arm','front-arm','rear-leg','front-leg'):self.relate('connect','torso',part)
        self.relate('connect','back-arm','front-arm');self.relate('connect','rear-leg','front-leg')
        self.mark_human_figure('person',head='head',torso='torso-curve',torso_junction='start')
