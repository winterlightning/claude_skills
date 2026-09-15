"""Podcast Microphone beside Laptop.

Symbol plan: Laptop on the left and upright podcast microphone on the right; clear equipment grouping. Remove cable and tripod diagonals.
HRECT_L centerline extremes (4,8)-(44,40); envelope follows the subject's proportions.
Construction reference: Lucide laptop: clean display and lower base; Lucide mic: capsule and stem.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '270a1a6b-80b7-445e-85e4-d5adfa15b5c5'
SOURCE_PATH = 'pictographic-primitives/audio/microphone podcast laptop_270a1a6b-80b7-445e-85e4-d5adfa15b5c5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'podcast-microphone-beside-laptop'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('podcast', 'microphone', 'beside', 'laptop')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def box(n,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if a==b: continue
                if i%2: arc(n+str(i),a,b,r)
                else: line(n+str(i),a,b)
            join(n,*(n+str(i) for i in range(8) if pts[i]!=pts[(i+1)%8]),closed=True)

        box('screen',4,8,22,24,2)
        line('keyboard',(4,40),(26,40))
        line('hinge',(6,32),(4,40))
        connect('screen','hinge'); connect('hinge','keyboard')
        box('microphone',36,16,8,16,4)
        line('stand',(40,32),(40,40))
        line('foot',(35,40),(44,40))
        connect('microphone','stand'); connect('stand','foot')
