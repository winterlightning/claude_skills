from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4756649f-fa81-4c81-bfa9-f4206356d978'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__underwater-drone-twin-thrusters/20260929T090411Z-thuan-mac/reference/underwater drone_4756649f-fa81-4c81-bfa9-f4206356d978.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The drone became an empty capsule with feet, no visible propellers, and angular water.
# Revision plan: Restored curved water waves, paired propeller shafts, a broad central body and an underslung equipment pod.
# Construction reference: gamepad-2: smoothly joined lateral lobes; original supplies the drone-specific body and propulsion

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
    icon_id = 'underwater-drone-twin-thrusters'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Water, propellers and underside pod are all essential to the underwater drone. Preserve their compact 48px arrangement and true contacts with 4px strokes.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '7308c64870ae6b3be5e11ef413596758c36cfa4fb828b2ad6ce904e26c29e215'}
    aliases = ()
    keywords = ('underwater drone',)

    def build(self):

        # Two shallow water waves; propeller crossbars and shafts remain visible.
        for j,x in enumerate((4,24)):
            curve(self,f'wave-{j}',(x,5),((x+6,11),(x+14,11),(x+20,5)))
        for x in (10,38):
            self.add_line(f'propeller-{x}',(x-5,16),(x+5,16))
            self.add_line(f'shaft-{x}',(x,16),(x,24))
            self.relate('connect',f'propeller-{x}',f'shaft-{x}')
        curve(self,'body',(4,25),((6,25),(8,24),(10,24)),((15,24),(17,21),(24,21)),((31,21),(33,24),(38,24)),((40,24),(42,25),(44,25)),((46,25),(46,31),(44,31)),((38,31),(32,35),(24,35)),((16,35),(10,31),(4,31)),((2,31),(2,25),(4,25)),closed=True)
        for x in (10,38):self.relate('connect','body',f'shaft-{x}')
        curve(self,'pod',(4,31),((11,31),(14,36),(14,39)),((14,44),(34,44),(34,39)),((34,36),(37,31),(44,31)))
        self.relate('connect','body','pod')

