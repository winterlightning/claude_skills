"""Square up left, reconstructed from the supplied reference.
Symbol plan: one complete composition; shared frame and repeated geometry parameters.
Lucide square-arrow-up informs tangent rounded corners and joined arrow construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0426472c-0785-4dc2-86f3-c6d7d6107f27'
SOURCE_PATH = 'icon_set/work/todo-references/square up left_0426472c-0785-4dc2-86f3-c6d7d6107f27.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-up-left'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/signage'
    aliases = ()
    keywords = ('square', 'up', 'left')

    def build(self):
        # Bent upward arrow with a leftward foot; intentional directional asymmetry.
        self.frame()
        tip=(27,15)
        self.add_polyline('head',(21,21),tip,(33,21))
        self.add_line('shaft-1',(15,33),(25,33))
        self.add_arc('elbow',(25,33),(27,31),radius_x=2,sweep=False)
        self.add_line('upright',(27,31),tip)
        self.add_contour('stem','shaft-1','elbow','upright')
        self.relate('connect','head','stem')


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

