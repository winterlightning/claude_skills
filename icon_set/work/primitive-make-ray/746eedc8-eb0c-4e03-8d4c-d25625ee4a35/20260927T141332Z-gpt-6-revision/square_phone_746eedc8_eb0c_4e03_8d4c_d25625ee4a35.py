"""A diagonal phone receiver inside a rounded square.
Plan: SQUARE preserves the enclosure and inset receiver.
Reduction: Earpiece notches reduced to shallow shoulders; receiver band widened.
Construction: Lucide phone: smooth outer sweep, broad inner return and distinct end pads.
Layout: Directional receiver is intentionally asymmetric inside the symmetric frame."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '746eedc8-eb0c-4e03-8d4c-d25625ee4a35'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__square-phone/20260927T140026Z-thuan-mac-1/reference/square phone_746eedc8-eb0c-4e03-8d4c-d25625ee4a35.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'square-phone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('square', 'phone')

    def build(self):
        self.frame()
        self.add_line('upper-ear-0',(14,14),(21,14))
        self.add_line('upper-ear-1',(21,14),(25,18))
        self.add_line('upper-ear-2',(25,18),(22,21))
        self.add_bezier('inner-sweep',(22,21),((23,23),(25,25),(28,26)))
        self.add_line('lower-ear-0',(28,26),(31,23))
        self.add_line('lower-ear-1',(31,23),(35,27))
        self.add_line('lower-ear-2',(35,27),(35,34))
        self.add_bezier('outer-sweep',(35,34),((26,39),(10,27),(14,14)))
        self.add_contour('handset','upper-ear-0','upper-ear-1','upper-ear-2','inner-sweep','lower-ear-0','lower-ear-1','lower-ear-2','outer-sweep',closed=True)

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def frame(self):
        # SQUARE extremes: centerlines (6,6)-(42,42), ink (4,4)-(44,44).
        # Shared quarter-circle corners give a tangent-continuous square.
        lo, hi, r = 6, 42, 4
        nodes = [(lo+r,lo),(hi-r,lo),(hi,lo+r),(hi,hi-r),
                 (hi-r,hi),(lo+r,hi),(lo,hi-r),(lo,lo+r)]
        members=[]
        for i,a in enumerate(nodes):
            b=nodes[(i+1)%8]; name=f'frame-{i}'; members.append(name)
            if i%2: self.add_arc(name,a,b,radius_x=r)
            else: self.add_line(name,a,b)
        self.add_contour('frame',*members,closed=True)

    def up_arrow(self, name, x, top, bottom, half):
        tip=(x,top)
        self.add_polyline(name+'-head',(x-half,top+half),tip,(x+half,top+half))
        self.add_line(name+'-shaft',(x,bottom),tip)
        self.relate('connect',name+'-head',name+'-shaft')

