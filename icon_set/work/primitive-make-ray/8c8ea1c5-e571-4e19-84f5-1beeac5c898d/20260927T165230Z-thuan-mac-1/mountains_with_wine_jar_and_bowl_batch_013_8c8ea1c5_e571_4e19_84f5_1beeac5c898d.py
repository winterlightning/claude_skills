"""Two mountain peaks above a shallow bowl and capped wine jar. Remove cloud and snow decoration; maintain the two vessels and landscape hierarchy.
No useful exact Lucide festival match; supplied landscape and vessels establish arrangement.
Keyshape SQUARE on SOLO48; exact envelope from the unchanged contract.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8c8ea1c5-e571-4e19-84f5-1beeac5c898d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mountains-with-wine-jar-and-bowl-batch-013/20260927T164916Z-thuan-mac-1/reference/double ninth festival drink_8c8ea1c5-e571-4e19-84f5-1beeac5c898d.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/double ninth festival drink_8c8ea1c5-e571-4e19-84f5-1beeac5c898d.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-013/references/double ninth festival drink_8c8ea1c5-e571-4e19-84f5-1beeac5c898d.svg'
AUTHOR = "gpt-6"

class BatchIcon(Solo48):
    icon_id = 'mountains-with-wine-jar-and-bowl-batch-013'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('mountains', 'with', 'wine', 'jar', 'and', 'bowl')

    def build(self):

        def circle(name, x, y, r):
            self.add_arc(name+'-upper',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-lower',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_polyline('mountains',(6,20),(16,10),(24,20),(30,6),(42,18))
        self.add_line('bowl-rim',(6,32),(22,32))
        self.add_bezier('bowl',(22,32),((20,38),(20,42),(14,42)),((8,42),(8,38),(6,32)))
        self.add_contour('bowl-outline','bowl-rim','bowl',closed=True)
        self.add_polyline('jar',(32,28),(42,28),(42,38),(40,42),(34,42),(32,38),closed=True)
