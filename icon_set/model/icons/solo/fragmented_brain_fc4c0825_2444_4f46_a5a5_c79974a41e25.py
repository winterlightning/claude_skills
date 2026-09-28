"""fragmented-brain: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc4c0825-2444-4f46-a5a5-c79974a41e25'
SOURCE_PATH = 'pictographic-primitives/symbol/fragmented brain_fc4c0825-2444-4f46-a5a5-c79974a41e25.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class FragmentedBrain(Solo48):
    icon_id = 'fragmented-brain'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('fragmented', 'brain', 'symbol')

    def build(self):
        # Plan: HRECT_L; coherent oblique outline and shared facet intersections replace jagged perimeter fragments.
        # Reference: Human reference vocabulary inspected; supplied symbol is an abstract fragmented form, not an anatomical brain silhouette.
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

        # Preserve the supplied oblique fragmented silhouette, but keep facets coherent.
        path('outline',(8,20),[('C',(12,12),(22,8),(30,8)),('C',(34,8),(35,9),(38,12)),('C',(41,15),(44,14),(44,18)),
         ('C',(44,22),(40,25),(36,27)),('L',(12,39)),('C',(10,40),(9,40),(8,40)),('C',(5,40),(4,38),(4,34)),('C',(4,29),(5,25),(8,20))],True)
        self.add_polyline('facet-cross',(8,20),(26,23),(36,27))
        self.add_polyline('facet-spine',(12,39),(26,23),(38,12))
        self.relate('connect','facet-cross','facet-spine');self.relate('connect','facet-cross','outline');self.relate('connect','facet-spine','outline')
