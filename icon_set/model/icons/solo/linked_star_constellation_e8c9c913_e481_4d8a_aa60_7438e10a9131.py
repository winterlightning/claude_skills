# Final repair: Restore five circular stars with exact endpoint-attached links; remove detached decorative sparkles.
'Linked-Star Constellation\nPlan: Five point stars form a connected irregular astronomical graph; one detached sparkle.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Filled point stars replace tiny hollow rings; one detached sparkle remains.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8c9c913-e481-4d8a-aa60-7438e10a9131'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/astrology constellation_e8c9c913-e481-4d8a-aa60-7438e10a9131.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'linked-star-constellation'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('linked', 'star', 'constellation')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[((x+rx,y),rx,ry,True),((x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r):
            ellipse(name,x,y,r,r)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)

        nodes=[(9,31),(23,19),(35,9),(39,31),(25,39)]
        for j,(x,y) in enumerate(nodes):circle(f'star-{j}',x,y,3)
        links=[((12,31),(20,19),0,1),((26,19),(35,12),1,2),((23,22),(25,36),1,4),((28,39),(36,31),4,3),((36,31),(38,9),3,2)]
        for j,(a,b,s,t) in enumerate(links):
            self.add_line(f'link-{j}',a,b)
            self.relate('connect',f'link-{j}',f'star-{s}');self.relate('connect',f'link-{j}',f'star-{t}')

        self.relate('connect','link-3','link-4')
