"""Sacred gateway interpretation: central tall arched portal, paired ascending side ornaments and spreading footings. Omit ambiguous interior miniature U and facial-looking band.
Lucide house: shared architectural side geometry; catalog gateway interpretation takes priority over ambiguous face-like source.
Keyshape SQUARE on SOLO48; exact envelope from the unchanged contract.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0fe4b8c7-0141-4d0d-8d06-c51c5d1dbb9a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arched-figure-beneath-paired-raised-forms-batch-013/20260927T160834Z-thuan-mac-1/reference/vaikuntha ekadashi_0fe4b8c7-0141-4d0d-8d06-c51c5d1dbb9a.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/vaikuntha ekadashi_0fe4b8c7-0141-4d0d-8d06-c51c5d1dbb9a.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-013/references/vaikuntha ekadashi_0fe4b8c7-0141-4d0d-8d06-c51c5d1dbb9a.svg'
AUTHOR = "gpt-6"

class BatchIcon(Solo48):
    icon_id = 'arched-figure-beneath-paired-raised-forms-batch-013'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('arched', 'figure', 'beneath', 'paired', 'raised', 'forms')

    def build(self):

        def circle(name, x, y, r):
            self.add_arc(name+'-upper',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-lower',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        # The source's main mass is round, with two detached angular forms above.
        circle('round-figure',24,32,10)
        self.add_polyline('upper-left-form',(6,12),(11,6),(16,10))
        self.add_polyline('upper-right-form',(42,12),(37,6),(32,10))
        self.add_polyline('left-side-form',(14,32),(6,32),(6,42))
        self.add_polyline('right-side-form',(34,32),(42,32),(42,42))
        self.relate('connect','round-figure','left-side-form')
        self.relate('connect','round-figure','right-side-form')
