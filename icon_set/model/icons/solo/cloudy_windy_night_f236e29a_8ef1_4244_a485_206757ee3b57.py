'Cloudy Windy Night.\nPlan and review: Retained crescent, cloud and curled wind stroke; crescent asymmetry follows the source.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide cloud-moon and wind: crescent, rounded cloud, hooked wind run.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f236e29a-8ef1-4244-a485-206757ee3b57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/weather night wind 1_f236e29a-8ef1-4244-a485-206757ee3b57.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloudy-windy-night'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('cloudy', 'windy', 'night')

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

        path('cloud',(14,24),[((6,18),8,6,True),((14,12),8,6,True),((24,16),10,4,True),((32,20),8,4,True),((26,24),6,4,True),(14,24)],True)
        curve('moon',(24,16),((24,8),(30,6),(38,6)),((34,9),(34,13),(36,15)),((38,17),(40,18),(42,18)))
        self.relate('connect','cloud','moon')
        path('wind',(10,34),[(34,34),((34,42),4,4,True),(30,42)])
