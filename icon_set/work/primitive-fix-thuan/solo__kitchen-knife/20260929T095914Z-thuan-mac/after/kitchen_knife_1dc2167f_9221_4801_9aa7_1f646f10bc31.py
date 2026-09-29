from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1dc2167f-9221-4801-9aa7-1f646f10bc31'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kitchen-knife/20260929T095914Z-thuan-mac/reference/knife edge_1dc2167f-9221-4801-9aa7-1f646f10bc31.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The horizontal kitchen knife was changed into a diagonal curved dagger.
# Revision plan: Restored a horizontal straight-backed chef blade with a curved cutting edge and a rounded capsule handle.
# Construction reference: No useful local chef-knife match used; original supplies the horizontal silhouette, straight spine and curved cutting edge.

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
    icon_id = 'kitchen-knife'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'Preserve the narrow horizontal chef-knife proportions instead of bending or widening it to fill the keyshape. The drawing retains4px strokes and a clear8-unit handle interior.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '44e02c7fa1d83451cf8a9676cf764099442779816247e90343331269bb03c9d6'}
    aliases = ()
    keywords = ('knife edge',)

    def build(self):
        # Natural horizontal profile, with a shared heel and no decorative details.
        self.add_polyline('blade-top-heel',(4,18),(28,18),(28,26),(28,30))
        curve(self,'cutting-edge',(28,30),((13,30),(7,28),(4,18)))
        # The top/heel polyline is already a joined path; connect the smooth cutting edge at both ends.
        self.relate('connect','blade-top-heel','cutting-edge')
        self.add_line('handle-top',(28,18),(40,18))
        self.add_arc('handle-end',(40,18),(40,26),radius_x=4)
        self.add_line('handle-bottom',(40,26),(28,26))
        self.add_contour('handle','handle-top','handle-end','handle-bottom')
        self.relate('connect','blade-top-heel','handle')
