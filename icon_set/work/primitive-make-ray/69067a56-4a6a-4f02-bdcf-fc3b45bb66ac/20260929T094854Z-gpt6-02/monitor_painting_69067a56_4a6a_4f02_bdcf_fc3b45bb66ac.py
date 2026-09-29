from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '69067a56-4a6a-4f02-bdcf-fc3b45bb66ac'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__monitor-painting/20260929T094854Z-thuan-mac/reference/monitor painting_69067a56-4a6a-4f02-bdcf-fc3b45bb66ac.svg'
AUTHOR = "gpt-6"

# Original/current comparison: A plain oval and diagonal stroke replaced the artist palette and brush, and the stand was too short.
# Revision plan: Restored a kidney-shaped palette, paint mark and pointed brush head; lengthened the monitor stand.
# Construction reference: palette: kidney contour and thumb recess; monitor: rounded display and centered pedestal

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
    icon_id = 'monitor-painting'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'The palette and pointed brush must both remain recognizable inside the screen. Preserve compact inner marks and the longer11-unit monitor stand at4px stroke.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '55904d512a2e2585138dbbc6a6201118a9d6c45dfb06c2e557bc37041a5b15cf'}
    aliases = ()
    keywords = ('monitor painting',)

    def build(self):
        # Frame4,4–44,33; a true11-unit stand reaches y44 and keeps the screen distinct from its base.
        rounded(self,'monitor',4,4,44,33,4)
        self.add_line('stand',(24,33),(24,44));self.add_line('base',(15,44),(33,44))
        self.relate('connect','monitor','stand');self.relate('connect','stand','base')

        curve(self,'palette',(23,11),((14,7),(8,14),(10,22)),((12,29),(24,30),(24,24)),((21,24),(21,19),(26,18)),((28,14),(27,12),(23,11)),closed=True)
        self.add_dot('paint',(16,17))
        curve(self,'brush-head',(35,10),((34,14),(30,16),(32,19)),((32,20),(33,21),(34,21)),((39,21),(39,17),(35,10)),closed=True)
        self.add_line('brush-handle',(34,21),(29,28))
        self.relate('connect','brush-head','brush-handle')
