from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '17ed2c95-c2a7-5b8f-ad64-d8501faae014'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__whiskered-seal/20260929T090411Z-thuan-mac/reference/seal_17ed2c95-c2a7-5b8f-ad64-d8501faae014.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The seal became a ghost-like bell with a nose dot; its tail and paired flippers disappeared.
# Revision plan: Restored a smooth seal body, two outward flippers and paired whiskers, and added a minimal face to make the animal clear at UI size.
# Construction reference: No useful Lucide seal match; use coherent smooth contours and the supplied reference silhouette.

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
    icon_id = 'whiskered-seal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Preserve the seal silhouette, whiskers, paired flippers and simple face at 48px. Compact contour/whisker spacing is intentional; the small side tail is omitted to avoid clutter.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '6fdcf40b55ee1c97b4f6b52dd0dade27a94c244354838f7d4c744b2e5cc1a9ef'}
    aliases = ()
    keywords = ('seal',)

    def build(self):

        curve(self,'body',(14,16),((14,2),(34,2),(34,16)),((34,18),(35,21),(35,23)),((36,31),(39,36),(43,40)),((44,44),(35,43),(31,39)),((26,44),(18,44),(13,39)),((9,44),(3,44),(5,40)),((6,38),(8,36),(9,34)),((12,29),(13,25),(13,23)),((13,21),(14,18),(14,16)),closed=True)
        curve(self,'left-flipper',(13,39),((17,36),(18,33),(18,31)))
        curve(self,'right-flipper',(31,39),((27,36),(26,33),(26,31)))
        self.relate('connect','body','left-flipper');self.relate('connect','body','right-flipper')
        for name,a,b in [('left-top',(14,16),(7,14)),('left-low',(13,23),(6,25)),('right-top',(34,16),(41,14)),('right-low',(35,23),(42,25))]:
            self.add_line(name,a,b)
            self.relate('connect','body',name)

        self.add_dot('eye-left',(20,16));self.add_dot('eye-right',(28,16));self.add_dot('nose',(24,23))

