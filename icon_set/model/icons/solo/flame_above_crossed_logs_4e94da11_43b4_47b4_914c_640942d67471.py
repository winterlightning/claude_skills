'Flame above Crossed Logs\nPlan: Asymmetric flame above crossing logs; smaller inner flame removed.\nReference: Lucide flame: one coherent asymmetric contour.\nReduction: Omit inner flame; retain two crossed logs and outer flame.\nKeyshape: VRECT_L; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e94da11-43b4-47b4-914c-640942d67471'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bonfire_4e94da11-43b4-47b4-914c-640942d67471.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'flame-above-crossed-logs'
    keyshape = Keyshape.VRECT_L
    category = "objects"
    keywords = ('flame', 'above', 'crossed', 'logs')

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

        self.add_bezier('flame',(24,28),((12,28),(10,20),(16,14)),((21,9),(23,8),(22,4)),((33,10),(36,15),(36,20)),((36,26),(31,28),(24,28)))
        self.add_contour('flame-outline','flame',closed=True)
        self.add_line('log-left',(8,33),(40,44));self.add_line('log-right',(8,44),(40,33));self.relate('connect','log-left','log-right')
