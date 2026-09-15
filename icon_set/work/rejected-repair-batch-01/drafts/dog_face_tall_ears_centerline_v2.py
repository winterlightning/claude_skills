"""Smooth the two inner ear edges into the forehead while preserving tall pointed ears, and use a lower rounded nose mark for a more canine face.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/dog_face_tall_ears.py'
AUTHOR = 'gpt-6'

class DogFaceTallEars(Solo48):
    icon_id = 'dog-face-tall-ears-centerline-v2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/mammals'
    aliases = ('dog face', 'upright-ear dog')
    keywords = ('dog', 'canine', 'pet', 'face', 'tall ears', 'lucide')

    def build(self) -> None:
        p_8_28 = (8, 28)
        p_8_4 = (8, 4)
        p_19_18 = (19, 18)
        p_29_18 = (29, 18)
        p_40_4 = (40, 4)
        p_40_28 = (40, 28)
        p_25_44 = (25, 44)
        p_23_44 = (23, 44)
        p_17_26 = (17, 26)
        p_31_26 = (31, 26)
        p_21_33 = (21, 33)
        p_24_35 = (24, 35)
        p_27_33 = (27, 33)
        self.add_line('left-ear-outer', p_8_28, p_8_4)
        self.add_bezier('left-ear-inner', p_8_4, ((11, 11), (15, 17), p_19_18))
        self.add_line('forehead', p_19_18, p_29_18)
        self.add_bezier('right-ear-inner', p_29_18, ((33, 17), (37, 11), p_40_4))
        self.add_line('right-ear-outer', p_40_4, p_40_28)
        self.add_arc('right-jaw', p_40_28, p_25_44, radius_x=15, radius_y=16, sweep=True, large_arc=False)
        self.add_line('chin', p_25_44, p_23_44)
        self.add_arc('left-jaw', p_23_44, p_8_28, radius_x=15, radius_y=16, sweep=True, large_arc=False)
        self.add_line('left-eye', p_17_26, p_17_26)
        self.add_line('right-eye', p_31_26, p_31_26)
        self.add_line('nose-1', p_21_33, p_24_35)
        self.add_line('nose-2', p_24_35, p_27_33)
        self.add_contour('head', 'left-ear-outer', 'left-ear-inner', 'forehead', 'right-ear-inner', 'right-ear-outer', 'right-jaw', 'chin', 'left-jaw', closed=True)
        self.add_contour('nose', 'nose-1', 'nose-2', closed=False)
    variant_of = 'dog-face-tall-ears'
    variant_label = 'Batch 01 centerline repair'
