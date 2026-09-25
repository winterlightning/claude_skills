"""Adjustable Plastic Cable Tie.

Plan: Broad locking head above an open strap; repeated divisions have 8-unit pitch. Envelope 10,4–38,44.
Construction reference: cable (local original and atomic-debug inspected).
Simplification: Strap divisions reduced to two evenly spaced ribs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0555f378-857c-402a-91f7-d7c7007787c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/cable zip tie 2_0555f378-857c-402a-91f7-d7c7007787c9.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'straight-cable-tie-strap'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('adjustable', 'plastic', 'cable', 'tie')

    def build(self):
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        def rect(name, left, top, right, bottom, r=2, bottom_nodes=()):
            pts=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for j,a in enumerate(pts):
                b=pts[(j+1)%8]; eid=f'{name}-{j}'
                if j == 4 and bottom_nodes:
                    run=[a]+[(x,bottom) for x in bottom_nodes]+[b]
                    for k,(u,v) in enumerate(zip(run,run[1:])):
                        member=f'{eid}-{k}'; self.add_line(member,u,v); members.append(member)
                    continue
                members.append(eid)
                if j%2: self.add_arc(eid,a,b,radius_x=r)
                else: self.add_line(eid,a,b)
            self.add_contour(name,*members,closed=True)

        rect('locking-head',10,4,38,22,3,bottom_nodes=(30,18))
        self.add_line('slot',(21,13),(27,13))
        self.add_polyline('strap-left',(18,22),(18,30),(18,38),(18,44))
        self.add_polyline('strap-right',(30,22),(30,30),(30,38),(30,44))
        for side in ('strap-left','strap-right'): self.relate('connect','locking-head',side)
        for j,y in enumerate((30,38)):
            self.add_line(f'division-{j}',(18,y),(30,y))
            for side in ('strap-left','strap-right'): self.relate('connect',side,f'division-{j}')
