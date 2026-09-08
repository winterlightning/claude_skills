from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd29e7ca4-d2c5-4d01-abce-5114e1f6725b'
SOURCE_PATH = 'pictographic-primitives/animals/silk bug_d29e7ca4-d2c5-4d01-abce-5114e1f6725b.svg'
AUTHOR = 'gpt-6'


class DomedBeetle(Solo48):
    icon_id = 'domed-beetle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('beetle', 'bug', 'insect', 'shell', 'antennae', 'legs', 'nature', 'wildlife')

    def build(self) -> None:
        # Square extremes (2,2)-(46,46); paired legs around x=24.
        self.add_arc('crown', (16, 16), (32, 16), radius_x=8, radius_y=8, sweep=True)
        self.add_line('head-base', (32, 16), (16, 16))
        self.add_contour('head', 'crown', 'head-base', closed=True)
        self.add_arc('shoulder-r', (24, 16), (36, 28), radius_x=12, radius_y=12, sweep=True)
        self.add_line('side-r', (36, 28), (36, 34))
        self.add_arc('base-r', (36, 34), (24, 46), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('base-l', (24, 46), (12, 34), radius_x=12, radius_y=12, sweep=True)
        self.add_line('side-l', (12, 34), (12, 28))
        self.add_arc('shoulder-l', (12, 28), (24, 16), radius_x=12, radius_y=12, sweep=True)
        self.add_contour('case', 'shoulder-r', 'side-r', 'base-r', 'base-l', 'side-l', 'shoulder-l', closed=True)
        self.add_line('seam', (24, 16), (24, 46))
        self.add_line('left-antenna-1', (16, 16), (12, 8))
        self.add_line('left-antenna-2', (12, 8), (12, 2))
        self.add_contour('left-antenna', 'left-antenna-1', 'left-antenna-2', closed=False)
        self.add_line('left-foreleg-1', (12, 28), (4, 20))
        self.add_line('left-foreleg-2', (4, 20), (4, 14))
        self.add_contour('left-foreleg', 'left-foreleg-1', 'left-foreleg-2', closed=False)
        self.add_line('left-midleg-1', (12, 28), (2, 28))
        self.add_line('left-midleg-2', (2, 28), (2, 34))
        self.add_contour('left-midleg', 'left-midleg-1', 'left-midleg-2', closed=False)
        self.add_line('left-rearleg-1', (12, 34), (6, 40))
        self.add_line('left-rearleg-2', (6, 40), (6, 46))
        self.add_contour('left-rearleg', 'left-rearleg-1', 'left-rearleg-2', closed=False)
        self.add_line('right-antenna-1', (32, 16), (36, 8))
        self.add_line('right-antenna-2', (36, 8), (36, 2))
        self.add_contour('right-antenna', 'right-antenna-1', 'right-antenna-2', closed=False)
        self.add_line('right-foreleg-1', (36, 28), (44, 20))
        self.add_line('right-foreleg-2', (44, 20), (44, 14))
        self.add_contour('right-foreleg', 'right-foreleg-1', 'right-foreleg-2', closed=False)
        self.add_line('right-midleg-1', (36, 28), (46, 28))
        self.add_line('right-midleg-2', (46, 28), (46, 34))
        self.add_contour('right-midleg', 'right-midleg-1', 'right-midleg-2', closed=False)
        self.add_line('right-rearleg-1', (36, 34), (42, 40))
        self.add_line('right-rearleg-2', (42, 40), (42, 46))
        self.add_contour('right-rearleg', 'right-rearleg-1', 'right-rearleg-2', closed=False)
        self.relate("connect", 'head', 'left-antenna')
        self.relate("connect", 'head', 'right-antenna')
        self.relate("connect", 'case', 'seam')
        self.relate("connect", 'case', 'left-foreleg')
        self.relate("connect", 'case', 'left-midleg')
        self.relate("connect", 'case', 'left-rearleg')
        self.relate("connect", 'case', 'right-foreleg')
        self.relate("connect", 'case', 'right-midleg')
        self.relate("connect", 'case', 'right-rearleg')
        self.relate("connect", 'left-foreleg', 'left-midleg')
        self.relate("connect", 'right-foreleg', 'right-midleg')
