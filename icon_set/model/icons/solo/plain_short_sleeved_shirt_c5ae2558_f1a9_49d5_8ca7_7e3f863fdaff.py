'Short Sleeve T-Shirt.\nPlan and review: Retained crew neckline, angled short sleeves and flat torso hem. Mirrored continuous outline.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide shirt: one continuous outline around neck, sleeves and torso.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5ae2558-f1a9-49d5-8ca7-7e3f863fdaff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/garment_c5ae2558-f1a9-49d5-8ca7-7e3f863fdaff.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plain-short-sleeved-shirt'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('plain', 'short', 'sleeved', 'shirt')

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

        path('shirt',(18,6),[(6,14),(10,24),(16,22),(16,42),(32,42),(32,22),(38,24),(42,14),(30,6),((18,6),6,6,True)],True)
