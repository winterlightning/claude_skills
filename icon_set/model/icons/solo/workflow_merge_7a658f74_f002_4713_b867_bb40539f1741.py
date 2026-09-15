"""workflow-merge: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a658f74-f002-4713-b867-bb40539f1741'
SOURCE_PATH = 'pictographic-primitives/diagrams/workflow merge_7a658f74-f002-4713-b867-bb40539f1741.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class WorkflowMerge(Solo48):
    icon_id = 'workflow-merge'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('workflow', 'merge', 'diagrams')

    def build(self):
        # Plan: VRECT_L; three equal circular nodes with connector ends precisely at circle extremes; no one-unit pseudo-arc.
        # Reference: Lucide git-compare-arrows: exact node-boundary contacts.
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

        for name,cx,cy in [('top',13,9),('bottom',13,39),('branch',35,26)]:oval(name,cx,cy,5)
        self.add_polyline('stem',(13,14),(13,26),(13,34));self.add_line('branch-rail',(13,26),(30,26))
        self.relate('connect','stem','top');self.relate('connect','stem','bottom');self.relate('connect','branch-rail','stem');self.relate('connect','branch-rail','branch')
