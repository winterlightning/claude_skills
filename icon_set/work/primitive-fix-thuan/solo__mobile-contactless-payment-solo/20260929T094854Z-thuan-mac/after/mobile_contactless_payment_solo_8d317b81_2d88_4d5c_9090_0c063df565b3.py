from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8d317b81-2d88-4d5c-9090-0c063df565b3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mobile-contactless-payment-solo/20260929T094854Z-thuan-mac/reference/mobile phone dollar sign wireless_8d317b81-2d88-4d5c-9090-0c063df565b3.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The phone lost its top edge and the dollar sign became a zigzag, obscuring contactless payment.
# Revision plan: Restored a complete rounded phone, a smooth dollar sign and two centered wireless arcs.
# Construction reference: smartphone: closed portrait enclosure; original supplies two wireless arcs and a dollar mark

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
    icon_id = 'mobile-contactless-payment-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'A complete phone plus legible dollar sign and wireless arcs needs compact detail spacing. Preserve4px strokes and the currency curves rather than replacing the dollar with a zigzag.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '9316aa33e896b4e7d8c5223432b77ef805c9b970c90145baa6b7944f632d95ce'}
    aliases = ()
    keywords = ('mobile phone dollar sign wireless',)

    def build(self):
        curve(self,'wifi-outer',(7,7),((17,1),(31,1),(41,7)))
        curve(self,'wifi-inner',(15,12),((20,7),(28,7),(33,12)))
        rounded(self,'phone',13,18,35,45,4)
        curve(self,'dollar',(28,25),((26,22),(20,22),(20,27)),((20,30),(28,29),(28,33)),((28,37),(22,38),(20,35)))
        self.add_line('currency-stem',(24,23),(24,39));self.relate('connect','dollar','currency-stem')
