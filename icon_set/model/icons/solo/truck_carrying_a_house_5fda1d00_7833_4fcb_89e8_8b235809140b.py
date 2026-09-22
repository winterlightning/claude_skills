'Physical house carried on flatbed: one scene, not an applied modifier. Two wheels, left cab and gabled payload retained; cramped doorway omitted.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_L uses exact SOLO48 contract bounds. Lucide truck informs chassis runs split at the wheel contacts.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5fda1d00-7833-4fcb-89e8-8b235809140b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/real estate truck house_5fda1d00-7833-4fcb-89e8-8b235809140b.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'truck-carrying-a-house'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    aliases = ("House Relocation Truck",)
    keywords = ("truck", "house", "moving", "transport", "flatbed", "vehicle")
    category = "transport"
    def build(self):



        def path(name,start,steps,closed=False):
            members=[]; point=start
            for j,step in enumerate(steps):
                member=f'{name}-{j}'
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=4):
            if rad==0:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),(l,t)); return
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        def bez(name,start,*segments): self.add_bezier(name,start,*segments)

        poly('cab',(4,37),(4,24),(8,20),(16,20))
        poly('house',(16,26),(16,20),(16,18),(30,8),(44,18),(44,26),(16,26))
        line('chassis-left',(4,37),(12,37));line('chassis-middle',(18,37),(30,37));poly('chassis-right',(36,37),(44,37),(44,26))
        for name,x in [('wheel-left',15),('wheel-right',33)]:
            circle(name,x,37,3)
        join('cab-3','house-1','house-2')
        join('cab-1','chassis-left');join('house-5','house-6','chassis-right-2')
        join('chassis-left','wheel-left-0','wheel-left-1');join('chassis-middle','wheel-left-0','wheel-left-1')
        join('chassis-middle','wheel-right-0','wheel-right-1');join('chassis-right-1','wheel-right-0','wheel-right-1')
