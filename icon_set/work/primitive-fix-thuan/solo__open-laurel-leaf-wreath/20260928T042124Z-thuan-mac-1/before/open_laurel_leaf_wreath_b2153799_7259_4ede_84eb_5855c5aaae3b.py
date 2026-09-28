"""Open laurel wreath with two pointed leaves per side.
SQUARE envelope. Mirrored leaves follow connected stems, keeping an open crown.
Source supplies detached pointed leaves; no local Lucide wreath match.
Reduced from eight to four broad leaves; connected stems retain wreath recognition.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "b2153799-7259-4ede-84eb-5855c5aaae3b"
SOURCE_PATH = "pictographic-primitives/_uncategorized_29/olive wreath 1_b2153799-7259-4ede-84eb-5855c5aaae3b.svg"
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = "open-laurel-leaf-wreath"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "rewards"
    categories = ("rewards", "primitive", "primitives")
    aliases = ("Victory Laurel Wreath",)
    keywords = ("laurel", "wreath", "leaves", "victory", "foliage", "award")
    def build(self):
        # Two broad leaves per side preserve open leaf holes at native size.
        leaves=[((16,6),(6,20),(6,6),(6,12),(16,20),(20,12)),
                ((6,30),(19,42),(6,38),(13,42),(19,34),(12,30))]
        for side in range(2):
            mirror=lambda p:(48-p[0],p[1]) if side else p
            for j,points in enumerate(leaves):
                a,b,c,d,e,f=map(mirror,points);name=f'leaf-{side}-{j}'
                self.add_bezier(name+'-outer',a,(c,d,b))
                self.add_bezier(name+'-inner',b,(e,f,a))
                self.add_contour(name,name+'-outer',name+'-inner',closed=True)
        for side in range(2):
            x=42 if side else 6
            self.add_line(f'stem-{side}',(x,20),(x,30))
            self.relate('connect',f'stem-{side}',f'leaf-{side}-0-outer',f'leaf-{side}-0-inner',f'leaf-{side}-1-outer',f'leaf-{side}-1-inner')
        self.add_line('base',(19,42),(29,42))
        self.relate('connect','base','leaf-0-1-outer','leaf-0-1-inner','leaf-1-1-outer','leaf-1-1-inner')
