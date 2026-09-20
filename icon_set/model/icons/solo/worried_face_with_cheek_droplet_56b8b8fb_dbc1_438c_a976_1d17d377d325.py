'Sad Face with Sweat Drop.\nPlan and review: Retained raised brows, short eyes, frown and right cheek droplet. Simplified droplet to round bulb and attached eye track; shifted small frown left. Existing complete-circle diameter4 exception only.\nKeyshape: CIRCLE, exact SOLO48 envelope.\nConstruction reference: Source face and tear; Lucide circular-face vocabulary.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56b8b8fb-dbc1-438c-a976-1d17d377d325'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/face sad sweat_56b8b8fb-dbc1-438c-a976-1d17d377d325.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'worried-face-with-cheek-droplet'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('worried', 'face', 'with', 'cheek', 'droplet')

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

        circle('head',24,24,20)
        self.add_line('brow-left',(18,15),(20,14));self.add_line('brow-right',(28,14),(30,15))
        self.add_line('eye-left',(18,23),(20,23));self.add_line('eye-right',(28,23),(30,23))
        self.add_arc('frown',(17,33),(21,33),radius_x=2,radius_y=2,sweep=True)
        path('tear',(30,26),[((30,30),2,2,True),((30,26),2,2,True)],True)
        self.add_line('tear-tip',(30,23),(30,26));self.relate('connect','tear-tip','tear')
        self.relate('connect','eye-right','tear')
        self.relate('connect','tear-tip','eye-right')
