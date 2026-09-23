"""Crossed Adhesive Bandages."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bae2081c-f794-5ea3-918b-d77e9a27de24'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/bandage_bae2081c-f794-5ea3-918b-d77e9a27de24.svg'
AUTHOR = 'gpt-6'


class CrossedAdhesiveBandages(Solo48):
    icon_id = 'crossed-adhesive-bandages'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('crossed', 'adhesive', 'bandages')

    def build(self):
        # Plan: two matching diagonal capsules; front strip occludes the rear.
        # SQUARE extrema (6,6)-(42,42). Shared cap construction is reflected
        # about x=24 for the rear ends. Lucide bandage: round ends, sparse pad.
        def cap(prefix, mirror=False, lower=False):
            def point(p):
                x, y = p
                if lower:
                    x, y = 48-x, 48-y
                if mirror:
                    x = 48-x
                return x, y
            start = (28,8)
            segments = [((30,6),(32,6),(34,6)),
                        ((38,6),(42,10),(42,14)),
                        ((42,16),(42,18),(40,20))]
            self.add_bezier(prefix, point(start),
                            *((point(a),point(b),point(c)) for a,b,c in segments))
        cap('front-top')
        for i, (a,b) in enumerate(zip([(40,20),(36,24),(24,36)], [(36,24),(24,36),(20,40)]), 1):
            self.add_line(f'front-right-{i}',a,b)
        cap('front-bottom',lower=True)
        for i, (a,b) in enumerate(zip([(8,28),(12,24),(24,12)], [(12,24),(24,12),(28,8)]), 1):
            self.add_line(f'front-left-{i}',a,b)
        self.add_contour('front','front-top','front-right-1','front-right-2',
                         'front-right-3','front-bottom','front-left-1',
                         'front-left-2','front-left-3',closed=True)
        cap('back-top',mirror=True)
        self.add_line('back-top-left',(8,20),(12,24))
        self.add_line('back-top-right',(24,12),(20,8))
        self.add_contour('back-upper','back-top-right','back-top','back-top-left')
        cap('back-bottom',mirror=True,lower=True)
        self.add_line('back-bottom-right',(40,28),(36,24))
        self.add_line('back-bottom-left',(24,36),(28,40))
        self.add_contour('back-lower','back-bottom-left','back-bottom','back-bottom-right')
        for rear in ('back-upper','back-lower'):
            self.relate('connect','front',rear)
        self.add_dot('pad-perforation',(24,24))
