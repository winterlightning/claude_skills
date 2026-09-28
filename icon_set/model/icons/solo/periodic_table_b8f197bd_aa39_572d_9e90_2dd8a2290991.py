"""periodic-table: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8f197bd-aa39-572d-9e90-2dd8a2290991'
SOURCE_PATH = 'pictographic-primitives/science/periodic table_b8f197bd-aa39-572d-9e90-2dd8a2290991.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PeriodicTable(Solo48):
    icon_id = 'periodic-table'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    categories = ('science', 'primitives')
    aliases = ()
    keywords = ('periodic', 'table', 'science')

    def build(self):
        # Plan: HRECT_L; a shared cell grid owns both towers, rows and exact column junctions; irregular top cap and rounded detours removed.
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

        self.add_polyline('table',(4,8),(14,8),(14,20),(34,20),(34,8),(44,8),(44,20),(44,30),(44,40),(34,40),(14,40),(4,40),(4,30),(4,20),closed=True)
        self.add_polyline('row',(4,30),(14,30),(34,30),(44,30))
        for side,x in [('left',14),('right',34)]:
         self.add_polyline(side+'-column',(x,20),(x,30),(x,40));self.relate('connect',side+'-column','row');self.relate('connect',side+'-column','table')
        self.add_line('left-cell',(4,20),(14,20));self.add_line('right-cell',(34,20),(44,20))
        for part in ['row','left-cell','right-cell']:self.relate('connect',part,'table')
