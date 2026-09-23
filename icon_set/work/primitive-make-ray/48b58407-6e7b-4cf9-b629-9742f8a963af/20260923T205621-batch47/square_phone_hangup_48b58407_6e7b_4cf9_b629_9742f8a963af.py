"""Square phone hangup, reconstructed from the supplied reference.
Symbol plan: one complete composition; shared frame and repeated geometry parameters.
Lucide square-arrow-up informs tangent rounded corners and joined arrow construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '48b58407-6e7b-4cf9-b629-9742f8a963af'
SOURCE_PATH = 'icon_set/work/todo-references/square phone hangup_48b58407-6e7b-4cf9-b629-9742f8a963af.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-phone-hangup'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/signage'
    aliases = ()
    keywords = ('square', 'phone', 'hangup')

    def build(self):
        # Curved receiver, with round earpiece transitions; deliberate diagonal pose.
        self.frame()
        self.add_bezier('receiver',(16,15),
            ((12,17),(15,26),(22,31)),
            ((27,34),(32,33),(33,30)),
            ((34,28),(31,26),(29,25)),
            ((27,24),(27,28),(25,27)),
            ((22,25),(19,22),(20,21)),
            ((23,19),(20,16),(19,15)),
            ((18,14),(17,14),(16,15)))
        self.add_contour('handset','receiver',closed=True)


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

