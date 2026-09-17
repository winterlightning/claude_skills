"""Electric Rice Cooker."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48f160bd-d445-4b9a-bc62-1faffcd6a1ae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/rice cooker_48f160bd-d445-4b9a-bc62-1faffcd6a1ae.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arched-electric-rice-cooker'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('rice cooker', 'rice', 'appliance', 'handle', 'control', 'kitchen', 'cooking')

    def build(self):
        # Plan: Tall arched rice cooker with inset arch handle and attached blank control panel. Lucide cooking-pot shared lid structure. Fine indicator omitted. Mirrored envelope (8,4)-(40,44).
        self.add_bezier('dome',(8,22),((8,12),(14,4),(24,4)),((34,4),(40,12),(40,22)))
        self.add_polyline('lid',(8,22),(16,22),(32,22),(40,22));self.relate('connect','dome','lid')
        self.add_arc('handle',(16,22),(32,22),radius_x=8,radius_y=9);self.relate('connect','handle','lid')
        self.add_line('right',(40,22),(40,36));self.add_arc('br',(40,36),(32,44),radius_x=8)
        self.add_line('base',(32,44),(16,44));self.add_arc('bl',(16,44),(8,36),radius_x=8)
        self.add_line('left',(8,36),(8,22))
        for a,b in (('right','br'),('br','base'),('base','bl'),('bl','left'),('left','lid'),('right','lid'),('left','dome'),('right','dome')):self.relate('connect',a,b)
        self.add_polyline('panel',(16,44),(16,32),(32,32),(32,44))
        for n in ('base','bl','br'):self.relate('connect','panel',n)
