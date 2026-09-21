'Hands Sheltering a Baby Head\nPlan: Mirrored protective hands arch above the baby; broad circular head.\nReference: Shared human user.svg circular head vocabulary; Lucide hand anatomical reduction.\nReduction: Drop facial curl and finger outlines; retain head and two sheltering hand gestures.\nKeyshape: SQUARE; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b0f724c-6381-4158-9f19-2b2a426b6450'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/baby guard protect 2_0b0f724c-6381-4158-9f19-2b2a426b6450.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hands-sheltering-a-baby-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('hands', 'sheltering', 'a', 'baby', 'head')

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

        circle('baby',24,32,10)
        for side in (-1,1):
            def p(x,y):return (24+side*x,y)
            self.add_polyline(f'hand-{side}',p(18,26),p(16,14),p(5,6))
