"""Christmas Bauble.

Plan: Circular bauble with a round hanging loop. Reduce cap height to its attachment at the top of the ball. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39af05ac-7d1b-56a1-b0fd-80e5d7b4dc9a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/christmas tree ornament_39af05ac-7d1b-56a1-b0fd-80e5d7b4dc9a.svg'
AUTHOR = 'gpt-6'

class ChristmasBauble(Solo48):
    icon_id = 'christmas-bauble'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/holidays"
    aliases = ()
    keywords = ('christmas', 'bauble')

    def build(self):
        for name,x,y,r in [('ball',24,28,16),('loop',24,8,4)]:
         self.add_arc(name+'-r',(x,y-r),(x,y+r),radius_x=r)
         self.add_arc(name+'-l',(x,y+r),(x,y-r),radius_x=r)
         self.add_contour(name,name+'-r',name+'-l',closed=True)
        self.relate('connect','ball','loop')
