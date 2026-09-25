"""Cheetah face with rounded ears and paired tear marks. Lucide cat informs mirrored head construction. Nose reduced to an open chevron ; mouth omitted for clearance; cheek marks carry species identity."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ec57f29-8f61-5416-9fb6-9743aae76de5'
SOURCE_PATH = 'pictographic-primitives/animals/leopard head front_6ec57f29-8f61-5416-9fb6-9743aae76de5.svg'
AUTHOR = 'gpt-6'


class CheetahFace(Solo48):
    icon_id = 'cheetah-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('cheetah', 'leopard', 'face', 'head', 'big cat', 'tear marks', 'feline', 'wildlife')

    def build(self) -> None:
        # Exact visible extremes: (0, 3, 48, 45); centerline inset 2.
        self.add_arc('crown', (14, 10), (34, 10), radius_x=18, radius_y=8, sweep=True, large_arc=False)
        self.add_bezier('ear-right-top', (34, 10), *(((34.57884175, 7.63438391), (37.10343542, 6), (40, 6)),))
        self.add_bezier('ear-right-round', (40, 6), *(((41.4191706, 7.2570869), (42, 9.11095735), (42, 11)),))
        self.add_bezier('ear-right-side', (42, 11), *(((42, 12.85640646), (42, 15.14359354), (42, 17)),))
        self.add_bezier('cheek-right', (42, 17), *(((41.62781329, 30.96743587), (33.67692068, 42), (24, 42)),))
        self.add_bezier('cheek-left', (24, 42), *(((14.32307932, 42), (6.37218671, 30.96743587), (6, 17)),))
        self.add_bezier('ear-left-side', (6, 17), *(((6, 15.14359354), (6, 12.85640646), (6, 11)),))
        self.add_bezier('ear-left-round', (6, 11), *(((6, 9.11095735), (6.5808294, 7.2570869), (8, 6)),))
        self.add_bezier('ear-left-top', (8, 6), *(((10.89656458, 6), (13.42115825, 7.63438391), (14, 10)),))
        self.add_contour('outline', 'crown', 'ear-right-top', 'ear-right-round', 'ear-right-side', 'cheek-right', 'cheek-left', 'ear-left-side', 'ear-left-round', 'ear-left-top', closed=True)
        self.add_line('eye-left',(17,20),(20,20))
        self.add_bezier('tear-left',(20,20),((20,22),(20,23),(19,24)))
        self.add_contour('mark-left', 'eye-left', 'tear-left', closed=False)
        self.add_line('eye-right',(31,20),(28,20))
        self.add_bezier('tear-right',(28,20),((28,22),(28,23),(29,24)))
        self.add_contour('mark-right', 'eye-right', 'tear-right', closed=False)
        self.add_polyline('nose',(21,32),(24,33),(27,32))
