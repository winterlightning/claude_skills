from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '675d2e83-bae0-46ca-b68a-04732a2c88a9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__monitor-shuttlecock/20260929T094854Z-thuan-mac/reference/monitor shuttlecock_675d2e83-bae0-46ca-b68a-04732a2c88a9.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The shuttlecock became a solid three-pronged blob and the monitor stand was too short.
# Revision plan: Lengthened the stand and rebuilt the shuttlecock with a distinct circular cork and outlined feather fan.
# Construction reference: monitor: rounded frame with centered long pedestal; original supplies cork and fanned feather silhouette

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
    icon_id = 'monitor-shuttlecock'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Preserve the feather fan and its separate cork within the monitor. Compact feather spacing is retained at4px stroke; the11-unit stand directly addresses the reviewer.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'c442835d0021ec80e0984ceb1397e71b96a792a0ea95070f8be2e94ead6dac8a'}
    aliases = ()
    keywords = ('monitor shuttlecock',)

    def build(self):
        # Frame4,4–44,33; a true11-unit stand reaches y44 and keeps the screen distinct from its base.
        rounded(self,'monitor',4,4,44,33,4)
        self.add_line('stand',(24,33),(24,44));self.add_line('base',(15,44),(33,44))
        self.relate('connect','monitor','stand');self.relate('connect','stand','base')

        circle(self,'cork',15,25,3)
        curve(self,'feather-outline',(15,22),((16,18),(17,13),(18,10)),((19,7),(23,9),(22,13)),((25,8),(30,11),(27,16)),((32,11),(36,16),(32,19)),((28,21),(22,24),(18,25)))
        self.relate('connect','cork','feather-outline')
        self.add_line('feather-rib',(27,16),(18,25));self.relate('connect','feather-rib','feather-outline');self.relate('connect','feather-rib','cork')
