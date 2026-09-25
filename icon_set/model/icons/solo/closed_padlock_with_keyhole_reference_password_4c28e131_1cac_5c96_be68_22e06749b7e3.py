"""Closed Padlock with Keyhole.
Plan: Mirrored shackle and rounded body share split top-wall endpoints. Ink (6,2)-(42,46).
Reference construction: lock.
Reduction: Represent the narrow keyhole slot as a single round-ended stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4c28e131-1cac-5c96-be68-22e06749b7e3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/lock password_4c28e131-1cac-5c96-be68-22e06749b7e3.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'closed-padlock-with-keyhole-reference-password'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('closed', 'padlock', 'with', 'keyhole')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        pts=[(12,18),(16,18),(32,18),(36,18)]
        for j,(a,b) in enumerate(zip(pts,pts[1:])):self.add_line(f'top-{j}',a,b)
        self.add_arc('tr',(36,18),(40,22),radius_x=4)
        self.add_line('right',(40,22),(40,40))
        self.add_arc('br',(40,40),(36,44),radius_x=4)
        self.add_line('bottom',(36,44),(12,44))
        self.add_arc('bl',(12,44),(8,40),radius_x=4)
        self.add_line('left',(8,40),(8,22))
        self.add_arc('tl',(8,22),(12,18),radius_x=4)
        self.add_contour('body','top-0','top-1','top-2','tr','right','br','bottom','bl','left','tl',closed=True)
        self.add_line('shackle-left',(16,18),(16,12))
        self.add_arc('shackle-top',(16,12),(32,12),radius_x=8)
        self.add_line('shackle-right',(32,12),(32,18))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','body','shackle')
        circle('keyhole',24,30,3)
        self.add_line('slot',(24,33),(24,35))
        self.relate('connect','keyhole','slot')
