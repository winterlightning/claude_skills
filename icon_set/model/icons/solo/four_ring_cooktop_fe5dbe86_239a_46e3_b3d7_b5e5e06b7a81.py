"""Four Burner Stove Top."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fe5dbe86-239a-46e3-b3d7-b5e5e06b7a81'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/cooktop_fe5dbe86-239a-46e3-b3d7-b5e5e06b7a81.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-ring-cooktop'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('cooktop', 'burner', 'stove', 'kitchen', 'cooking', 'appliance', 'hob')

    def build(self):
        # Plan: Four round burner rings inside a cooktop indicated by four corner brackets. Shared two-by-two spacing. Full frame reduced to corners to keep all four ring interiors. No exact Lucide match. Bounds (6,6)-(42,42).
        for i,(x,y) in enumerate(((16,16),(32,16),(16,32),(32,32))):
         self.add_arc(f'ring-t-{i}',(x-4,y),(x+4,y),radius_x=4)
         self.add_arc(f'ring-b-{i}',(x+4,y),(x-4,y),radius_x=4)
         self.add_contour(f'burner-{i}',f'ring-t-{i}',f'ring-b-{i}',closed=True)
        for i,(x,y,sx,sy) in enumerate(((6,6,1,1),(42,6,-1,1),(6,42,1,-1),(42,42,-1,-1))):
         self.add_polyline(f'corner-{i}',(x,y+sy*2),(x,y),(x+sx*2,y))
