"""A diagonal phone receiver inside a rounded square.
Plan: SQUARE preserves the enclosing sign and nine-unit content margins.
Reduction: Earpiece notches reduced to shallow shoulders; receiver band widened.
Construction: Lucide phone: outer curved sweep, inner return and flared end pads.
Layout: Receiver has deliberate diagonal orientation matching the reference despite the hangup filename."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '48b58407-6e7b-4cf9-b629-9742f8a963af'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_35/square phone hangup_48b58407-6e7b-4cf9-b629-9742f8a963af.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'square-phone-hangup'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('square', 'phone', 'hangup')

    def build(self):
        self.frame()
        # Rounded outer sweep with flared earpieces and a broad inner return.
        for j,(a,b) in enumerate(zip([(15,15),(23,15),(25,17)],[(23,15),(25,17),(24,18)])): self.add_line(f'upper-ear-{j}',a,b)
        self.add_bezier('inner-bend',(24,18),((25,21),(27,23),(30,24)))
        for j,(a,b) in enumerate(zip([(30,24),(31,23),(33,25)],[(31,23),(33,25),(33,33)])): self.add_line(f'lower-ear-{j}',a,b)
        self.add_arc('outer-bend',(33,33),(15,15),radius_x=18,sweep=True)
        self.add_contour('handset','upper-ear-0','upper-ear-1','upper-ear-2','inner-bend','lower-ear-0','lower-ear-1','lower-ear-2','outer-bend',closed=True)

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

