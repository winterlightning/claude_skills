"""A design pen nib below a Bezier control diamond, horizontal handles, and two curved guide arms. Symmetry about x24; the upper diamond and nib remain distinct symbols. Extrema (6,6)-(42,42).
Lucide pen-tool: closed nib outline with circular vent and connected slit; source supplies upright orientation and Bezier controls.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd921e04-704d-5a6b-a478-676cad6d9f2e'
SOURCE_PATH = 'icon_set/work/todo-references/design pen tool_cd921e04-704d-5a6b-a478-676cad6d9f2e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'design-pen-tool'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/devices"
    aliases = ()
    keywords = ('design', 'pen', 'tool')

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

        self.add_polyline('control',(24,6),(28,10),(24,14),(20,10),closed=True)
        self.add_line('handle-left',(6,10),(16,10))
        self.add_line('handle-right',(32,10),(42,10))
        self.add_bezier('guide-left',(6,26),((6,18),(11,12),(16,10)))
        self.add_bezier('guide-right',(32,10),((37,12),(42,18),(42,26)))
        self.relate('connect','guide-left','handle-left')
        self.relate('connect','guide-right','handle-right')
        self.add_polyline('nib',(24,18),(34,32),(30,40),(18,40),(14,32),closed=True)
        self.circle('vent',24,32,2)
        self.add_line('slit',(24,18),(24,30))
        self.relate('connect','slit','nib')
        self.relate('connect','slit','vent')
        self.add_line('cuff-left',(18,40),(18,42))
        self.add_line('cuff-right',(30,40),(30,42))
        self.relate('connect','cuff-left','nib')
        self.relate('connect','cuff-right','nib')
