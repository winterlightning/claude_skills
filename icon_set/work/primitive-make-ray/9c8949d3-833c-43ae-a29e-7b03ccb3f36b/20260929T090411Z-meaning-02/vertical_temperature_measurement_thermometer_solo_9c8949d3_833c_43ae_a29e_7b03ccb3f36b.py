from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9c8949d3-833c-43ae-a29e-7b03ccb3f36b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vertical-temperature-measurement-thermometer-solo/20260929T090411Z-thuan-mac/reference/thermometer_9c8949d3-833c-43ae-a29e-7b03ccb3f36b.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The thermometer has an oversized blunt column and the scale became dots.
# Revision plan: Restored a slender tube, round bulb, fluid stem and horizontal measurement ticks.
# Construction reference: thermometer: narrow stem and rounded bulb

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
    if closed: icon.add_contour(name,name+'-curve',closed=True)

class Drawing(Solo48):
    icon_id = 'vertical-temperature-measurement-thermometer-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('thermometer',)

    def build(self):
        self.add_arc('cap',(10,12),(26,12),radius_x=8)
        self.add_line('tube-right',(26,12),(26,28))
        self.add_arc('bulb',(26,28),(10,28),radius_x=10,large_arc=True)
        self.add_line('tube-left',(10,28),(10,12))
        self.add_contour('thermometer','cap','tube-right','bulb','tube-left',closed=True)
        self.add_line('mercury',(18,19),(18,35))
        self.add_line('scale-top',(35,11),(40,11))
        self.add_line('scale-middle',(35,21),(38,21))
