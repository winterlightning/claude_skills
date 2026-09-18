"""Mirrored tiered fir silhouette with central trunk; tiers derived from shared x axis.
Keyshape VRECT_L: exact SOLO48 centerline envelope, chosen for subject proportions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3b062822-fdff-4272-a7a0-62ab026cce05'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fir_3b062822-fdff-4272-a7a0-62ab026cce05.svg'
AUTHOR = 'gpt-6'
class Batch045Icon7(Solo48):
    icon_id = 'tiered-fir-tree-batch-045'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('tree', 'fir', 'evergreen', 'pine', 'forest', 'branches', 'nature')
    # Reference: trees: mirrored tier silhouette and central trunk.
    # Reduction: Three branch tiers reduced to two.
    # Bounds: (6, 2, 42, 46)
    def build(self):
        def path(name, start, *steps, closed=False):
            members=[]; p=start
            for i,step in enumerate(steps):
                q=step[1]
                if p == q: continue
                member=f"{name}-{i}"
                if step[0]=='L': self.add_line(member,p,q)
                else: self.add_arc(member,p,q,radius_x=step[2],radius_y=step[3],sweep=step[4])
                members.append(member); p=q
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

        axis=24
        side=[(axis,4),(axis+16,20),(axis+4,20),(axis+16,34),(axis,34)]
        pts=side+[(2*axis-x,y) for x,y in reversed(side[1:-1])]
        self.add_polyline('crown',*pts,closed=True)
        self.add_line('trunk',(axis,34),(axis,44)); self.relate('connect','crown','trunk')
