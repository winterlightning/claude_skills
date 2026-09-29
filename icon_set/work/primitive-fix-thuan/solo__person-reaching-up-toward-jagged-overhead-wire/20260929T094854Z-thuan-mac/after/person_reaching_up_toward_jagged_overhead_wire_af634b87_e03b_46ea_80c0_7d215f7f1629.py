from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'af634b87-e03b-46ea-80c0-7d215f7f1629'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-reaching-up-toward-jagged-overhead-wire/20260929T094854Z-thuan-mac/reference/safety danger electricity_af634b87-e03b-46ea-80c0-7d215f7f1629.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The overhead danger was reduced to a hanging zigzag and the figure lost its raised forearm and reaching gesture.
# Revision plan: Restored the stepped overhead wire, angular electrical discharge and a person raising a bent arm toward it.
# Construction reference: human_ref/full_body_ref.png: circular head and bent arm; original supplies the wire and discharge

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
    icon_id = 'person-reaching-up-toward-jagged-overhead-wire'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'The overhead wire and electrical discharge must remain above the raised hand. Preserve compact scene spacing and the exact4px human head gap.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '529068455f90c277568baa2fc7a567613193fc1e1d23f2020f90d06ae8ddfec8'}
    aliases = ()
    keywords = ('safety danger electricity',)

    def build(self):
        self.add_polyline('wire',(4,4),(32,4),(32,10),(44,10))
        self.add_polyline('discharge',(32,4),(24,11),(29,13),(26,18),(34,15))
        self.relate('connect','wire','discharge')
        # Head(16,22),r4; torso starts(16,34): 34-(22+4)=8 centerline,4 ink.
        circle(self,'head',16,22,4)
        self.add_line('torso',(16,34),(16,44))
        curve(self,'raised-arm',(16,34),((25,34),(33,35),(33,28)),((33,26),(33,24),(33,22)))
        self.add_line('lower-arm',(16,34),(6,43))
        self.relate('connect','torso','raised-arm');self.relate('connect','torso','lower-arm');self.relate('connect','raised-arm','lower-arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
