'Elephant Head and Trunk.\nPlan and review: Retained broad elephant ear/crown and long curling trunk. Omitted tiny trunk divisions. Rebuilt curved extrema exactly on the keyshape.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '709b50ed-3ff8-48bf-8633-dd4ca59593d1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/ivory_709b50ed-3ff8-48bf-8633-dd4ca59593d1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'elephant-head-and-curved-trunk'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('elephant', 'head', 'and', 'curved', 'trunk')

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

        path('head',(24,16),[(24,24),((8,24),8,8,True),(8,20),((24,4),16,16,True),((40,20),16,16,True),(40,38),((28,38),6,6,True),(28,30)])
