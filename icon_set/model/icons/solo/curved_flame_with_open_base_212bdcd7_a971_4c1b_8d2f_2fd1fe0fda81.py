'Simple Curved Fire Flame.\nPlan and review: Retained curved left upper tip, secondary right tongue and open inner base. Rebalanced outer tongue for internal clearance.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide flame: coherent outer tongue and inner turn; preserve source split base.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '212bdcd7-a971-4c1b-8d2f-2fd1fe0fda81'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fire flame curved_212bdcd7-a971-4c1b-8d2f-2fd1fe0fda81.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-flame-with-open-base'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('curved', 'flame', 'with', 'open', 'base')

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

        curve('flame',(20,44),((8,42),(8,34),(8,28)),((8,18),(26,14),(22,4)),((30,12),(32,18),(28,24)),((36,24),(38,20),(40,18)),((40,34),(40,40),(28,44)),((32,40),(28,36),(24,30)),((18,36),(16,40),(20,44)))
