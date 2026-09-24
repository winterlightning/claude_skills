"""A notched airline boarding pass carries a right-facing airplane.
Symbol plan: Symmetric concave side notches on a horizontal ticket; asymmetric rising aircraft with swept wing and tail.
Keyshape visible bounds: (2, 6, 46, 42).
Construction references: Lucide tickets-plane and plane: ticket proportions and coherent plane contour; supplied reference: side notches and single prominent wing..
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9cbe2481-852f-43a0-a967-6cc8e7df1295'
SOURCE_PATH = 'pictographic-primitives/travel/plane boarding pass_9cbe2481-852f-43a0-a967-6cc8e7df1295.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'plane-boarding-pass'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('plane', 'boarding', 'pass')
    def build(self):
        # Ticket notches are concave semicircles on the two short edges.
        self.add_line('top',(4,8),(44,8))
        self.add_line('right-upper',(44,8),(44,21))
        self.add_arc('right-notch',(44,21),(44,27),radius_x=3,sweep=False)
        self.add_line('right-lower',(44,27),(44,40))
        self.add_line('bottom',(44,40),(4,40))
        self.add_line('left-lower',(4,40),(4,27))
        self.add_arc('left-notch',(4,27),(4,21),radius_x=3,sweep=False)
        self.add_line('left-upper',(4,21),(4,8))
        self.add_contour('ticket','top','right-upper','right-notch','right-lower','bottom','left-lower','left-notch','left-upper',closed=True)
        points=[(15,27),(20,31),(34,23)]
        self.add_line('tail-lower',points[0],points[1]);self.add_line('fuselage-lower',points[1],points[2])
        self.add_arc('nose',(34,23),(32,18),radius_x=3,sweep=False)
        points=[(32,18),(27,21),(21,17),(17,20),(23,24),(20,26),(17,24),(15,27)]
        members=['tail-lower','fuselage-lower','nose']
        for i,(a,b) in enumerate(zip(points,points[1:])):
            name=f'upper-{i}';self.add_line(name,a,b);members.append(name)
        self.add_contour('plane',*members,closed=True)

    def circle(self, name, cx, cy, r):
        self.add_arc(name+"-top", (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+"-bottom", (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+"-top", name+"-bottom", closed=True)

    def box(self, name, left, top, right, bottom, r=3):
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f"{name}-{i}"
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
            members.append(part)
        self.add_contour(name,*members,closed=True)
