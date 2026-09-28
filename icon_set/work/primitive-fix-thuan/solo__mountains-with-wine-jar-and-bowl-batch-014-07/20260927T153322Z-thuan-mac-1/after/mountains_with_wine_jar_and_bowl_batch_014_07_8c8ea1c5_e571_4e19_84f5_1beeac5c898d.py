"""Mountain with Wine Jar and Bowl.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Mountain skyline over squat capped wine jar and bowl.
Reduction: Omit cloud and scalloped band; retain both vessels.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8c8ea1c5-e571-4e19-84f5-1beeac5c898d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mountains-with-wine-jar-and-bowl-batch-014-07/20260927T153322Z-thuan-mac-1/reference/double ninth festival drink_8c8ea1c5-e571-4e19-84f5-1beeac5c898d.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/double ninth festival drink_8c8ea1c5-e571-4e19-84f5-1beeac5c898d.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-014/references/double ninth festival drink_8c8ea1c5-e571-4e19-84f5-1beeac5c898d.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'mountains-with-wine-jar-and-bowl-batch-014-07'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('mountains', 'wine', 'jar', 'bowl', 'cloud', 'festival')

    def build(self):
        # Rounded twin mountain ridges behind a bowl and a wine jar.
        self.add_bezier('left-rise',(6,20),((9,12),(12,6),(16,6)))
        self.add_bezier('left-fall',(16,6),((19,6),(20,13),(22,20)))
        self.add_bezier('right-rise',(22,20),((26,12),(28,6),(32,6)))
        self.add_bezier('right-fall',(32,6),((36,6),(39,13),(42,20)))
        self.add_contour('mountains','left-rise','left-fall','right-rise','right-fall')
        self.add_line('jar-top',(32,28),(38,28))
        self.add_arc('jar-ur',(38,28),(42,32),radius_x=4,sweep=True)
        self.add_line('jar-right',(42,32),(42,38))
        self.add_arc('jar-lr',(42,38),(38,42),radius_x=4,sweep=True)
        self.add_line('jar-bottom',(38,42),(32,42))
        self.add_arc('jar-ll',(32,42),(28,38),radius_x=4,sweep=True)
        self.add_line('jar-left',(28,38),(28,32))
        self.add_arc('jar-ul',(28,32),(32,28),radius_x=4,sweep=True)
        self.add_contour('jar','jar-top','jar-ur','jar-right','jar-lr','jar-bottom','jar-ll','jar-left','jar-ul',closed=True)
        self.add_line('bowl-rim',(6,32),(20,32))
        self.add_bezier('bowl-body',(20,32),((20,42),(6,42),(6,32)))
        self.add_contour('bowl','bowl-rim','bowl-body',closed=True)
