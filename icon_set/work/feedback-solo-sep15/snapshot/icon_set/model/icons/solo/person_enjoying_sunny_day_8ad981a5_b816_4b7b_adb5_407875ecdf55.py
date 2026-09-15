"""A person opens their arms beneath a small cloud and sun. SQUARE centerline extremes (6,6)-(42,42). Human construction follows human_ref/user.svg and full_body_ref.png: circular head radius 4, bottom y=27; shoulder top y=35 gives exactly 4 units of painted clearance.
Reduction: Reduced sun rays to four attached cardinal rays and the cloud to three compact lobes.
Lucide: sun, cloud
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ad981a5-b816-4b7b-adb5-407875ecdf55'
SOURCE_PATH = 'pictographic-primitives/nature/virtual environment day_8ad981a5-b816-4b7b-adb5-407875ecdf55.svg'
AUTHOR = 'gpt-6'

class PersonEnjoyingSunnyDay(Solo48):
    icon_id = 'person-enjoying-sunny-day'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-04"
    aliases = ()
    keywords = ('person', 'sun', 'cloud', 'day', 'weather', 'outdoors', 'environment', 'relax')

    def build(self) -> None:
        # Shared human references: icon_set/references/human_ref/user.svg and full_body_ref.png.
        a=24;cy=23;r=4;body_top=cy+r+8
        self.add_arc('head-right',(a,cy-r),(a,cy+r),radius_x=r)
        self.add_arc('head-left',(a,cy+r),(a,cy-r),radius_x=r)
        self.add_contour('head','head-right','head-left',closed=True)
        self.add_arc('shoulder-left',(12,42),(a,body_top),radius_x=12,radius_y=7)
        self.add_arc('shoulder-right',(a,body_top),(36,42),radius_x=12,radius_y=7)
        self.add_contour('shoulders','shoulder-left','shoulder-right')
        for side in (-1,1): self.add_line(f'arm-{side}',(a+side*12,29),(a+side*18,29))
        # Three lobes form one cloud, with no inner marks.
        self.add_arc('cloud-top',(9,9),(13,9),radius_x=2,radius_y=3)
        self.add_arc('cloud-right',(13,9),(13,15),radius_x=3)
        self.add_line('cloud-base',(13,15),(9,15))
        self.add_arc('cloud-left',(9,15),(9,9),radius_x=3)
        self.add_contour('cloud','cloud-top','cloud-right','cloud-base','cloud-left',closed=True)
        x,y,r=36,12,3
        pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y)]
        for j in range(4):self.add_arc(f'sun-{j}',pts[j],pts[(j+1)%4],radius_x=r)
        self.add_contour('sun',*[f'sun-{j}' for j in range(4)],closed=True)
        for j,(dx,dy) in enumerate(((0,-1),(1,0),(0,1),(-1,0))):
         self.add_line(f'ray-{j}',pts[j],(x+dx*6,y+dy*6))
         for k in (j,(j-1)%4):self.relate('connect',f'ray-{j}',f'sun-{k}')
