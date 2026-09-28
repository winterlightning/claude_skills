"""Sacred gateway interpretation: central tall arched portal, paired ascending side ornaments and spreading footings. Omit ambiguous interior miniature U and facial-looking band.
Lucide house: shared architectural side geometry; catalog gateway interpretation takes priority over ambiguous face-like source.
Keyshape SQUARE on SOLO48; exact envelope from the unchanged contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fe4b8c7-0141-4d0d-8d06-c51c5d1dbb9a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/vaikuntha ekadashi_0fe4b8c7-0141-4d0d-8d06-c51c5d1dbb9a.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/vaikuntha ekadashi_0fe4b8c7-0141-4d0d-8d06-c51c5d1dbb9a.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-013/references/vaikuntha ekadashi_0fe4b8c7-0141-4d0d-8d06-c51c5d1dbb9a.svg'
AUTHOR = 'gpt-6'

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

        self.add_arc('arch',(14,24),(34,24),radius_x=10,radius_y=18)
        self.add_polyline('right-pier',(34,24),(34,42),(42,42))
        self.add_polyline('left-pier',(6,42),(14,42),(14,24))
        self.relate('connect','left-pier','arch')
        self.relate('connect','right-pier','arch')
        for side in (-1,1):
         x=24+side*18
         self.add_polyline('ornament-'+str(side),(x,23),(x,10),(x-side*2,6))
