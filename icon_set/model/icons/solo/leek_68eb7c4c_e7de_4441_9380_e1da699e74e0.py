'Simple Garden Leek.\nPlan and review: Retained leek stalk with a curved left leaf and cut-ended diagonal right leaf. Reduced three leaves to two because the central blade crowded both neighboring blades.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: No useful exact Lucide match; source silhouette and geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68eb7c4c-e7de-4441-9380-e1da699e74e0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/leek_68eb7c4c-e7de-4441-9380-e1da699e74e0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'leek'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('leek',)

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

        path('leek',(12,44),[(22,44),(30,22),(40,12),(32,4),(20,24)])
        curve('left',(20,24),((20,12),(16,4),(8,4)),((16,22),(12,30),(12,44)));self.relate('connect','leek','left')
