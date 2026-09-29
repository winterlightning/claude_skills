from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fb5ed3c8-9522-4523-9735-214910411c7e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__video-game-controller-team/20260929T090411Z-thuan-mac/reference/video game controller team_fb5ed3c8-9522-4523-9735-214910411c7e.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The team heads were tiny ring marks and the controller lacked any controls.
# Revision plan: Restored a recognizable controller with D-pad and action buttons below three clear player busts.
# Construction reference: human_ref/user.svg: circular heads and rounded shoulders; gamepad-2: grips, D-pad and action buttons

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
    icon_id = 'video-game-controller-team'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    human_construction = "bust"
    exception = {'reason': 'Three teammates and a populated controller need compact spacing. Preserve the three-head count and control marks at 48px, with circular heads and rounded shoulders.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '33b2ff334bbd16561004941a350ceec29b1902ed8d11992b0d61d638e6b67800'}
    aliases = ()
    keywords = ('video game controller team',)

    def build(self):
        # Repeated players share head radius and shoulder geometry.
        for j,cx in enumerate((10,24,38)):
            circle(self,f'head-{j}',cx,7,4)
            self.add_arc(f'shoulders-{j}',(cx-6,21),(cx+6,21),radius_x=6)
            self.relate('connect',f'head-{j}',f'shoulders-{j}')

        curve(self,'controller',(12,26),((7,26),(6,28),(5,34)),((4,39),(4,43),(8,43)),((11,43),(14,40),(17,40)),((21,40),(27,40),(31,40)),((34,40),(37,43),(40,43)),((44,43),(44,39),(43,34)),((42,28),(41,26),(36,26)),((30,26),(18,26),(12,26)),closed=True)
        self.add_line('dpad-h',(11,34),(17,34));self.add_line('dpad-v',(14,31),(14,37));self.relate('connect','dpad-h','dpad-v')
        self.add_dot('button-left',(31,32));self.add_dot('button-right',(37,32))
