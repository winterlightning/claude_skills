"""organic-tree: smooth geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20ca0045-a5f1-5d77-8e5b-2bce89d1e61d'
SOURCE_PATH = 'pictographic-primitives/ecology/organic tree_20ca0045-a5f1-5d77-8e5b-2bce89d1e61d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class OrganicTree(Solo48):
    icon_id = 'organic-tree'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecology'
    categories = ('primitives', 'ecology')
    aliases = ()
    keywords = ('organic', 'tree', 'ecology')

    def build(self):
        # Plan: VRECT_L; mirrored tree crown with smooth shoulders and a centered trunk.
        # Reference: No close Lucide tree match; preserve the original crown and branch structure.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L': self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C': self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A': self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)

        path('crown',(24,4),[('C',(30,4),(34,8),(34,14)),('L',(34,16)),
         ('C',(38,18),(40,21),(40,25)),('C',(40,31),(34,34),(24,34)),
         ('C',(14,34),(8,31),(8,25)),('C',(8,21),(10,18),(14,16)),('L',(14,14)),('C',(14,8),(18,4),(24,4))],True)
        self.add_polyline('trunk',(24,16),(24,24),(24,34),(24,44));self.relate('connect','trunk','crown')
        self.add_line('base',(18,44),(30,44));self.relate('connect','base','trunk')
