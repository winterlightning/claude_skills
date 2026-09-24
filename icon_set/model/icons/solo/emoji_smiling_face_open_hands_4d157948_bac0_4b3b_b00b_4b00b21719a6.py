"""Smiling face above two open hands. SQUARE exact extrema. Hand pairs share dimensions and mirror about x24; face remains circular."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID = '4d157948-bac0-4b3b-b00b-4b00b21719a6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/emoji smiling face open hands_4d157948-bac0-4b3b-b00b-4b00b21719a6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'emoji-smiling-face-open-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbol'
    aliases = ()
    keywords = ()
    # Keyshape chosen first; stroke centerlines inset 2 from the ink bounds.
    chosen_bounds = Keyshape.SQUARE.bounds_for(Profile.SOLO48)
    def build(self):
        # Circular face above two mirrored open mitten silhouettes.
        self.add_arc('head',(6,24),(42,24),radius_x=18)
        for name,x in [('left',18),('right',30)]:
            self.add_line('eye-'+name,(x-1,18),(x+1,18))
        self.add_arc('smile',(20,26),(28,26),radius_x=4,radius_y=2,sweep=False)
        for name,sign in [('left',1),('right',-1)]:
            def p(x,y): return (x if sign==1 else 48-x,y)
            self.add_polyline(name+'-fingers',p(7,37),p(6,34),p(9,32),p(13,35),p(15,33),p(17,37))
            self.add_arc(name+'-palm',p(17,37),p(7,37),radius_x=5,sweep=sign==1)
            self.relate('connect',name+'-fingers',name+'-palm')
