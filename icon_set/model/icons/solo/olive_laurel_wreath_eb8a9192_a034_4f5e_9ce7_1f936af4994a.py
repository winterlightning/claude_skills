"""A mirrored open olive wreath with two curved branches and five leaf strokes per side. Fine foliage reduced to readable paired sprays.

Construction: No useful Lucide subject match found.
Keyshape SQUARE; centerline extremes are the visible bounds inset by 2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb8a9192-a034-4f5e-9ce7-1f936af4994a'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/olive wreath_eb8a9192-a034-4f5e-9ce7-1f936af4994a.svg'


class OliveLaurelWreath(Solo48):
    icon_id = 'olive-laurel-wreath'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('wreath', 'laurel', 'olive', 'victory', 'greek', 'award', 'olympic', 'honour')

    def build(self) -> None:
        for side, flip in (("left",False),("right",True)):
            def p(x,y):
                return (48-x if flip else x,y)
            self.add_line(side+"-tip", p(18,2), p(14,10))
            self.add_arc(side+"-upper", p(14,10), p(8,28), radius_x=6, radius_y=18, sweep=flip)
            self.add_arc(side+"-lower", p(8,28), p(12,38), radius_x=16, radius_y=18, sweep=flip)
            self.add_arc(side+"-foot", p(12,38), p(24,46), radius_x=16, radius_y=18, sweep=flip)
            self.add_contour(side, side+"-tip", side+"-upper", side+"-lower", side+"-foot")
            for name,a,b in (("top-leaf",(14,10),(20,8)),("outer-high",(8,28),(2,18)),("inner-high",(8,28),(16,22)),("outer-low",(12,38),(2,34)),("inner-low",(12,38),(18,32))):
                self.add_line(side+"-"+name,p(*a),p(*b))
                self.relate("connect",side,side+"-"+name)
            self.relate("connect",side+"-outer-high",side+"-inner-high")
            self.relate("connect",side+"-outer-low",side+"-inner-low")
        self.relate("connect","left","right")
