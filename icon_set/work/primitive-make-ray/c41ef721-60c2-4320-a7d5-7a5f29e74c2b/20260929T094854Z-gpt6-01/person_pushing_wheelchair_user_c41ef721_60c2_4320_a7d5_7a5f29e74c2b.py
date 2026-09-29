from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c41ef721-60c2-4320-a7d5-7a5f29e74c2b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-pushing-wheelchair-user/20260929T094854Z-thuan-mac/reference/wheelchair helper_c41ef721-60c2-4320-a7d5-7a5f29e74c2b.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The helper and seated user were reduced to disconnected-looking heads, a horizontal bar and cramped angular limbs; the wheel was too small.
# Revision plan: Restored a walking helper, bent pushing arm, larger open wheelchair wheel and a clear seated figure with a forward leg.
# Construction reference: human_ref/full_body_ref.png: coherent limbs and circular heads; accessibility: open wheelchair arc and seated leg

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
    icon_id = 'person-pushing-wheelchair-user'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('wheelchair helper',)

    def build(self):
        # Shared human reference. Left head (10,7),r4 -> torso(10,19); right head(33,11),r4 -> torso(33,23): both gaps exactly4 ink.
        circle(self,'helper-head',10,7,4)
        curve(self,'helper-torso',(10,19),((10,23),(8,26),(8,30)))
        self.add_line('helper-back-leg',(8,30),(4,44))
        self.add_polyline('helper-front-leg',(8,30),(14,35),(17,43))
        self.add_polyline('pushing-arm',(10,19),(17,24),(33,23))
        for part in ('helper-back-leg','helper-front-leg','pushing-arm'):self.relate('connect','helper-torso',part)
        self.relate('connect','helper-back-leg','helper-front-leg')
        circle(self,'user-head',33,11,4)
        self.add_line('user-torso',(33,23),(33,32))
        self.add_polyline('user-leg',(33,32),(40,32),(45,43))
        self.relate('connect','user-torso','user-leg');self.relate('connect','pushing-arm','user-torso')
        curve(self,'wheel',(21,27),((14,31),(15,41),(24,44)),((31,46),(38,42),(38,36)))
        self.mark_human_figure('helper',head='helper-head',torso='helper-torso-curve',torso_junction='start')
        self.mark_human_figure('wheelchair-user',head='user-head',torso='user-torso',torso_junction='start')
