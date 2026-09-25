'Rainy Weather Cloud.\nPlan and review: Retained broad cloud and three evenly spaced diagonal rain streaks.\nKeyshape: HRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide cloud-rain: cloud over evenly spaced precipitation.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba81c297-bc80-44fc-a380-432a19b372ce'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/hail_ba81c297-bc80-44fc-a380-432a19b372ce.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rain-cloud-with-three-streaks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('rain', 'cloud', 'with', 'three', 'streaks')

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

        path('cloud',(12,27),[((4,19),8,8,True),((12,11),8,8,True),((32,11),10,3,True),((44,19),12,8,True),((36,27),8,8,True),(12,27)],True)
        for j,x in enumerate((14,26,38)):self.add_line(f'rain-{j}',(x,36),(x-2,40))
