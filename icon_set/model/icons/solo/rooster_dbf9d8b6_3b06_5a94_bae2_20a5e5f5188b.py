"""Rooster with scalloped base and three-lobed crown. Lucide bird informs beak attachment. Centerline (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dbf9d8b6-3b06-5a94-bae2-20a5e5f5188b'
SOURCE_PATH = 'pictographic-primitives/animals/rooster_dbf9d8b6-3b06-5a94-bae2-20a5e5f5188b.svg'
AUTHOR = 'gpt-6'


class RoosterWithScallopedBase(Solo48):
    icon_id = 'rooster-with-scalloped-base'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('rooster', 'cockerel', 'comb', 'wattle', 'beak', 'farm', 'poultry', 'bird')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('body-1',(8, 25),*(((8, 18.74424516), (11.57447263, 13.52127822), (17, 13)),))
        self.add_arc('body-2',(17, 13),(29, 24),radius_x=12,radius_y=12,large_arc=False,sweep=True)
        self.add_line('body-3-1',(29,24),(29,34))
        self.add_line('body-3-2',(29,34),(29,44))
        self.add_bezier('body-4',(29,44),((27,44),(25,44),(23,44)))
        self.add_bezier('body-5',(23, 44),*(((21.5422399, 41.80973859), (19.21753356, 40.84111095), (17, 42)),))
        self.add_bezier('body-6',(17, 42),*(((15.5422399, 43.69026141), (13.41315017, 44), (12, 44)),))
        self.add_bezier('body-7',(12, 44),*(((10.33321801, 44), (8.94281517, 43.27396325), (8, 42)),))
        self.add_line('body-8',(8, 42),(8, 25))
        self.add_bezier('comb-1',(10, 16),*(((8.01485553, 13.57862198), (8, 9.53600957), (9, 7)),))
        self.add_bezier('comb-2',(9, 7),*(((9.45820393, 6.05572809), (10.56966011, 5.5), (11.75, 5.5)), ((12.93033989, 5.5), (14.05572809, 6.05572809), (15, 7))))
        self.add_bezier('comb-3',(15, 7),*(((15.0, 5.34314575), (16.790861, 4), (19.0, 4)), ((21.209139, 4), (23.0, 5.34314575), (23, 7))))
        self.add_bezier('comb-4',(23, 7),*(((23.94427191, 6.05572809), (25.42621348, 5.5), (27.0, 5.5)), ((28.57378652, 5.5), (30.05572809, 6.05572809), (31, 7))))
        self.add_bezier('comb-5',(31, 7),*(((32.68717387, 10.44231727), (31.01512946, 15.45845051), (27, 18)),))
        self.add_line('beak-1',(29,24),(40,27))
        self.add_line('beak-2',(40,27),(29,34))
        self.add_arc('wattle-1',(29,34),(39,39),radius_x=10,radius_y=5)
        self.add_arc('wattle-2',(39,39),(29,44),radius_x=10,radius_y=5)
        self.add_line('eye',(20, 26),(20, 26))
        self.add_contour('body',*('body-1', 'body-2', 'body-3-1', 'body-3-2', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8'),closed=True)
        self.add_contour('comb',*('comb-1', 'comb-2', 'comb-3', 'comb-4', 'comb-5'),closed=False)
        self.add_contour('beak',*('beak-1', 'beak-2'),closed=False)
        self.add_contour('wattle',*('wattle-1', 'wattle-2'),closed=False)
        self.relate('connect',*('body', 'comb'))
        self.relate('connect',*('body', 'beak'))
        self.relate('connect',*('body', 'wattle'))
        self.relate('connect',*('beak', 'wattle'))
