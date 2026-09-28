"""fire-5ae1316a: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ae1316a-475c-4f56-8965-7568f85bd529'
SOURCE_PATH = 'pictographic-primitives/weather/fire_5ae1316a-475c-4f56-8965-7568f85bd529.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Fire5ae1316a(Solo48):
    icon_id = 'fire-5ae1316a'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    categories = ('weather', 'primitives')
    aliases = ()
    keywords = ('fire', 'weather')

    def build(self):
        # Plan: VRECT_L; one flowing asymmetric flame tip over a smooth balanced bowl.
        # Reference: No useful simple-flame Lucide match; preserve the original leaning flame silhouette.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        # Deliberately asymmetric flame tip; continuous curve through both side extremes.
        path('flame',(22,4),[('C',(23,15),(40,18),(40,29)),('C',(40,38),(33,44),(24,44)),
         ('C',(15,44),(8,38),(8,29)),('C',(8,18),(20,17),(22,4))],True)
