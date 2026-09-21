# Final repair: Restore waffle grid with four intersecting grooves set safely inside circle.
'Round Waffle with Square Grid\nPlan: Circular waffle with orthogonal wide grid; ends meet split circle at cardinal nodes.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Reduce dense grid to four broad waffle cells, retaining circular edge.\nKeyshape: CIRCLE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '990104d5-be37-45c2-91c8-e084ab7d5e38'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stroopwafel_990104d5-be37-45c2-91c8-e084ab7d5e38.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-waffle-with-square-grid'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('round', 'waffle', 'with', 'square', 'grid')

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

        circle('waffle',24,24,20)
        for v in (19,29):
            self.add_line(f'h-{v}',(16,v),(32,v))
            self.add_line(f'v-{v}',(v,16),(v,32))
        for x in (19,29):
            for y in (19,29):self.relate('connect',f'h-{x}',f'v-{y}')
