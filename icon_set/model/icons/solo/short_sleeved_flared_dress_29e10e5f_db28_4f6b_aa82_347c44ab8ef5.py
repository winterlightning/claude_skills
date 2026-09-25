'Short Sleeve Dress.\nPlan and review: Retained crew neckline, short sleeves, fitted waist seam and flared skirt. Broadened sleeve openings and simplified curved hem to a straight hem.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide shirt: integrated neck scoop and short sleeve silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '29e10e5f-db28-4f6b-aa82-347c44ab8ef5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/frock_29e10e5f-db28-4f6b-aa82-347c44ab8ef5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'short-sleeved-flared-dress'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('short', 'sleeved', 'flared', 'dress')

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

        path('dress',(18,4),[(8,10),(8,20),(16,20),(18,28),(10,44),(38,44),(30,28),(32,20),(40,20),(40,10),(30,4),((18,4),6,6,True)],True)
        self.add_line('waist',(18,28),(30,28));self.relate('connect','waist','dress')
