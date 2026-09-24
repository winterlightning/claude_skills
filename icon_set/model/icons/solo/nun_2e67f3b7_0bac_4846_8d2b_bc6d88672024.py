"""nun.
Symmetric arch veil, circular face and cross give a very simplified nun portrait.
Square balances the veil and robe; face is enclosed by veil rather than a detached stick figure.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e67f3b7-0bac-4846-8d2b-bc6d88672024'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/nun_2e67f3b7-0bac-4846-8d2b-bc6d88672024.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A nun wearing a veil and a cross.

    Plan: Circular face, symmetric arched veil, detached shoulders and cross; shared human-reference vocabulary.
    Construction reference: No useful Lucide match; shared human_ref/user.svg supplies circular head and broad shoulders.
    """
    icon_id = 'nun'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('nun',)
    # human_ref/user.svg inspected. Face bottom centerline y=28, shoulder top y=36: centerline gap 8, ink gap 4. Face radius 7; symmetrical shoulders.

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
        self.add_arc('veil-top',(6,24),(42,24),radius_x=18)
        self.add_line('veil-base-1',(42,24),(42,42))
        self.add_line('veil-base-2',(42,42),(6,42))
        self.add_line('veil-base-3',(6,42),(6,24))
        self.add_contour('veil','veil-top','veil-base-1','veil-base-2','veil-base-3',closed=True)
        self.circle('face',24,20,5)
        self.add_polyline('cross-v',(24,33),(24,34),(24,42))
        self.add_polyline('cross-h',(20,34),(24,34),(28,34))
        self.relate('connect','cross-v','cross-h')
        self.relate('connect','cross-v','veil')

# Repair plan: Symmetric arch veil, circular face and cross give a very simplified nun portrait.
# Omissions: Forehead band, neck and shoulder seam omitted.
# Construction references: human_ref/user.svg: circular head vocabulary.
# Keyshape and proportions: Square balances the veil and robe; face is enclosed by veil rather than a detached stick figure.
