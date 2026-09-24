"""cuffed-thumbs-up.
Plan: Continuous hand silhouette, rounded thumb and fingertip transitions, full cuff and one finger separator; width allocated before detailing.
Keyshape: SQUARE, exact SOLO48 inset envelope.
Reference construction: Lucide thumbs-up: contiguous thumb-palm contour and single cuff divider.
Omissions: Three finger dividers reduced to one.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1f9081ba-1e28-4062-8437-47975e42f022'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/thumb_1f9081ba-1e28-4062-8437-47975e42f022.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'cuffed-thumbs-up'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('thumb',)

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

        path('outline',(6,26),[((10,22),4,4,True),(16,22),(24,14),(24,6),(28,6),((32,10),4,4,True),(29,22),(36,22),((42,28),6,6,True),(42,36),((36,42),6,6,True),(10,42),((6,38),4,4,True),(6,26)],True)
        self.add_line('cuff',(16,22),(16,42));self.relate('connect','cuff','outline')
        self.add_line('finger',(33,32),(42,32));self.relate('connect','finger','outline')
