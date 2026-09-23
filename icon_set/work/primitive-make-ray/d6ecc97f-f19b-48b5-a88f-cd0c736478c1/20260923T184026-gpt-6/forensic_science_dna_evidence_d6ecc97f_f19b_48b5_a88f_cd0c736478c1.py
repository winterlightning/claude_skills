"""A forensic scalpel above a sample trace beside a DNA helix.
Construction: dna. DNA rungs reduced to the two end rungs; small blade details omitted.
Keyshape SQUARE; extremes are fixed by SOLO48. All dimensions are authored locally.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd6ecc97f-f19b-48b5-a88f-cd0c736478c1'
SOURCE_PATH = 'icon_set/work/todo-references/forensic science dna evidence_d6ecc97f-f19b-48b5-a88f-cd0c736478c1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'forensic-science-dna-evidence'
    keyshape = Keyshape.SQUARE
    # Declared visible-ink extrema: (4, 4, 44, 44).
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('forensic', 'science', 'dna', 'evidence')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def rect(self, name, x, y, w, h, r=2):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; n=f'{name}-{i}'
            if i%2: self.add_arc(n,a,b,radius_x=r)
            else: self.add_line(n,a,b)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def build(self):

        # Plan: diagonal scalpel in upper left; trace below; mirrored helix right.
        self.add_bezier('scalpel',(6,28),((12,28),(19,24),(26,16)),((31,11),(34,6),(29,6)),((27,6),(26,6),(23,9)))
        self.add_line('blade-edge',(23,9),(6,28))
        self.add_contour('knife','scalpel','blade-edge',closed=True)
        self.add_line('blade-join',(20,13),(24,17))
        self.relate('connect','knife','blade-join')
        self.add_bezier('sample',(7,36),((6,42),(16,42),(17,38)),((18,34),(21,38),(22,32)))
        for side in (-1,1):
            x=36+side*6
            self.add_bezier('helix-'+str(side),(x,24),((x,32),(36-side*6,34),(36-side*6,42)))
        self.add_line('rung-top',(30,24),(42,24))
        self.add_line('rung-bottom',(30,42),(42,42))
        self.relate('connect','helix--1','helix-1','rung-top','rung-bottom')
