"""Electric Food Processor."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0220053c-adcd-4572-aebd-11002c5eeace'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/food processor_0220053c-adcd-4572-aebd-11002c5eeace.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'food-processor-with-feed-tube'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('processor', 'appliance', 'kitchen', 'bowl', 'feed tube', 'cooking', 'control')

    def build(self):
        # Plan: Food processor with feed tube, broad lidded bowl and rectangular motor base. Lucide blender shared axes and stacked parts. Control reduced to dot; fine bowl ticks omitted. Envelope (8,4)-(40,44).
        self.add_polyline('tube',(18,14),(18,4),(30,4),(30,14))
        self.add_polyline('lid',(8,14),(10,14),(18,14),(30,14),(38,14),(40,14));self.relate('connect','tube','lid')
        self.add_polyline('bowl',(10,14),(10,28),(38,28),(38,14))
        self.add_polyline('base',(10,28),(8,32),(8,44),(40,44),(40,32),(38,28))
        self.relate('connect','base','bowl')
        self.add_dot('control',(24,36))

        self.relate('connect','bowl','lid')
