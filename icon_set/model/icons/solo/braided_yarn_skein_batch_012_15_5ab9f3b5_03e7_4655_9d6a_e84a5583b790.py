"""Braided Skein of Yarn.

SOLO48 visible bounds: (4, 4, 44, 44). Centerline extremes: (6, 6, 42, 42).

Symbol plan: Diagonal skein with overlapping rounded lobes and flowing strand bands.
Reduction: Reduce braid to three broad lobes and two seams.
Construction reference: No useful local Lucide subject match; supplied reference governs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ab9f3b5-03e7-4655-9d6a-e84a5583b790'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/hobbies/yarn_5ab9f3b5-03e7-4655-9d6a-e84a5583b790.svg'
SAVED_REFERENCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/yarn_5ab9f3b5-03e7-4655-9d6a-e84a5583b790.svg'
EXPORTED_REFERENCE_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-012/references/yarn_5ab9f3b5-03e7-4655-9d6a-e84a5583b790.svg'
AUTHOR = "gpt-6"
BATCH_AUTHORING_RUN = "20260917-011-015"


class GeneratedSolo(Solo48):
    icon_id = 'braided-yarn-skein-batch-012-15'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    categories = ("primitives", "hobbies")
    aliases = ()
    keywords = ('yarn', 'skein', 'braid', 'thread', 'craft', 'textile')

    def build(self):
        self.add_bezier('skein-1', (6, 32), ((6, 23), (12, 22), (14, 20)))
        self.add_bezier('skein-2', (14, 20), ((14, 12), (22, 12), (24, 12)))
        self.add_bezier('skein-3', (24, 12), ((28, 6), (34, 6), (36, 6)))
        self.add_bezier('skein-4', (36, 6), ((40, 6), (42, 10), (42, 16)))
        self.add_bezier('skein-5', (42, 16), ((42, 24), (34, 26), (34, 28)))
        self.add_bezier('skein-6', (34, 28), ((34, 36), (28, 36), (26, 36)))
        self.add_bezier('skein-7', (26, 36), ((22, 42), (16, 42), (14, 42)))
        self.add_bezier('skein-8', (14, 42), ((8, 42), (6, 38), (6, 32)))
        self.add_contour('skein', 'skein-1', 'skein-2', 'skein-3', 'skein-4', 'skein-5', 'skein-6', 'skein-7', 'skein-8', closed=True)
        self.add_bezier('strand-a-1', (14, 20), ((24, 20), (16, 36), (26, 36)))
        self.add_contour('strand-a', 'strand-a-1', closed=False)
        self.add_bezier('strand-b-1', (24, 12), ((34, 12), (26, 28), (34, 28)))
        self.add_contour('strand-b', 'strand-b-1', closed=False)
        self.relate("connect", 'skein', 'strand-a')
        self.relate("connect", 'skein', 'strand-b')
