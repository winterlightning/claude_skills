"""graph-finance: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5552619f-de1f-40a4-b0e9-95549bca7398'
SOURCE_PATH = 'pictographic-primitives/finance/graph_5552619f-de1f-40a4-b0e9-95549bca7398.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class GraphFinance(Solo48):
    icon_id = 'graph-finance'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    categories = ('primitives', 'finance')
    aliases = ()
    keywords = ('graph', 'finance')

    def build(self):
        # Plan: HRECT_L; three bars with exact baseline nodes; removed duplicate foot segment.
        # Reference: No close Lucide match; reconstruct the supplied subject from its owning geometry.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L':self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C':self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A':self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry=None):
            ry=rx if ry is None else ry
            path(name,(cx-rx,cy),[('A',(cx,cy-ry),rx,ry,True),('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)

        self.add_polyline('baseline',(4,40),(10,40),(24,40),(38,40),(44,40))
        for i,x,top in [(0,10,8),(1,24,17),(2,38,22)]:
         self.add_line(f'bar-{i}',(x,top),(x,40));self.relate('connect',f'bar-{i}','baseline')
