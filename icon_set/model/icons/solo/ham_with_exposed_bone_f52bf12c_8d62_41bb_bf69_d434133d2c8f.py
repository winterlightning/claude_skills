'Meat on the Bone.\n\nSymbol plan: Ham with a broad rounded meat portion and exposed bone rendered as short shaft and rounded fork to preserve clear silhouette.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f52bf12c-8d62-41bb-bf69-d434133d2c8f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/flesh_f52bf12c-8d62-41bb-bf69-d434133d2c8f.svg'
AUTHOR = 'gpt-6'

class HamWithExposedBone(Solo48):
    icon_id = 'ham-with-exposed-bone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('ham', 'with', 'exposed', 'bone')

    def build(self):
        # Ham with a broad rounded meat portion and exposed bone rendered as short shaft and rounded fork to preserve clear silhouette.
        axis_x = 24
        p_6_11 = (6, 11)
        p_6_19 = (6, 19)
        p_6_28 = (6, 28)
        p_11_6 = (11, 6)
        p_11_33 = (11, 33)
        p_19_6 = (19, 6)
        p_19_33 = (19, 33)
        p_27_33 = (27, 33)
        p_28_6 = (28, 6)
        p_29_29 = (29, 29)
        p_33_12 = (33, 12)
        p_33_20 = (33, 20)
        p_33_29 = (33, 29)
        p_35_42 = (35, 42)
        p_36_38 = (36, 38)
        p_38_36 = (38, 36)
        p_39_39 = (39, 39)
        p_42_35 = (42, 35)
        self.add_bezier('ham-1', p_6_19, (p_6_11, p_11_6, p_19_6))
        self.add_bezier('ham-2', p_19_6, (p_28_6, p_33_12, p_33_20))
        self.add_bezier('ham-3', p_33_20, (p_33_29, p_27_33, p_19_33))
        self.add_bezier('ham-4', p_19_33, (p_11_33, p_6_28, p_6_19))
        self.add_contour('ham', 'ham-1', 'ham-2', 'ham-3', 'ham-4', closed=True)
        self.add_line('bone-shaft-1', p_29_29, p_39_39)
        self.add_contour('bone-shaft', 'bone-shaft-1', closed=False)
        self.relate("connect", 'ham', 'bone-shaft')
        self.add_bezier('bone-end-1', p_35_42, (p_36_38, p_38_36, p_42_35))
        self.add_contour('bone-end', 'bone-end-1', closed=False)
        self.relate("connect", 'bone-shaft', 'bone-end')
