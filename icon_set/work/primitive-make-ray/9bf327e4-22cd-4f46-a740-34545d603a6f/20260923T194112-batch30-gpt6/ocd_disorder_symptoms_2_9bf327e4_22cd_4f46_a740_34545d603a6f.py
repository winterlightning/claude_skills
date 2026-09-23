from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9bf327e4-22cd-4f46-a740-34545d603a6f'
SOURCE_PATH = 'icon_set/work/todo-references/ocd disorder symptoms 2_9bf327e4-22cd-4f46-a740-34545d603a6f.svg'
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

    def build(self):

        self.add_arc('cranium',(12,20),(40,20),radius_x=14,radius_y=16)
        self.add_arc('back',(40,20),(35,34),radius_x=22)
        self.add_line('neck-back',(35,34),(35,44))
        self.add_polyline('face-neck',(12,20),(8,28),(12,28),(12,34),(20,34),(20,44))
        self.add_contour('profile-top','cranium','back','neck-back')
        self.relate('connect','profile-top','face-neck')
        for i,y in enumerate((15,24)):
            self.add_polyline(f'check-{i}',(19,y),(21,y+2),(24,y-2))
            self.add_line(f'text-{i}',(32,y),(33,y))
        self.add_polyline('empty-box',(25,33),(29,33),(29,37),(25,37),closed=True)
