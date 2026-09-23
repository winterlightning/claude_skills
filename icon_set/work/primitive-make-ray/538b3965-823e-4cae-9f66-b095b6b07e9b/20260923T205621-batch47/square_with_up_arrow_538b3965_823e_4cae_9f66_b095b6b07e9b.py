"""Square with up arrow, reconstructed from the supplied reference.
Symbol plan: one complete composition; shared frame and repeated geometry parameters.
Lucide square-arrow-up informs tangent rounded corners and joined arrow construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '538b3965-823e-4cae-9f66-b095b6b07e9b'
SOURCE_PATH = 'icon_set/work/todo-references/square with up arrow_538b3965-823e-4cae-9f66-b095b6b07e9b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-with-up-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/signage'
    aliases = ()
    keywords = ('square', 'with', 'up', 'arrow')

    def build(self):
        # Open box and upward export arrow. The arrow owns the top extreme.
        # VRECT_L centerlines (8,4)-(40,44), ink (6,2)-(42,46).
        self.add_line('left-lip',(14,20),(12,20))
        self.add_arc('nw',(12,20),(8,24),radius_x=4,sweep=False)
        self.add_line('left',(8,24),(8,40))
        self.add_arc('sw',(8,40),(12,44),radius_x=4,sweep=False)
        self.add_line('base',(12,44),(36,44))
        self.add_arc('se',(36,44),(40,40),radius_x=4,sweep=False)
        self.add_line('right',(40,40),(40,24))
        self.add_arc('ne',(40,24),(36,20),radius_x=4,sweep=False)
        self.add_line('right-lip',(36,20),(34,20))
        self.add_contour('box','left-lip','nw','left','sw','base','se','right','ne','right-lip')
        self.up_arrow('arrow',24,4,32,8)


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

