from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0b6fcfb0-13db-4df2-9172-e8f486788553'
SOURCE_PATH = 'icon_set/work/todo-references/office sign document_0b6fcfb0-13db-4df2-9172-e8f486788553.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A document with a diagonal signing pen.

    Plan: Open page outline around the diagonal pen; coherent pointed pen contour.
    Construction reference: file-pen: diagonal writing tool with an open page boundary.
    """
    icon_id = 'office-sign-document'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('office', 'sign', 'document')

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

        self.add_polyline('page',(40,12),(40,4),(8,4),(8,44),(40,44),(40,32))
        self.add_polyline('pen',(16,34),(20,22),(32,10),(40,18),(28,30),(16,34))
        self.add_line('pen-band',(28,14),(36,22)); self.relate('connect','pen-band','pen')
