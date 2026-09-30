# Final repair: Use radial keyshape to retain broad natural moustache proportions and inward lower notch.
'Curled Handlebar Mustache\nPlan: Mirrored handlebar lobes; shared central notch and swept outer ends.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Keep paired lobes and upturned outer ends; broaden slender tips for stroke4.\nKeyshape: HRECT_M; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '607a7616-62ea-408b-9089-0b620729ff0d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/mustache 1_607a7616-62ea-408b-9089-0b620729ff0d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curled-handlebar-mustache'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "beauty"
    categories = ("beauty", "primitive", "primitives")
    keywords = ('curled', 'handlebar', 'mustache')

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

        path('moustache',(24,22),[((16,14),8,8,False),((8,22),8,8,False),(4,24),((14,38),10,14,False),((24,30),10,8,False),((34,38),10,8,False),((44,24),10,14,False),(40,22),((32,14),8,8,False),((24,22),8,8,False)],True)
