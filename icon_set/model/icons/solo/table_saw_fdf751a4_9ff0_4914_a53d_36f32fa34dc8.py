'Table saw: independent spacing revision.\n\nBroad blade replaces cramped tooth notches; keep table, legs and eight-unit brace gap.\nNative solo family, SQUARE keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fdf751a4-9ff0-4914-a53d-36f32fa34dc8'
SOURCE_PATH = 'pictographic-primitives/tools/sawmill table_fdf751a4-9ff0-4914-a53d-36f32fa34dc8.svg'
AUTHOR = 'gpt-6'

class TableSaw(Solo48):
    icon_id = 'table-saw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    categories = ('primitives', 'tools')
    aliases = ()
    keywords = ('table saw', 'saw', 'blade', 'workbench', 'woodworking', 'sawmill', 'cutting', 'power tool')

    def build(self):
        self.add_polyline('table',(6, 22),(12, 22),(36, 22),(42, 22),(42, 30),(38, 30),(10, 30),(6, 30),closed=True)
        self.add_arc('blade',(12, 22),(36, 22),radius_x=12,radius_y=16,sweep=True)
        self.add_polyline('left-leg',(10, 30),(10, 38),(10, 42),closed=False)
        self.add_polyline('right-leg',(38, 30),(38, 38),(38, 42),closed=False)
        self.add_line('brace',(10, 38),(38, 38))
        self.relate('connect','blade','table')
        self.relate('connect','left-leg','table')
        self.relate('connect','right-leg','table')
        self.relate('connect','brace','left-leg')
        self.relate('connect','brace','right-leg')
