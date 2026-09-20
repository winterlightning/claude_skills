'Roller Coaster and Ferris Wheel.\nPlan and review: Retained Ferris wheel and sloping roller-coaster track. Reduced spokes to three and supports to two, omitted ground baseline and small hub polygon. Both source UUIDs are recorded on this shared model.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide ferris-wheel: circular wheel with radial spokes; source coaster scene retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7fa6c31c-7745-4025-99b4-16a7e22d9594'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/theme park_7fa6c31c-7745-4025-99b4-16a7e22d9594.svg'
# Additional source reference with identical rendered artwork.
SOURCE_ICON_IDS = ('7fa6c31c-7745-4025-99b4-16a7e22d9594', '9cf656a0-7a4a-4dd2-9361-da20c0c4b28b')
SOURCE_PATHS = ('/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-011/references/21-7fa6c31c-7745-4025-99b4-16a7e22d9594.svg', '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-011/references/22-9cf656a0-7a4a-4dd2-9361-da20c0c4b28b.svg')
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'roller-coaster-ferris-wheel'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('roller', 'coaster', 'ferris', 'wheel')

    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; point=start
            for index, step in enumerate(steps):
                member=f"{name}-{index}"
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def curve(name,start,*segments):
            self.add_bezier(name,start,*segments)

        circle('wheel',30,18,12)
        self.add_line('spoke-top',(30,6),(30,18));self.add_line('spoke-left',(30,18),(18,18));self.add_line('spoke-right',(30,18),(42,18))
        for s in ('spoke-top','spoke-left','spoke-right'):self.relate('connect',s,'wheel')
        self.relate('connect','spoke-top','spoke-left');self.relate('connect','spoke-top','spoke-right');self.relate('connect','spoke-left','spoke-right')
        curve('track',(6,32),((6,22),(10,22),(12,32)),((16,40),(24,42),(30,42)),((34,42),(38,42),(42,42)))
        self.add_line('wheel-stand',(30,30),(30,42));self.relate('connect','wheel-stand','wheel');self.relate('connect','wheel-stand','track')
        self.add_line('support',(6,32),(6,42));self.relate('connect','support','track')
