"""Hand Taking Pill From Blister Pack.

Symbol plan: Blister card has two pill circles and open pressing corner; hand reaches up beneath. Extrema (6,6)-(42,42).
Construction reference: Shared human reference and Lucide hand-grab: one readable pressing finger.
Reduction: Reduced six pockets to two pills and pressing pocket to retain legibility.
Keyshape centerline extremes follow the SOLO48 contract; stroke 4, integer grid.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0f507713-b747-5098-b67a-640fe383c7e2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-taking-blister-pill/20260927T075452Z-thuan-mac-1/reference/cooking baking tray hand_0f507713-b747-5098-b67a-640fe383c7e2.svg'
AUTHOR = "gpt-6"


class HandTakingBlisterPill(Solo48):
    icon_id = 'hand-taking-blister-pill'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('hand', 'taking', 'blister', 'pill')

    def build(self):
        self.path('pack',(15,30),[(10,30),((6,30),(6,30),(6,26)),(6,10),((6,6),(6,6),(10,6)),(38,6),((42,6),(42,6),(42,10)),(42,20),(40,28)])
        for i,p in enumerate(((17,17),(31,17))):self.loop(f'pill-{i}',*p,3)
        self.path('hand',(17,42),[(17,36),(27,29),((32,29),(36,29),(40,28)),((42,29),(40,33),(36,34)),(27,40),(27,42)])
        self.relate('connect','pack','hand')

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
