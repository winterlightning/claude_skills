'Rainy Night Cloud with Moon.\nPlan and review: Retained crescent moon, small cloud and three diagonal rain marks. Reduced cloud width for moon clearance.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide cloud-moon-rain: crescent, compact cloud and repeated rain marks.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f73b2a6-4779-44dc-b31b-ecfec5449a1d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/weather night snow_8f73b2a6-4779-44dc-b31b-ecfec5449a1d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rainy-night'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('rainy', 'night')

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

        path('cloud',(14,28),[((6,20),8,8,True),((14,12),8,8,True),((26,20),12,8,True),((34,28),8,8,True),(14,28)],True)
        curve('moon',(42,6),((32,6),(32,16),(42,16)))
        for j,x in enumerate((16,27,38)):self.add_line(f'rain-{j}',(x,37),(x-3,42))
