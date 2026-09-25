"""Square this way up, reconstructed from the supplied reference.
Symbol plan: one complete composition; shared frame and repeated geometry parameters.
Lucide square-arrow-up informs tangent rounded corners and joined arrow construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ebf76c2-ab68-40f7-a75f-c12173488a0a'
SOURCE_PATH = 'icon_set/work/todo-references/square this way up_9ebf76c2-ab68-40f7-a75f-c12173488a0a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-this-way-up'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('square', 'this', 'way', 'up')

    def build(self):
        self.frame()
        # Matching upright arrows and a shared baseline, as on a shipping label.
        for i,x in enumerate((18,30)):
            n=f'arrow-{i}'; tip=(x,15)
            self.add_polyline(n+'-head',(x-2,19),tip,(x+2,19))
            self.add_line(n+'-shaft',(x,25),tip)
            self.relate('connect',n+'-head',n+'-shaft')
        self.add_line('baseline',(15,33),(33,33))


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

