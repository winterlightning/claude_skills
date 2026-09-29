from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8b9fd40e-030d-4023-801b-5cc4a7e68ec9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-reacting-to-spicy-food-batch-012-06/20260929T094854Z-thuan-mac/reference/spicy weakness person very spicy level_8b9fd40e-030d-4023-801b-5cc4a7e68ec9.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The profile face became an open C with a dot eye; it lost the distressed X eye and the body cue.
# Revision plan: Restored the open-mouth profile, distressed X eye and a tall flame beside the face.
# Construction reference: flame: asymmetric tongue and rounded lower lobe; supplied original: open-mouth profile and X eye

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
    icon_id = 'person-reacting-to-spicy-food-batch-012-06'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    exception = {'reason': 'The distressed profile, flame and shoulder cue need compact spacing. Keep all strokes4px while retaining the expression rather than substituting a generic dot eye.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '0c24f962f9b160a1ad506e40fa4f6d2fbbf62e6ac716a06d2267039f9f5d635d'}
    aliases = ()
    keywords = ('spicy weakness person very spicy level',)

    def build(self):
        # Face shown in profile rather than a generic floating circle; original X eye carries the reaction.
        curve(self,'flame',(10,4),((10,10),(15,13),(19,11)),((19,7),(17,5),(17,5)),((25,9),(27,20),(19,25)),((12,29),(5,22),(5,16)),((5,12),(8,7),(10,4)),closed=True)
        curve(self,'face',(29,16),((41,12),(46,21),(43,29)),((41,34),(37,35),(33,35)),((29,35),(25,34),(23,31)),((22,30),(22,28),(22,27)),((31,27),(32,21),(29,16)),closed=True)
        self.add_line('eye-a',(34,22),(38,26));self.add_line('eye-b',(38,22),(34,26));self.relate('connect','eye-a','eye-b')
        # Profile head lower extreme(33,35), shoulder top(33,43): exact4px visible gap.
        self.add_arc('shoulders',(22,46),(44,46),radius_x=11,radius_y=3)
