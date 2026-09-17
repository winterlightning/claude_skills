"""Unlocked Padlock with Round Slot — batch 52."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c42fc4b8-335a-5c21-a6d9-b68f9856802c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/lock unlock_c42fc4b8-335a-5c21-a6d9-b68f9856802c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'unlocked-padlock-with-round-slot'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('unlocked', 'padlock', 'with', 'round', 'slot')

    def build(self):
        # Plan: rounded lock body, open arch, circular keyhole and connected short slot.
        # VRECT_L extremes8,4,40,44. Lucide lock-keyhole-open supplies simple body and shackle.
        # Reduce the narrow waisted hole to a round aperture and open slot at native size.
        self.add_line('top-1',(12,18),(14,18));self.add_line('top-2',(14,18),(36,18))
        self.add_arc('tr',(36,18),(40,22),radius_x=4)
        self.add_line('right',(40,22),(40,40))
        self.add_arc('br',(40,40),(36,44),radius_x=4)
        self.add_line('bottom',(36,44),(12,44))
        self.add_arc('bl',(12,44),(8,40),radius_x=4)
        self.add_line('left',(8,40),(8,22))
        self.add_arc('tl',(8,22),(12,18),radius_x=4)
        self.add_contour('body','top-1','top-2','tr','right','br','bottom','bl','left','tl',closed=True)
        self.add_line('shackle-left',(14,18),(14,14))
        self.add_arc('shackle-top',(14,14),(24,4),radius_x=10)
        self.add_arc('shackle-end',(24,4),(32,8),radius_x=10)
        self.add_contour('shackle','shackle-left','shackle-top','shackle-end');self.relate('connect','shackle','body')
        self.circle('hole',24,31,3)
        self.add_line('slot',(24,34),(24,35));self.relate('connect','slot','hole')


    def circle(self,n,x,y,r):
        pts=[(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for j in range(4):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%4],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(4)],closed=True)

