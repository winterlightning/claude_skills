"""A raised index finger with thumb and palm below four dial strokes. Four dial marks form a 2x2 series; finger has an 8-unit-wide rounded cap. Deliberate hand asymmetry follows the source. Extremes (6,6)-(42,42). Human-reference.md and human_ref user/full-body inspected; no head-body pair exists.
Lucide hand: coherent round finger cap and continuous palm silhouette. Shared human references reviewed for rounded anatomy; head spacing does not apply.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ac8740e0-9a7e-4e67-901d-18b0353d7000'
SOURCE_PATH = 'icon_set/work/todo-references/dial finger_ac8740e0-9a7e-4e67-901d-18b0353d7000.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dial-finger'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/devices"
    aliases = ()
    keywords = ('dial', 'finger')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded(self, name, l, t, r, b, radius):
        q=radius
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
        for j in range(8):
            if j%2: self.add_arc(name+str(j),pts[j],pts[j+1],radius_x=q)
            else: self.add_line(name+str(j),pts[j],pts[j+1])
        self.add_contour(name, *(name+str(j) for j in range(8)), closed=True)

    def build(self):

        for row in range(2):
            for col in range(2):
                x,y=6+12*col,6+10*row
                self.add_line('key-'+str(row)+'-'+str(col),(x,y),(x+2,y))
        self.add_line('finger-left',(28,32),(28,20))
        self.add_arc('tip',(28,20),(36,20),radius_x=4)
        self.add_line('finger-right',(36,20),(36,28))
        self.add_bezier('palm-top',(36,28),((36,30),(42,30),(42,33)))
        self.add_line('palm-right',(42,33),(40,42))
        self.add_line('palm-left',(24,42),(18,31))
        self.add_bezier('thumb',(18,31),((15,25),(21,23),(24,28)))
        self.add_line('thumb-return',(24,28),(28,32))
        self.add_contour('hand','palm-left','thumb','thumb-return','finger-left','tip','finger-right','palm-top','palm-right')
