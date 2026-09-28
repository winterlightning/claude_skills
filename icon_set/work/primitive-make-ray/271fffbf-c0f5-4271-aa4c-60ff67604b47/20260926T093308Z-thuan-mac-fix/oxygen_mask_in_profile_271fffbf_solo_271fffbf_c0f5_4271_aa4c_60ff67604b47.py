'Side-facing head with rounded oxygen mask, cheek strap and long curved hose. Centerline8,4 to40,44.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "271fffbf-c0f5-4271-aa4c-60ff67604b47"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__oxygen-mask-in-profile-271fffbf-solo/20260926T093246Z-thuan-mac/reference/oxygen mask head side_271fffbf-c0f5-4271-aa4c-60ff67604b47.svg"
AUTHOR = "claude-opus-5-5"
CONSTRUCTION_REFERENCE = 'human_ref/user.svg: smooth round head; Lucide stethoscope: round tubing.'
OMISSIONS = 'Eye omitted, source continuous head/neck retained.'

def path(s,n,p,cs,closed=False):
    ids=[]
    for j,c in enumerate(cs):
        eid=f'{n}-{j}';q=c[-1]
        if c[0]=='L':s.add_line(eid,p,q)
        elif c[0]=='A':s.add_arc(eid,p,q,radius_x=c[1],radius_y=c[2],sweep=c[3])
        elif c[0]=='C':s.add_bezier(eid,p,(c[1],c[2],q))
        ids.append(eid);p=q
    s.add_contour(n,*ids,closed=closed)
def circle(s,n,x,y,r):
    path(s,n,(x-r,y),[('A',r,r,True,(x+r,y)),('A',r,r,True,(x-r,y))],True)

class Drawing(Solo48):
    icon_id = 'oxygen-mask-in-profile-271fffbf-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('oxygen', 'mask', 'head', 'side')
    def build(self):
        # Symbol plan (VRECT_L x8..44 wide 8..40, y4..44): head in profile facing
        # left. Head: forehead (14,18) up over the crown (26,4), round back of the
        # head at x40, nape curving in to the neck x36 down to y44.
        # Mask: cup from the nose bridge (14,18) out to x8 and round to a flat
        # bottom y36 (x12..20), cheek edge back up to (22,31) and the bridge.
        # Strap: (22,31) back toward the ear, free end (29,26).
        # Tube connector: box x12..20 from the mask bottom to y44.
        B = self.add_bezier
        L = self.add_line
        join = lambda a, b: self.relate('connect', a, b)
        B('head-front', (14, 18), ((14, 10), (19, 4), (26, 4)))
        B('head-crown', (26, 4), ((34, 4), (40, 10), (40, 18)))
        B('head-back', (40, 18), ((40, 26), (36, 32), (36, 36)))
        L('neck', (36, 36), (36, 44))
        self.add_contour('head', 'head-front', 'head-crown', 'head-back', 'neck')
        B('mask-front', (14, 18), ((11, 21), (8, 25), (8, 30)))
        B('mask-chin', (8, 30), ((8, 34), (9, 36), (12, 36)))
        L('mask-bottom', (12, 36), (20, 36))
        B('mask-corner', (20, 36), ((22, 36), (22, 34), (22, 31)))
        B('mask-cheek', (22, 31), ((22, 24), (18, 20), (14, 18)))
        self.add_contour('mask', 'mask-front', 'mask-chin', 'mask-bottom', 'mask-corner', 'mask-cheek', closed=True)
        join('head', 'mask')
        L('strap', (22, 31), (29, 26)); join('strap', 'mask')
        self.add_polyline('tube', (12, 36), (12, 44), (20, 44), (20, 36))
        join('tube', 'mask')
