'Simple Fish Symbol.\nPlan and review: Retained left-facing fish, forked tail and curved gill. Deliberate directional asymmetry follows source.\nKeyshape: HRECT_M, exact SOLO48 envelope.\nConstruction reference: Lucide fish: recognizable tail notch and gill seam; source left-facing orientation retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48c88512-d494-4400-aa6e-1031313b1bfb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fishery_48c88512-d494-4400-aa6e-1031313b1bfb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fish-facing-left'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('fish', 'facing', 'left')

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

        curve('body',(4,24),((12,6),(26,10),(34,20)),((37,16),(41,12),(44,10)),((43,18),(40,22),(40,24)),((40,26),(43,30),(44,38)),((41,36),(37,32),(34,28)),((26,38),(12,42),(4,24)))
        curve('gill',(14,14),((20,20),(20,28),(14,34)));self.relate('connect','gill','body')
