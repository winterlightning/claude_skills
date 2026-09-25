"""Upright bow and taut string joined at tips; arrow crosses at drawn nock. Omit unidentified floating object and support from the source. Arrow points right to preserve a legible archery tool.
Lucide bow-arrow: bow, taut string and arrow as connected archery tool.
Keyshape SQUARE on SOLO48; exact envelope from the unchanged contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a5f26275-d65e-486b-af08-f77f5cc364f2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/vijayadashami_a5f26275-d65e-486b-af08-f77f5cc364f2.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/vijayadashami_a5f26275-d65e-486b-af08-f77f5cc364f2.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-013/references/vijayadashami_a5f26275-d65e-486b-af08-f77f5cc364f2.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'bow-and-arrow-with-unresolved-adjacent-forms-batch-013'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('bow', 'and', 'arrow', 'with', 'unresolved', 'adjacent', 'forms')

    def build(self):

        def circle(name, x, y, r):
            self.add_arc(name+'-upper',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-lower',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_bezier('bow-upper',(14,6),((21,6),(26,14),(26,24)))
        self.add_bezier('bow-lower',(26,24),((26,34),(21,42),(14,42)))
        self.add_contour('bow','bow-upper','bow-lower')
        self.add_polyline('string',(14,6),(6,24),(14,42))
        self.relate('connect','bow','string')
        self.add_polyline('shaft',(6,24),(26,24),(42,24))
        self.relate('connect','shaft','string')
        self.relate('connect','shaft','bow')
        self.add_polyline('arrowhead',(34,16),(42,24),(34,32))
        self.relate('connect','shaft','arrowhead')
