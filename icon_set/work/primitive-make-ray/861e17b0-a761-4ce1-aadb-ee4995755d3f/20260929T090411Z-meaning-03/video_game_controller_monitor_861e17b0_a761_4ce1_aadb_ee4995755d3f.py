from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '861e17b0-a761-4ce1-aadb-ee4995755d3f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__video-game-controller-monitor/20260929T090411Z-thuan-mac/reference/video game controller monitor_861e17b0-a761-4ce1-aadb-ee4995755d3f.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The monitor is blank and the controller has no controls or cable, losing the gaming scene.
# Revision plan: Restored the on-screen game character, monitor stand, connecting cable and a clear angled gamepad silhouette with one action button.
# Construction reference: monitor: rounded display and centered stand; gamepad-2: controls and grip silhouette

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
    icon_id = 'video-game-controller-monitor'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Gaming on a monitor needs both the on-screen character and gamepad controls. Compact foreground overlap, small letter-like counter and cable are retained with 4px strokes.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '4b098cbbc9a728e5a6a9bd14dcf6b383faf5e6937a91f28dea2e604a883fd2d3'}
    aliases = ()
    keywords = ('video game controller monitor',)

    def build(self):

        rounded(self,'monitor',4,4,34,25,3)
        self.add_line('stand',(15,25),(15,32));self.add_line('foot',(8,32),(21,32));self.relate('connect','monitor','stand');self.relate('connect','stand','foot')
        # The reference game character is kept; at this scale the pad retains one action button.
        self.add_arc('pac-arc',(22,10),(22,20),radius_x=6,large_arc=True,sweep=False)
        self.add_line('pac-mouth-1',(22,20),(17,15));self.add_line('pac-mouth-2',(17,15),(22,10));self.add_contour('pacman','pac-arc','pac-mouth-1','pac-mouth-2',closed=True)
        curve(self,'cable',(34,16),((44,16),(44,24),(37,30)));self.relate('connect','monitor','cable')
        curve(self,'controller',(21,34),((25,31),(32,30),(37,30)),((44,30),(47,38),(42,42)),((38,46),(34,40),(31,41)),((26,42),(24,46),(20,44)),((14,41),(16,36),(21,34)),closed=True)
        self.relate('connect','cable','controller')
        self.add_dot('button',(36,35))

