'Article with Left Picture\nPlan: Picture block to left of three short paragraph lines; two long lines below.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Two lower lines replace three; abstract paragraph marks are not typeface characters.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b092f25e-e197-4703-97a1-2155fbcce7f1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/paragraph image left_b092f25e-e197-4703-97a1-2155fbcce7f1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'article-left-picture'
    keyshape = Keyshape.SQUARE
    category = "objects"
    keywords = ('article', 'left', 'picture')

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

        box('picture',6,6,24,22,4)
        for k,y in enumerate([6,14,22]):self.add_line(f'short-{k}',(33,y),(42,y))
        self.add_line('text-1',(6,32),(42,32));self.add_line('text-2',(6,42),(34,42))
