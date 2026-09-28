"""Square phone, reconstructed from the supplied reference.
Symbol plan: one complete composition; shared frame and repeated geometry parameters.
Lucide square-arrow-up informs tangent rounded corners and joined arrow construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '746eedc8-eb0c-4e03-8d4c-d25625ee4a35'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_35/square phone_746eedc8-eb0c-4e03-8d4c-d25625ee4a35.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'square-phone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/signage'
    aliases = ()
    keywords = ('square', 'phone')

    def build(self):
        self.frame()
        # Rounded outer sweep with flared earpieces and a broad inner return.
        for j,(a,b) in enumerate(zip([(15,15),(23,15),(27,19)],[(23,15),(27,19),(25,21)])): self.add_line(f'upper-ear-{j}',a,b)
        self.add_arc('inner-bend',(25,21),(27,23),radius_x=10,sweep=False)
        for j,(a,b) in enumerate(zip([(27,23),(29,21),(33,25)],[(29,21),(33,25),(33,33)])): self.add_line(f'lower-ear-{j}',a,b)
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

