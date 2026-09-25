# Final repair: Use tangent straight leads at node endpoints so exact8-unit separation is analytically certifiable.
'Square-Centered Ring Network\nPlan: Ring network with centered square; four main nodes replace six to preserve spacing.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Reduce six hollow nodes to four hollow nodes; retain ring and central square.\nKeyshape: CIRCLE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14a3a91e-9beb-47ca-9999-bd7a4d5e5429'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon mq_14a3a91e-9beb-47ca-9999-bd7a4d5e5429.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-centered-ring-network'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('square', 'centered', 'ring', 'network')

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
            if name.startswith('ring-'):
                for a,b in zip(members,members[1:]): self.relate('connect',a,b)
            else:
                self.add_contour(name, *members, closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[((x+rx,y),rx,ry,True),((x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r):
            ellipse(name,x,y,r,r)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)

        self.add_polyline('hub',(20,20),(28,20),(28,28),(20,28),closed=True)
        for j in range(4):
            def p(x,y):
                x-=24;y-=24
                for _ in range(j):x,y=-y,x
                return (24+x,24+y)
            x,y=p(24,8);circle(f'node-{j}',x,y,4)
            path(f'ring-{j}',p(28,8),[p(30,8),(p(40,18),10,10,True),p(40,20)])
        for j in range(4):
            self.relate('connect',f'ring-{j}-0',f'node-{j}');self.relate('connect',f'ring-{j}-2',f'node-{(j+1)%4}')
