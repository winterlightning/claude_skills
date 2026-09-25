"""Four equal rounded squares form a two-by-two grid. SQUARE extremes (6,6)-(42,42). Lucide grid-2x2 informs consistent corner radii; the source specifies four detached tiles rather than one divided frame. Shared side12, radius2 and pitch24; no tiles omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e611334b-e870-4c6a-94a2-cf370f8dd77f'
SOURCE_PATH = 'pictographic-primitives/symbol/grid of squares_e611334b-e870-4c6a-94a2-cf370f8dd77f.svg'
AUTHOR = 'gpt-6'


class GridFourSquares(Solo48):
    icon_id = 'grid-four-squares'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('grid', 'squares', 'apps', 'dashboard', 'layout', 'menu', 'category', 'tiles')

    def build(self) -> None:
        # One rounded-square definition, four equally spaced instances.
        for row,y in enumerate((6,30)):
            for col,x in enumerate((6,30)):
                n=f'tile-{row}-{col}'
                side,r=12,2
                self.add_line(n+'-top',(x+r,y),(x+side-r,y))
                self.add_arc(n+'-tr',(x+side-r,y),(x+side,y+r),radius_x=r)
                self.add_line(n+'-right',(x+side,y+r),(x+side,y+side-r))
                self.add_arc(n+'-br',(x+side,y+side-r),(x+side-r,y+side),radius_x=r)
                self.add_line(n+'-bottom',(x+side-r,y+side),(x+r,y+side))
                self.add_arc(n+'-bl',(x+r,y+side),(x,y+side-r),radius_x=r)
                self.add_line(n+'-left',(x,y+side-r),(x,y+r))
                self.add_arc(n+'-tl',(x,y+r),(x+r,y),radius_x=r)
                self.add_contour(n,*(n+'-'+a for a in ('top','tr','right','br','bottom','bl','left','tl')),closed=True)
