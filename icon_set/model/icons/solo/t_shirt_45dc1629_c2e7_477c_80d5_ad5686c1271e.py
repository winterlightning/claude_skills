"""t-shirt-45dc1629: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '45dc1629-c2e7-477c-80d5-ad5686c1271e'
SOURCE_PATH = 'pictographic-primitives/clothes/t shirt_45dc1629-c2e7-477c-80d5-ad5686c1271e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class TShirt45dc1629(Solo48):
    icon_id = 't-shirt-45dc1629'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('t', 'shirt', 'clothes')

    def build(self):
        # Plan: HRECT_L; matching shoulder curves, semicircular neck and equal sleeves.
        # Reference: No inspected Lucide shirt match; mirrored garment construction.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        path('shirt',(16,8),[('A',(32,8),8,8,False),('C',(40,8),(44,12),(44,18)),
         ('L',(44,26)),('L',(36,26)),('L',(36,40)),('L',(12,40)),('L',(12,26)),
         ('L',(4,26)),('L',(4,18)),('C',(4,12),(8,8),(16,8))],True)
        self.add_line('left-sleeve',(12,26),(12,18));self.add_line('right-sleeve',(36,26),(36,18))
        for side in ['left','right']:self.relate('connect',side+'-sleeve','shirt')
