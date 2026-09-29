from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5b0d6eeb-01ce-5e24-a6b5-c6b878c3f82b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__man-bow-avatar/20260929T095914Z-thuan-mac/reference/man bow_5b0d6eeb-01ce-5e24-a6b5-c6b878c3f82b.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The bow tie became a large crossing X attached to the torso and the hat was too blocky.
# Revision plan: Restored a smaller two-lobed bow tie, rounded hat crown, separate brim and circular jaw above broad shoulders.
# Construction reference: human_ref/user.svg: circular jaw and broad shoulders; original supplies the hat and separate bow-tie lobes

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
    icon_id = 'man-bow-avatar'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    human_construction = "bust"
    exception = {'reason': 'Preserve two bow-tie lobes beneath the hat and circular face, keeping them separate from the shoulders at48px. Compact bow interiors are intentional with4px strokes.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '4c2f76455bbd1ae384831db657ca1ba2b97d7508ff3aca640c58748de94951c6'}
    aliases = ()
    keywords = ('man bow',)

    def build(self):
        # Circular jaw r8 centered(24,13): lower extreme21; shoulder ellipse top25 gives exact touching ink.
        self.add_arc('jaw',(32,13),(16,13),radius_x=8)
        self.add_line('hat-left',(16,13),(16,9));self.add_arc('hat-tl',(16,9),(21,4),radius_x=5)
        self.add_line('hat-top',(21,4),(27,4));self.add_arc('hat-tr',(27,4),(32,9),radius_x=5)
        self.add_line('hat-right',(32,9),(32,13));self.add_contour('hat','hat-left','hat-tl','hat-top','hat-tr','hat-right')
        self.add_line('brim',(12,13),(36,13));self.relate('connect','hat','brim');self.relate('connect','jaw','brim')
        self.add_arc('shoulders',(4,44),(44,44),radius_x=20,radius_y=19)
        self.relate('connect','jaw','shoulders')
        self.add_polyline('bow-left',(16,31),(24,35),(16,39),closed=True)
        self.add_polyline('bow-right',(32,31),(32,39),(24,35),closed=True)
        self.relate('connect','bow-left','bow-right')
