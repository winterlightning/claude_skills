from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '25af2252-94aa-5683-bdb4-b15dc9190e60'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__man-glasses-1-avatar/20260929T095914Z-thuan-mac/reference/man glasses_25af2252-94aa-5683-bdb4-b15dc9190e60.svg'
AUTHOR = "gpt-6"

# Original/current comparison: The glasses merged into the head outline like goggles, and the ears and human bust proportions were lost.
# Revision plan: Restored separate lens circles, a short bridge and temple arms, visible ears and a broad shoulder curve.
# Construction reference: human_ref/user.svg: circular face and broad shoulders; original: round eyeglasses, ears and frontal bust

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
    icon_id = 'man-glasses-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    human_construction = "bust"
    exception = {'reason': 'Preserve facial glass rims, ears and shoulder contact within48px. The large circular head keeps the glasses visually separated from the face outline, with4px strokes and exact touching-ink bust construction.', 'approved_by': 'user-authorized-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '18e51c2bbf8b486836739f7674fb839d97708bc130ce04072808234555de331e'}
    aliases = ()
    keywords = ('man glasses',)

    def build(self):
        # Avatar construction: circular head/jaw r17; lower extreme37 and shoulder top41 are4 centerline units apart, so the ink touches.
        circle(self,'head',24,20,17)
        curve(self,'ear-left',(7,20),((2,17),(3,27),(9,28)))
        curve(self,'ear-right',(41,20),((46,17),(45,27),(39,28)))
        self.relate('connect','head','ear-left');self.relate('connect','head','ear-right')
        for side,cx in (('left',17),('right',31)):circle(self,'lens-'+side,cx,19,4)
        self.add_line('bridge',(21,19),(27,19))
        self.add_line('temple-left',(7,20),(13,19));self.add_line('temple-right',(35,19),(41,20))
        for side in ('left','right'):
            self.relate('connect','bridge','lens-'+side)
            self.relate('connect','temple-'+side,'lens-'+side)
            self.relate('connect','temple-'+side,'head')
        self.add_arc('shoulders',(4,46),(44,46),radius_x=20,radius_y=5)
        self.relate('connect','head','shoulders')
