"""A data lake with the two literal rows 10100 and 01100 above two wave strokes. Repeated binary cells share a width and row step; wave lobes repeat on a 12-unit step. Four centerline extremes: (6,6)-(42,42).
Lucide database inspected; its cylinder is not a useful match for the requested binary-over-water composition.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e8929314-39ec-46c6-9cfb-5107ebede2dc'
SOURCE_PATH = 'icon_set/work/todo-references/data lake code_e8929314-39ec-46c6-9cfb-5107ebede2dc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'data-lake-code'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/devices"
    aliases = ()
    keywords = ('data', 'lake', 'code')

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

        for row,text in enumerate(('10100','01100')):
            y=6+row*14
            for col,digit in enumerate(text):
                x=6+col*8
                p='digit-'+str(row)+'-'+str(col)
                if digit=='1': self.add_line(p,(x+2,y),(x+2,y+8))
                else: self.rounded(p,x,y,x+4,y+8,2)
        for row,y in enumerate((32,40)):
            for col in range(3):
                x=6+12*col
                self.add_bezier('wave-'+str(row)+'-'+str(col),(x,y),((x+3,y+3),(x+9,y+3),(x+12,y)))
            self.add_contour('water-'+str(row),*('wave-'+str(row)+'-'+str(col) for col in range(3)))
