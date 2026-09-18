"""Independent 32px profile of state32-d06f48d8-bfa8-4a85-98fd-5b92cb3c39ac.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd06f48d8-bfa8-4a85-98fd-5b92cb3c39ac'
SOURCE_PATH = 'icon_set/assets/combination-state32/d06f48d8-bfa8-4a85-98fd-5b92cb3c39ac.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d06f48d8-bfa8-4a85-98fd-5b92cb3c39ac', 'icon_set/assets/combination-state32/d06f48d8-bfa8-4a85-98fd-5b92cb3c39ac.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '081bcde1ecca168b2a47d7eba13a3dd490000a260dd0892b0516b8a91ef65e4d'

class Drawing(Sub32):
    icon_id = 'state32-d06f48d8-bfa8-4a85-98fd-5b92cb3c39ac'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (6, 3), ((6.666666666666667, 2.3333333333333335), (7.666666666666667, 2), (9, 2)))
        self.add_bezier('p1-r1-2', (9, 2), ((10.333333333333334, 2), (11.333333333333334, 2.666666666666667), (12, 4)))
        self.add_bezier('p1-r1-3', (12, 4), ((13.333333333333334, 4.666666666666667), (14.666666666666666, 5), (16, 5)))
        self.add_bezier('p1-r1-4', (16, 5), ((17.333333333333332, 5), (18.666666666666668, 4.666666666666667), (20, 4)))
        self.add_bezier('p1-r1-5', (20, 4), ((21.333333333333332, 2.666666666666667), (23, 2), (25, 2)))
        self.add_bezier('p1-r1-6', (25, 2), ((27, 2), (28.333333333333332, 3.3333333333333335), (29, 6)))
        self.add_bezier('p1-r1-7', (29, 6), ((29.666666666666668, 6.666666666666667), (30, 7.666666666666667), (30, 9)))
        self.add_bezier('p1-r1-8', (30, 9), ((30, 10.333333333333334), (29.333333333333332, 11.666666666666666), (28, 13)))
        self.add_bezier('p1-r1-9', (28, 13), ((27.333333333333332, 14.333333333333334), (27, 15.333333333333334), (27, 16)))
        self.add_bezier('p1-r1-10', (27, 16), ((27, 17.333333333333332), (27.333333333333332, 18.666666666666668), (28, 20)))
        self.add_bezier('p1-r1-11', (28, 20), ((29.333333333333332, 22), (30, 23.666666666666668), (30, 25)))
        self.add_bezier('p1-r1-12', (30, 25), ((30, 27), (28.666666666666668, 28.333333333333332), (26, 29)))
        self.add_bezier('p1-r1-13', (26, 29), ((25.333333333333332, 29.666666666666668), (24.333333333333332, 30), (23, 30)))
        self.add_bezier('p1-r1-14', (23, 30), ((21, 30), (19.333333333333332, 29.333333333333332), (18, 28)))
        self.add_bezier('p1-r1-15', (18, 28), ((16.666666666666668, 27.333333333333332), (15.666666666666666, 27), (15, 27)))
        self.add_bezier('p1-r1-16', (15, 27), ((13.666666666666666, 27), (12, 27.666666666666668), (10, 29)))
        self.add_bezier('p1-r1-17', (10, 29), ((8.666666666666666, 29.666666666666668), (7.666666666666667, 30), (7, 30)))
        self.add_bezier('p1-r1-18', (7, 30), ((4.333333333333334, 30), (3, 28), (3, 24)))
        self.add_bezier('p1-r1-19', (3, 24), ((3.6666666666666665, 22), (4, 20.333333333333332), (4, 19)))
        self.add_bezier('p1-r1-20', (4, 19), ((4, 17), (3.6666666666666665, 15.333333333333334), (3, 14)))
        self.add_bezier('p1-r1-21', (3, 14), ((2.3333333333333335, 12), (2, 10.333333333333334), (2, 9)))
        self.add_bezier('p1-r1-22', (2, 9), ((2, 6.333333333333334), (3.3333333333333335, 4.333333333333333), (6, 3)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', 'p1-r1-13', 'p1-r1-14', 'p1-r1-15', 'p1-r1-16', 'p1-r1-17', 'p1-r1-18', 'p1-r1-19', 'p1-r1-20', 'p1-r1-21', 'p1-r1-22', closed=False)
        self.add_line('p2-r1-1', (10, 21), (16, 14))
        self.add_line('p2-r1-2', (16, 14), (22, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
