"""Four App Tiles.

Plan: SQUARE centerlines (6,6)-(42,42); one rounded-square definition repeated in a 2x2 grid, radius 3 and step 23.
Construction references: Lucide layout-grid: shared quarter-circle corners and regular spacing.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d51a80c-eeda-5cd7-bab1-87340159d03a'
SOURCE_PATH = 'pictographic-primitives/apps/app window four_7d51a80c-eeda-5cd7-bab1-87340159d03a.svg'
SOURCE_ICON_IDS = ('7d51a80c-eeda-5cd7-bab1-87340159d03a',)
SOURCE_PATHS = ('pictographic-primitives/apps/app window four_7d51a80c-eeda-5cd7-bab1-87340159d03a.svg',)
AUTHOR = 'gpt-6'


class FourAppTiles(Solo48):
    icon_id = 'four-app-tiles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'apps'
    aliases = ()
    keywords = ('four', 'app', 'tiles')

    def build(self) -> None:
        size, radius, step = 13, 3, 23
        for row in range(2):
            for column in range(2):
                x, y = 6 + column * step, 6 + row * step
                k = f"tile-{row}-{column}"
                nodes = [(x+radius,y),(x+size-radius,y),(x+size,y+radius),(x+size,y+size-radius),(x+size-radius,y+size),(x+radius,y+size),(x,y+size-radius),(x,y+radius)]
                members=[]
                for i, start in enumerate(nodes):
                    end=nodes[(i+1)%8]; name=f"{k}-{i}"; members.append(name)
                    if i%2: self.add_arc(name,start,end,radius_x=radius)
                    else: self.add_line(name,start,end)
                self.add_contour(k,*members,closed=True)
