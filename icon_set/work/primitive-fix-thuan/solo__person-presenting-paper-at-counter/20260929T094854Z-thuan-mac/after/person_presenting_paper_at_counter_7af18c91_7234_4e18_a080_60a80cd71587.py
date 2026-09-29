from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7af18c91-7234-4e18-a080-60a80cd71587'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-presenting-paper-at-counter/20260929T094854Z-thuan-mac/reference/information desk paper_7af18c91-7234-4e18-a080-60a80cd71587.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The second person was omitted; the scene became one person holding a small square beside an unrelated box.
# Revision plan: Restored the two people facing each other, an angled document held up by the visitor, and the attendant reaching across a tapered counter.
# Construction reference: human_ref/full_body_ref.png: outlined circular heads and round-ended limbs; original supplies the facing people and paper exchange

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
    icon_id = 'person-presenting-paper-at-counter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Two full figures, an angled document and a counter require compact spacing at 48px; retain their roles and exact 4px detached head gaps with 4px strokes.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'fc49a25453b1528a12070fd59548c18819a06a730c6de6c9d6a0c908a8d1b0b5'}
    aliases = ()
    keywords = ('information desk paper',)

    def build(self):
        # Human construction: both heads r4 at y8; actual upper torso junction y20 gives 20-(8+4)=8 centerline /4 ink.
        for who,cx in (('visitor',7),('attendant',41)):
            circle(self,who+'-head',cx,8,4)
            self.add_line(who+'-torso',(cx,20),(cx,44))
            self.mark_human_figure(who,head=who+'-head',torso=who+'-torso',torso_junction='start')
        self.add_polyline('paper',(21,4),(30,6),(27,20),(18,18),closed=True)
        curve(self,'visitor-arm',(7,20),((11,20),(13,26),(17,23)),((19,22),(20,20),(18,18)))
        self.relate('connect','visitor-arm','visitor-torso');self.relate('connect','visitor-arm','paper')
        self.add_polyline('counter',(26,30),(37,30),(35,44),(28,44),closed=True)
        self.add_polyline('attendant-arm',(41,20),(34,30),(30,30))
        self.relate('connect','attendant-arm','attendant-torso');self.relate('connect','attendant-arm','counter')
