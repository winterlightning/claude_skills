from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '96c9812c-13cb-4856-884d-c1360a6bd316'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__martini-glass-with-skewered-olive/20260929T095914Z-thuan-mac/reference/appetizer_96c9812c-13cb-4856-884d-c1360a6bd316.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The skewered olive became a short bent stroke and the garnish lost its round fruit shape.
# Revision plan: Restored a distinct outlined olive, diagonal skewer and clean V-shaped martini bowl on a slender stem.
# Construction reference: Original supplies triangular bowl and skewered olive; geometric circles/curves and shared stem junctions follow the common authoring guide.

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
    icon_id = 'martini-glass-with-skewered-olive'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'The diagonal skewer and oval olive must remain visible inside the bowl. Preserve compact garnish spacing and the wide martini rim at4px stroke.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'cf9bff6360ab3e03e0a81e3db0ee7638ebae40416f84eafd368ae14e3156b637'}
    aliases = ()
    keywords = ('appetizer',)

    def build(self):
        self.add_polyline('bowl',(4,10),(44,10),(24,32),closed=True)
        self.add_line('stem',(24,32),(24,44));self.add_line('base',(15,44),(33,44))
        self.relate('connect','bowl','stem');self.relate('connect','stem','base')
        curve(self,'olive',(23,21),((19,16),(25,10),(30,13)),((36,17),(29,25),(23,21)),closed=True)
        self.add_line('skewer-upper',(36,4),(30,13));self.add_line('skewer-lower',(23,21),(20,25))
        self.relate('connect','olive','skewer-upper');self.relate('connect','olive','skewer-lower');self.relate('connect','bowl','skewer-upper')
