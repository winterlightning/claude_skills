"""weather-cloud: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '361882de-5b14-5b65-b55b-5cd35ffd633c'
SOURCE_PATH = 'pictographic-primitives/weather/weather cloud_361882de-5b14-5b65-b55b-5cd35ffd633c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class WeatherCloud(Solo48):
    icon_id = 'weather-cloud'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    categories = ('weather', 'primitives')
    aliases = ()
    keywords = ('weather', 'cloud')

    def build(self):
        # Plan: HRECT_L; smooth crown, matching shoulders and tangent base replace lumpy cloud joins.
        # Reference: Lucide cloud: continuous cloud silhouette.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        path('cloud',(14,40),[('A',(4,30),10,10,True),('A',(14,20),10,10,True),
         ('C',(14,13),(18,8),(24,8)),('C',(30,8),(34,13),(34,20)),
         ('A',(44,30),10,10,True),('A',(34,40),10,10,True),('L',(14,40))],True)
