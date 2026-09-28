"""A five-lobed flower with an upright stem. VRECT extremes (8,4)-(40,44).
Reduction: Removed the centre ring so five broad petal lobes remain clear. Opened the leaf interiors.
Lucide construction: flower-2, leaf
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a838d4d1-5686-50bb-ab98-47d224dd2824'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__five-petal-flower-with-leaves/20260927T032256Z-thuan-mac-1/reference/lilac_2b341bc8-cb9a-4490-9129-7339b9080d7e.svg'
AUTHOR = "gpt-6"


class FivePetalFlowerWithLeaves(Solo48):
    icon_id = 'five-petal-flower-with-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    categories = ("nature", "primitives")
    aliases = ()
    keywords = ('flower', 'daisy', 'petals', 'bloom', 'stem', 'leaves', 'garden', 'nature')

    def build(self) -> None:
        # Five rounded lobes share five recessed valleys; mirrored leaves frame the stem.
        petals = [
            ('top',(19,10),((19,2),(29,2),(29,10))),
            ('upper-right',(29,10),((39,8),(39,16),(32,17))),
            ('lower-right',(32,17),((39,23),(34,29),(24,22))),
            ('lower-left',(24,22),((14,29),(9,23),(16,17))),
            ('upper-left',(16,17),((9,16),(9,8),(19,10))),
        ]
        for name,start,controls in petals:
            self.add_bezier(name,start,controls)
        self.add_contour('flower',*(p[0] for p in petals),closed=True)
        self.add_line('stem',(24,22),(24,44))
        self.relate('connect','stem','flower')
        self.add_arc('leaf-left',(8,35),(24,44),radius_x=16,radius_y=9)
        self.add_arc('leaf-right',(24,44),(40,35),radius_x=16,radius_y=9)
        self.relate('connect','stem','leaf-left')
        self.relate('connect','stem','leaf-right')

SOURCE_REFERENCES = (('2b341bc8-cb9a-4490-9129-7339b9080d7e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/lilac_2b341bc8-cb9a-4490-9129-7339b9080d7e.svg'),)
