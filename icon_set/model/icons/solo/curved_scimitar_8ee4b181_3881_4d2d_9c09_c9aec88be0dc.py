"""curved-scimitar.
Plan: Swept scimitar blade with continuous belly curve, diagonal guard and rounded grip. Guard owns actual blade and grip junctions.
Keyshape: SQUARE, exact SOLO48 inset envelope.
Reference construction: Lucide sword: diagonal guard and connected grip.
Omissions: Small guard thickness.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8ee4b181-3881-4d2d-9c09-c9aec88be0dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/40-8ee4b181-3881-4d2d-9c09-c9aec88be0dc.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'curved-scimitar'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('weapon', 'scimitar')

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

        curve('blade',(17,28),((25,24),(32,18),(33,12)),((36,10),(39,8),(42,6)),((42,22),(37,30),(25,36)))
        self.add_line('guard',(12,23),(30,41));self.relate('connect','guard','blade')
        curve('grip',(17,28),((10,33),(6,34),(6,38)),((6,40),(8,42),(10,42)),((13,42),(19,37),(23,34)))
        self.relate('connect','grip','guard');self.relate('connect','grip','blade')
