from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f404c979-1c1a-47d8-a682-5c3d8c7994bf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__weather-app-sun-cloud-location/20260929T090411Z-thuan-mac/reference/weather app sun cloud location_f404c979-1c1a-47d8-a682-5c3d8c7994bf.svg'
AUTHOR = "gpt-6"

# Original/current comparison: A cross replaced the sun and the detached cloud and pin no longer overlap as a weather-location composition.
# Revision plan: Restored a round sun behind a cloud with a foreground location pin and clear circular pin opening.
# Construction reference: cloud-sun: overlapping disk/cloud lobes and short rays; original supplies foreground location pin

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
    icon_id = 'weather-app-sun-cloud-location'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Keep the sun/cloud/pin overlap and the circular marker opening at 48px. Compact foreground spacing is needed for the complete weather-location composition.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '6231dfb2bb15585f9d4dd5a4eea19bd3ef0df234ae67dbde53eecbf1dfb27de7'}
    aliases = ()
    keywords = ('weather app sun cloud location',)

    def build(self):

        # Sun disk and cloud share actual endpoints at the occluded disk edge.
        curve(self,'sun',(9,22),((3,16),(7,7),(14,7)),((18,7),(21,10),(22,14)))
        self.add_line('ray-top',(14,2),(14,3))
        self.add_line('ray-left',(2,14),(3,14))
        self.add_line('ray-diagonal',(4,5),(5,6))
        curve(self,'cloud',(22,37),((16,37),(8,38),(6,32)),((2,26),(5,22),(9,22)),((11,22),(12,22),(14,22)),((15,17),(18,14),(22,14)),((28,14),(31,17),(33,21)),((38,20),(41,22),(42,25)))
        self.relate('connect','sun','cloud')
        curve(self,'pin',(35,44),((31,39),(26,34),(26,30)),((26,18),(44,18),(44,30)),((44,34),(39,39),(35,44)),closed=True)
        circle(self,'pin-hole',35,29,3)

