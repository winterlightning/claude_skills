'Simple Two Story Building.\nPlan and review: Retained peaked hostel, two upper window marks and centered rectangular door. Omitted facade band; reduced square windows to marks.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide house: roof/walls and centered entry; source pair of upper windows retained as marks.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd68588e8-199b-4759-aaca-fb5c7dd8616b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/hostel_d68588e8-199b-4759-aaca-fb5c7dd8616b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hostel-building'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('hostel', 'building')

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

        path('house',(6,22),[(24,6),(42,22),(42,42),(6,42),(6,22)],True)
        for j,x in enumerate((16,32)):self.add_dot(f'window-{j}',(x,24))
        path('door',(20,42),[(20,32),(28,32),(28,42)]);self.relate('connect','door','house')
