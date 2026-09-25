"""Festival still life: upper-right diamond kite and lower-left three-sweet scalloped mound in bowl. Omit kite spars to keep the diamond opening clear; flowing tail remains.
No useful exact Lucide festival match; supplied still life establishes arrangement.
Keyshape SQUARE on SOLO48; exact envelope from the unchanged contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f6afb752-c918-40fd-9be7-5c7a79a0b099'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/makara sankranti_f6afb752-c918-40fd-9be7-5c7a79a0b099.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/makara sankranti_f6afb752-c918-40fd-9be7-5c7a79a0b099.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-013/references/makara sankranti_f6afb752-c918-40fd-9be7-5c7a79a0b099.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'kite-and-bowl-of-sweets-batch-013'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('kite', 'and', 'bowl', 'of', 'sweets')

    def build(self):

        def circle(name, x, y, r):
            self.add_arc(name+'-upper',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-lower',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_polyline('kite',(32,6),(42,14),(32,22),(22,14),closed=True)
        self.add_bezier('tail',(32,22),((32,32),(42,34),(42,42)))
        self.relate('connect','kite','tail')
        self.add_bezier('sweets',(6,34),((6,26),(9,24),(12,28)),((10,18),(18,18),(18,28)),((22,24),(24,26),(24,34)))
        self.add_line('rim',(6,34),(24,34))
        self.add_bezier('bowl',(24,34),((23,38),(21,42),(18,42)),((16,42),(14,42),(12,42)),((9,42),(7,38),(6,34)))
        self.add_contour('bowl-outline','rim','bowl',closed=True)
        self.relate('connect','sweets','bowl-outline')
