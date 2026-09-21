'Round Millstone with Central Hole and Seam\nPlan: Concentric millstone hole and diagonal seam, each seam stops at hole.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Keep source topology; circular opening and interrupted seam.\nKeyshape: CIRCLE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9b28114-7a67-408b-bb64-c72a32b6d82b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/millstone_c9b28114-7a67-408b-bb64-c72a32b6d82b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-millstone-with-central-hole-and-seam'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('round', 'millstone', 'with', 'central', 'hole', 'and', 'seam')

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

        path('stone',(8,36),[((40,12),20,20,True),((8,36),20,20,True)],True)
        path('hole',(20,27),[((28,21),5,5,True),((20,27),5,5,True)],True)
        self.add_line('seam-left',(8,36),(20,27));self.add_line('seam-right',(28,21),(40,12))
        for p in ('seam-left','seam-right'):
            self.relate('connect',p,'stone');self.relate('connect',p,'hole')
