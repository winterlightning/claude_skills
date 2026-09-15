"""flow: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ade3493-48f5-5b0b-99db-f678a591e277'
SOURCE_PATH = 'pictographic-primitives/diagrams/flow_7ade3493-48f5-5b0b-99db-f678a591e277.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Flow(Solo48):
    icon_id = 'flow'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('flow', 'diagrams')

    def build(self):
        # Plan: HRECT_L; three equal circular nodes, tangent return bend and exact boundary contacts; stray tip and inward hooks removed.
        # Reference: Lucide git-compare-arrows: clean circular nodes and coherent connector runs.
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

        # Three equal nodes and a smooth return path with exact circle contacts.
        for name,cx,cy in [('start',9,13),('top',27,13),('bottom',27,35)]:oval(name,cx,cy,5)
        self.add_line('forward',(14,13),(22,13));self.relate('connect','forward','start');self.relate('connect','forward','top')
        path('return',(32,13),[('C',(39,13),(44,17),(44,24)),('C',(44,31),(39,35),(32,35))])
        self.relate('connect','return','top');self.relate('connect','return','bottom')
        self.add_line('back',(22,35),(8,35));self.add_polyline('arrowhead',(13,30),(8,35),(13,40))
        self.relate('connect','back','bottom');self.relate('connect','back','arrowhead')
