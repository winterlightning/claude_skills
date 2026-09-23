"""Forensic knife and specimen beside a DNA double helix.
Symbol plan: preserve the reference's complete composition; shared parameters own repeated elements.
Keyshape SQUARE; exact profile envelope supplied by Keyshape.bounds_for.
Omissions: Middle DNA rungs omitted; two terminal rungs preserve ladder structure.
Lucide: none; rounded contour and coherent stroke construction where applicable.
Human reference: icon_set/references/human_ref/user.svg for portrait modules.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d6ecc97f-f19b-48b5-a88f-cd0c736478c1'
SOURCE_PATH='icon_set/work/todo-references/forensic science dna evidence_d6ecc97f-f19b-48b5-a88f-cd0c736478c1.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='forensic-dna-evidence'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('forensic', 'science', 'dna', 'evidence')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def box(self, name, x, y, w, h, r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            eid=f'{name}-{i}';ids.append(eid)
            if i%2:self.add_arc(eid,pts[i],pts[(i+1)%8],radius_x=r)
            else:self.add_line(eid,pts[i],pts[(i+1)%8])
        self.add_contour(name,*ids,closed=True)

    def build(self):

        self.add_polyline('blade',(6,28),(28,6),(34,12),(20,26),(6,28))
        self.add_line('handle-seam',(22,12),(28,18))
        self.relate('connect','blade','handle-seam')
        self.add_bezier('sample',(6,36),((6,42),(16,42),(16,38)),((16,37),(20,37),(20,36)))
        self.add_bezier('dna-left',(32,26),((32,32),(42,34),(42,42)))
        self.add_bezier('dna-right',(42,26),((42,32),(32,34),(32,42)))
        self.relate('connect','dna-left','dna-right')
        for y in (26,42):
            self.add_line('rung-'+str(y),(32,y),(42,y))
            self.relate('connect','rung-'+str(y),'dna-left','dna-right')

