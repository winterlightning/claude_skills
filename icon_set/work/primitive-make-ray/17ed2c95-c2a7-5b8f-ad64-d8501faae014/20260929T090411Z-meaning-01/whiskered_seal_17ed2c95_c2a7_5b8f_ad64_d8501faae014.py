from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '17ed2c95-c2a7-5b8f-ad64-d8501faae014'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__whiskered-seal/20260929T090411Z-thuan-mac/reference/seal_17ed2c95-c2a7-5b8f-ad64-d8501faae014.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The seal became a ghost-like bell with a nose dot; its tail and paired flippers disappeared.
# Revision plan: Restored the smooth seal body, curled side tail, two outward flippers and paired whiskers; omitted facial detail absent from the original.
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
    aliases = ()
    keywords = ('seal',)

    def build(self):
        # One curved animal body; the front flippers and rear tail remain separate readable lobes.
        curve(self,'body',(14,16),((12,3),(34,2),(34,16)),((34,25),(37,34),(43,40)),((44,44),(35,43),(31,39)),((26,44),(18,44),(13,39)),((9,44),(3,44),(5,40)),((11,34),(13,25),(14,16)),closed=True)
        curve(self,'left-flipper',(13,39),((17,36),(18,33),(18,31)))
        curve(self,'right-flipper',(31,39),((27,36),(26,33),(26,31)))
        self.relate('connect','body','left-flipper');self.relate('connect','body','right-flipper')
        self.add_polyline('tail',(7,36),(3,27),(8,28),(10,23),(12,29))
        self.relate('connect','tail','body')
        for name,a,b in [('left-top',(14,18),(7,16)),('left-low',(13,22),(6,24)),('right-top',(34,18),(41,16)),('right-low',(35,22),(42,24))]:
            self.add_line(name,a,b)
            self.relate('connect','body',name)
