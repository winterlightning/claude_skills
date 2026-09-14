"""A broad alien head has a rounded crown and cheeks tapering to a soft pointed chin. Two large almond-shaped eyes slope upward toward the sides, leaving the lower face unmarked.

HRECT_XL visible extremes (2,6)-(46,42); broad dome, mirrored eyes and tapered jaw. No useful Lucide alien match. No facial embellishment.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3111e4ee-f8d7-5adc-8f71-0cc4e4063457'
SOURCE_PATH = 'pictographic-primitives/science/alien_3111e4ee-f8d7-5adc-8f71-0cc4e4063457.svg'
AUTHOR = 'gpt-6'

class AlienHeadSlantedEyes(Solo48):
    icon_id = 'alien-head-slanted-eyes'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ()
    keywords = ('alien', 'head', 'face', 'extraterrestrial', 'eyes', 'space')

    def circle(self, name, x, y, r):
        points = [(x-r,y), (x,y-r), (x+r,y), (x,y+r)]
        for i, start in enumerate(points):
            self.add_arc(f'{name}-{i}', start, points[(i+1)%4], radius_x=r)
        self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)

    def build(self):
        self.add_arc('crown', (4,22), (44,22), radius_x=20, radius_y=14)
        self.add_arc('jaw-right', (44,22), (24,40), radius_x=22)
        self.add_arc('jaw-left', (24,40), (4,22), radius_x=22)
        self.add_contour('head','crown','jaw-right','jaw-left',closed=True)
        for side in (-1,1):
            a=(24+side*10,20); b=(24+side*5,26)
            self.add_arc(f'eye-{side}-a',a,b,radius_x=4,sweep=side==1)
            self.add_arc(f'eye-{side}-b',b,a,radius_x=4,sweep=side==1)
            self.add_contour(f'eye-{side}',f'eye-{side}-a',f'eye-{side}-b',closed=True)
