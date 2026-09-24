"""A design pen nib below a Bezier control diamond, horizontal handles, and two curved guide arms. Symmetry about x24; the upper diamond and nib remain distinct symbols. Extrema (6,6)-(42,42).
Lucide pen-tool: closed nib outline with circular vent and connected slit; source supplies upright orientation and Bezier controls.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'cd921e04-704d-5a6b-a478-676cad6d9f2e'
SOURCE_PATH = 'pictographic-primitives/design/design pen tool_cd921e04-704d-5a6b-a478-676cad6d9f2e.svg'
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
        # Wider control diamond shares genuine handle endpoints.
        self.add_polyline('control',(24,6),(30,12),(24,18),(18,12),closed=True)
        for name,left in [('left',True),('right',False)]:
            x,tip=(6,18) if left else (42,30)
            self.add_line('handle-'+name,(x,12),(tip,12))
            self.add_bezier('guide-'+name,(x,28),((x,20),(tip,16),(tip,12)))
            self.relate('connect','guide-'+name,'handle-'+name)
            self.relate('connect','control','handle-'+name)
            self.relate('connect','control','guide-'+name)
        self.add_polyline('nib',(24,26),(34,34),(30,42),(18,42),(14,34),closed=True)
        self.circle('vent',24,35,2)
        self.add_line('slit',(24,26),(24,33))
        self.relate('connect','slit','nib')
        self.relate('connect','slit','vent')
