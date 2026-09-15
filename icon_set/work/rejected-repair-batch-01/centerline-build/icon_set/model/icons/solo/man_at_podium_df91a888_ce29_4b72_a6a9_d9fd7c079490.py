"""A speaker with a defined neck rises behind a wide lectern. Lucide users informs the rounded shoulders; tiny ear steps are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df91a888-ce29-4b72-a6a9-d9fd7c079490'
SOURCE_PATH = 'pictographic-primitives/users/man podium_df91a888-ce29-4b72-a6a9-d9fd7c079490.svg'
AUTHOR = 'gpt-6'


class ManAtPodium(Solo48):
    icon_id = 'man-at-podium'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/identity"
    aliases = ()
    keywords = ('man', 'podium', 'lectern', 'speaker', 'presentation', 'speech', 'person', 'talk')

    def build(self) -> None:
        # Square extremes (6,6)-(42,42); shoulders and neck mirror around x=24.
        self.add_arc('shoulder-left',(12,33),(18,27),radius_x=6)
        self.add_line('neck-left',(18,27),(18,24))
        self.add_arc('head',(18,24),(30,24),radius_x=10,large_arc=True)
        self.add_line('neck-right',(30,24),(30,27))
        self.add_arc('shoulder-right',(30,27),(36,33),radius_x=6)
        self.add_contour('speaker','shoulder-left','neck-left','head','neck-right','shoulder-right')
        self.add_polyline('lectern',(6,33),(12,33),(36,33),(42,33))
        self.add_line('leg-left',(12,33),(10,42))
        self.add_line('leg-right',(36,33),(38,42))
        self.relate('connect','speaker','lectern')
        for side in ('left','right'):
            self.relate('connect','lectern','leg-'+side)
            self.relate('connect','speaker','leg-'+side)
