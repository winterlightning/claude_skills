'Cloud with Rain Drops.\nPlan and review: Retained cloud and all three equally spaced diagonal rain strokes.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide cloud-rain: cloud above evenly spaced rain strokes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b0e7b77-0101-4ff8-b82d-4b17ff5d13e2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cloud rain_1b0e7b77-0101-4ff8-b82d-4b17ff5d13e2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloud-with-rain-drops'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cloud', 'with', 'rain', 'drops')

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

        path('cloud',(12,28),[((4,20),8,8,True),((12,12),8,8,True),((32,12),10,4,True),((44,20),12,8,True),((36,28),8,8,True),(12,28)],True)
        for j,x in enumerate((14,26,38)): self.add_line(f'rain-{j}',(x,36),(x-2,40))
