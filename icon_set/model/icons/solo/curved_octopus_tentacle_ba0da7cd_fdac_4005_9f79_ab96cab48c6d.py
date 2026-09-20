'Curved Octopus Tentacle.\nPlan and review: Retained S-shaped taper and hooked tip; reduced four suction details to one small circular cup. The diameter4 cup uses the existing small-circle contract exception; no new waiver was added.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: No useful Lucide subject match; source render guides construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba0da7cd-fdac-4005-9f79-ab96cab48c6d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tentacle_ba0da7cd-fdac-4005-9f79-ab96cab48c6d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-octopus-tentacle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('curved', 'octopus', 'tentacle')

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

        curve('outer',(8,44),((8,34),(8,28),(14,24)),((26,16),(34,18),(30,4)),((36,4),(40,10),(40,16)),((40,26),(31,30),(31,36)),((31,40),(31,42),(33,44)))
        circle('sucker-low',20,36,2)
