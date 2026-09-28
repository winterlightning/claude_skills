'Koala: round head and ear, smooth sitting back and a single clear gripping arm on the branch.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95f00a8c-536e-5767-97fa-8968fad8e99a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__koala-with-branch/20260927T133723Z-thuan-mac-1/reference/koala bamboo_95f00a8c-536e-5767-97fa-8968fad8e99a.svg'
AUTHOR = "gpt-6"


class KoalaWithBranch(Solo48):
    icon_id = 'koala-with-branch-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('koala', 'branch', 'eucalyptus', 'holding', 'marsupial', 'australia', 'animal', 'sitting')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        # Both ears are part of one clean head silhouette, avoiding tight
        # overlapping ear strokes and restoring the original two-ear reading.
        head_curves = [
            ('crown-right',(20,8),((24,8),(27,9),(29,11))),
            ('right-ear-top',(29,11),((29,7),(31,6),(32,6))),
            ('right-ear-side',(32,6),((34,6),(34,10),(34,14))),
            ('right-ear-base',(34,14),((34,17),(32,19),(30,19))),
            ('right-cheek',(30,19),((30,21),(29,23),(28,24))),
            ('right-jaw',(28,24),((26,27),(23,28),(20,28))),
            ('left-jaw',(20,28),((17,28),(14,27),(12,24))),
            ('left-cheek',(12,24),((11,23),(10,21),(10,19))),
            ('left-ear-base',(10,19),((8,19),(6,17),(6,14))),
            ('left-ear-side',(6,14),((6,10),(6,6),(8,6))),
            ('left-ear-top',(8,6),((9,6),(11,7),(11,11))),
            ('crown-left',(11,11),((13,9),(16,8),(20,8))),
        ]
        for name, start, controls in head_curves:
            self.add_bezier(name,start,controls)
        self.add_contour('head',*(name for name,_,_ in head_curves),closed=True)
        self.add_line('nose',(20,17),(20,19))
        self.add_arc('back', (12, 24), (10, 36), radius_x=18, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('bottom', (10, 36), (20, 42), radius_x=10, radius_y=6, large_arc=False, sweep=False)
        self.add_line('foot', (20, 42), (30, 42))
        self.add_line('branch', (30, 42), (42, 22))
        self.add_line('arm', (28, 24), (36, 32))
        self.add_contour('body', *('back', 'bottom', 'foot'), closed=False)
        self.relate('connect', *('body', 'head'))
        self.relate('connect', *('branch', 'body'))
        self.relate('connect', *('arm', 'branch'))
        self.relate('connect', *('arm', 'head'))
