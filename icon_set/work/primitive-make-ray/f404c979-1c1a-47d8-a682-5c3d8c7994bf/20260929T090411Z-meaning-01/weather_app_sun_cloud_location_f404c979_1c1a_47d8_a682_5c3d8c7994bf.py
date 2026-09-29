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
    aliases = ()
    keywords = ('weather app sun cloud location',)

    def build(self):
        # Sun rays are three short radial strokes; the disk is partially covered by the cloud.
        self.add_arc('sun',(10,23),(23,12),radius_x=9,large_arc=True)
        self.add_line('ray-top',(14,3),(14,5))
        self.add_line('ray-left',(3,15),(5,15))
        self.add_line('ray-diagonal',(5,6),(7,8))
        curve(self,'cloud',(23,37),((17,37),(8,38),(6,32)),((2,26),(8,20),(14,21)),((16,11),(29,10),(33,20)),((38,20),(42,22),(43,27)))
        # Foreground pin interrupts the cloud; a deliberate occlusion, not spurious contact.
        curve(self,'pin',(35,44),((31,39),(26,34),(26,30)),((26,18),(44,18),(44,30)),((44,34),(39,39),(35,44)),closed=True)
        circle(self,'pin-hole',35,29,3)
