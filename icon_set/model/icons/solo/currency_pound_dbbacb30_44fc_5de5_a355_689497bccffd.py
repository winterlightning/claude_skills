"""currency-pound: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dbbacb30-44fc-5de5-a355-689497bccffd'
SOURCE_PATH = 'pictographic-primitives/money/currency pound_dbbacb30-44fc-5de5-a355-689497bccffd.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class CurrencyPound(Solo48):
    icon_id = 'currency-pound'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    aliases = ()
    keywords = ('currency', 'pound', 'money')

    def build(self):
        # Plan: VRECT_L; smooth pound bowl and flowing foot replace the faceted upper hook.
        # Reference: No close Lucide pound match; coherent typographic stem and bowl.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        path('pound',(8,44),[('C',(17,44),(18,37),(18,30)),('L',(18,24)),('L',(18,16)),
         ('C',(18,8),(21,4),(29,4)),('C',(35,4),(40,6),(40,10))])
        self.add_line('base',(8,44),(40,44));self.relate('connect','base','pound')
        self.add_polyline('bar',(8,24),(18,24),(30,24));self.relate('connect','bar','pound')
