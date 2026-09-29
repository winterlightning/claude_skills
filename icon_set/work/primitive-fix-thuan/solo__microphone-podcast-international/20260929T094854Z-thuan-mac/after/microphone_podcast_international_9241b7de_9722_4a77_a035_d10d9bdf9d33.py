from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9241b7de-9722-4a77-a035-d10d9bdf9d33'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__microphone-podcast-international/20260929T094854Z-thuan-mac/reference/microphone podcast international_9241b7de-9722-4a77-a035-d10d9bdf9d33.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The globe lost its meridians and became a headset-like arch; the microphone lost its stand.
# Revision plan: Restored globe latitude/longitude lines over a capsule microphone, curved cradle and pedestal.
# Construction reference: globe: meridians and latitude; mic: capsule, supporting cradle and stand

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
    icon_id = 'microphone-podcast-international'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'The globe grid and microphone pedestal are essential to international podcast meaning. Preserve compact globe-grid and capsule/cradle spacing at4px stroke.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'f3b7ee9667ec5cb5f0ee1d733b9778e9b853d86b3b823e18dc4db325c3cd77da'}
    aliases = ()
    keywords = ('microphone podcast international',)

    def build(self):
        # Hemisphere is open below, as in the reference, and centered over the microphone.
        curve(self,'globe',(6,20),((6,17),(7,14),(9,12)),((12,7),(17,4),(24,4)),((31,4),(36,7),(39,12)),((41,14),(42,17),(42,20)))
        self.add_line('latitude',(9,12),(39,12));self.relate('connect','globe','latitude')
        for side in (-1,1):
            curve(self,'meridian-'+str(side),(24,4),((24+side*6,4),(24+side*8,11),(24+side*8,20)))
            self.relate('connect','globe','meridian-'+str(side));self.relate('connect','latitude','meridian-'+str(side))
        self.relate('connect','meridian--1','meridian-1')
        rounded(self,'microphone',19,20,29,34,5)
        curve(self,'cradle',(10,27),((10,29),(10,30),(10,31)),((10,36),(17,39),(24,39)),((31,39),(38,36),(38,31)),((38,30),(38,29),(38,27)))
        self.add_line('stand',(24,39),(24,44));self.add_line('base',(16,44),(32,44))
        self.relate('connect','cradle','stand');self.relate('connect','stand','base')
