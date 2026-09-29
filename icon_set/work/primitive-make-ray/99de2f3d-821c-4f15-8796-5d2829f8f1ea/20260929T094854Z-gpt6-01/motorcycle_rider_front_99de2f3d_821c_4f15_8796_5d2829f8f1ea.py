from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '99de2f3d-821c-4f15-8796-5d2829f8f1ea'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__motorcycle-rider-front/20260929T095914Z-thuan-mac/reference/racing_99de2f3d-821c-4f15-8796-5d2829f8f1ea.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The rider became an angular robot-like torso with a rectangular central block instead of a rounded front wheel.
# Revision plan: Restored rounded shoulders, relaxed angled arms, handlebar segments and a narrow capsule-shaped front wheel beneath the rider.
# Construction reference: human_ref/full_body_ref.png: circular head and smooth upper body; supplied original: centered wheel and paired angled arms

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
    icon_id = 'motorcycle-rider-front'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Keep a front-view rider, both handlebars and the narrow front wheel. Compact connected vehicle details preserve meaning at4px stroke; the head gap remains exactly4px.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '4a5786b0069f331b0f1ecfad87ff906e24ce196f681bc64e3234ec8da24a3d86'}
    aliases = ()
    keywords = ('racing',)

    def build(self):
        # Detached head: cy9,r5 -> shoulder top22, exactly8 centerline /4 ink.
        circle(self,'head',24,9,5)
        curve(self,'shoulders',(11,32),((5,30),(11,22),(17,22)),((21,22),(27,22),(31,22)),((37,22),(43,30),(37,32)))
        self.add_line('left-arm',(11,32),(8,43));self.add_line('right-arm',(37,32),(40,43))
        self.relate('connect','shoulders','left-arm');self.relate('connect','shoulders','right-arm')
        rounded(self,'front-wheel',21,30,27,44,3)
        self.add_line('left-handlebar',(11,32),(21,32));self.add_line('right-handlebar',(27,32),(37,32))
        for side in ('left','right'):
            self.relate('connect',side+'-handlebar',side+'-arm')
            self.relate('connect',side+'-handlebar','front-wheel')
