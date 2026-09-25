'Upright Sidewalk Slab on Ground Line\nPlan: Upright paving slab with rounded upper corners, lower horizontal seam, and ground.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Use actual saved brief and reference; preserve slab rather than stale top-hat concept.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd3612e6-972a-48c9-b3ed-3d396f381c9a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/sidewalk_cd3612e6-972a-48c9-b3ed-3d396f381c9a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-sidewalk-slab-on-ground-line'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    keywords = ('upright', 'sidewalk', 'slab', 'on', 'ground', 'line')

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

        path('slab',(12,44),[(12,10),((18,4),6,6,True),(30,4),((36,10),6,6,True),(36,44)])
        self.add_line('joint',(12,30),(36,30));self.relate('connect','joint','slab')
        self.add_line('ground',(8,44),(40,44));self.relate('connect','ground','slab')
