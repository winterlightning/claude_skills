"""ocd disorder symptoms 2.
Left-facing head contains one check and an empty checkbox.
Vertical envelope reserves room for checklist; intentional side-profile asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9bf327e4-22cd-4f46-a740-34545d603a6f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/ocd disorder symptoms 2_9bf327e4-22cd-4f46-a740-34545d603a6f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A head silhouette containing an obsessive checklist.

    Plan: Left-facing profile with checklist inside; deliberate anatomical asymmetry.
    Construction reference: No useful Lucide match; supplied reference defines checklist profile.
    """
    icon_id = 'ocd-disorder-symptoms-2'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('ocd', 'disorder', 'symptoms', '2')
    # human_ref/user.svg inspected for contour economy. This is a connected head/neck profile, not a detached stick figure; no detached-head gap applies.

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-a', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-b', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded(self, name, left, top, right, bottom, radius=4):
        r=radius
        pts=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
             (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        names=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8]; n=f'{name}-{i}'; names.append(n)
            if i%2: self.add_arc(n,a,b,radius_x=r)
            else: self.add_line(n,a,b)
        self.add_contour(name,*names,closed=True)

    def clipboard(self):
        # Clip and board share the two nodes (16,12), (32,12).
        self.add_polyline('board', (16,12),(8,12),(8,44),(40,44),(40,12),(32,12))
        self.rounded('clip',16,4,32,12,4)
        self.relate('connect','board','clip')

    def cross(self, name, cx, cy, radius):
        for suffix,end in [('l',(cx-radius,cy)),('r',(cx+radius,cy)),('t',(cx,cy-radius)),('b',(cx,cy+radius))]:
            self.add_line(name+'-'+suffix,(cx,cy),end)
        self.relate('connect',*(name+'-'+s for s in ['l','r','t','b']))

    def build(self) -> None:
        self.add_arc('head-top',(8,20),(40,20),radius_x=16)
        self.add_line('neck-back',(40,20),(40,44))
        self.relate('connect','head-top','neck-back')
        self.add_polyline('face-neck',(8,20),(8,28),(16,28),(16,44))
        self.relate('connect','head-top','face-neck')
        self.add_polyline('check',(20,16),(24,20),(29,14))
        self.add_polyline('empty-box',(24,30),(32,30),(32,38),(24,38),closed=True)

# Repair plan: Left-facing head contains one check and an empty checkbox.
# Omissions: Repeated completed row and text rules omitted.
# Construction references: human_ref/full_body_ref.png: restrained human construction.
# Keyshape and proportions: Vertical envelope reserves room for checklist; intentional side-profile asymmetry.
