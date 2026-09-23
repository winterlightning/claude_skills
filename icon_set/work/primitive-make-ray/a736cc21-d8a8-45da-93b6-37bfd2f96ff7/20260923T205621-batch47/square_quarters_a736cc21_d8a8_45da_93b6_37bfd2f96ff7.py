"""Square quarters, reconstructed from the supplied reference.
Symbol plan: one complete composition; shared frame and repeated geometry parameters.
Lucide square-arrow-up informs tangent rounded corners and joined arrow construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a736cc21-d8a8-45da-93b6-37bfd2f96ff7'
SOURCE_PATH = 'icon_set/work/todo-references/square quarters_a736cc21-d8a8-45da-93b6-37bfd2f96ff7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-quarters'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/signage'
    aliases = ()
    keywords = ('square', 'quarters')

    def build(self):
        self.frame()
        # Nested grid: four equal cells, shared center and attachment nodes.
        lo,c,hi=15,24,33
        nodes=[(lo,lo),(c,lo),(hi,lo),(hi,c),(hi,hi),(c,hi),(lo,hi),(lo,c)]
        self.add_polyline('grid',*nodes,closed=True)
        for name,p in [('north',(c,lo)),('east',(hi,c)),('south',(c,hi)),('west',(lo,c))]:
            self.add_line(name,p,(c,c))
            self.relate('connect','grid',name)
        self.relate('connect','north','east','south','west')


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

