"""Gas Stove Burner with Flames.

Symbol plan: Three equal flame loops on a 16-unit series; broad rounded burner. Extrema (4,8)-(44,40).
Construction reference: Lucide flame: coherent lobes and pointed tip.
Reduction: Dropped pedestal and baseline to preserve three open flame interiors.
Keyshape centerline extremes follow the SOLO48 contract; stroke 4, integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ea71018-0faa-5fbf-aeb4-02467c816835'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/stove gas_8ea71018-0faa-5fbf-aeb4-02467c816835.svg'
AUTHOR = 'gpt-6'


class ThreeFlameStoveBurner(Solo48):
    icon_id = 'three-flame-stove-burner'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('three', 'flame', 'stove', 'burner')

    def build(self):
        for x in (8,24,40):
            self.add_bezier(f'flame-{x}-right',(x,8),((x,11),(x+4,12),(x+4,16)))
            self.add_arc(f'flame-{x}-base',(x+4,16),(x-4,16),radius_x=4)
            self.add_bezier(f'flame-{x}-left',(x-4,16),((x-4,12),(x,11),(x,8)))
            self.add_contour(f'flame-{x}',f'flame-{x}-right',f'flame-{x}-base',f'flame-{x}-left',closed=True)
        self.path('burner',(8,29),[(40,29),((44,29),(44,29),(44,33)),(44,36),((44,40),(44,40),(40,40)),(8,40),((4,40),(4,40),(4,36)),(4,33),((4,29),(4,29),(8,29))],True)

    def loop(self, name, x, y, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (x-rx,y), (x+rx,y), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (x+rx,y), (x-rx,y), radius_x=rx, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def path(self, name, start, commands, closed=False):
        ids=[]
        point=start
        for i,command in enumerate(commands):
            key=f'{name}-{i}'
            if len(command)==2:
                self.add_line(key, point, command)
                point=command
            else:
                c1,c2,end=command
                self.add_bezier(key, point, (c1,c2,end))
                point=end
            ids.append(key)
        self.add_contour(name, *ids, closed=closed)
