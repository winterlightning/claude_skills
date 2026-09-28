'Cropped lower leg and left-facing foot resting inside horizontal support rails. Preserve support context and heel contour; unify the foot and leg silhouette and omit the upper rail for clearance. No local Lucide foot match.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '198be850-92b5-4683-964e-34fac5eeb9e9'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/bandage leg hanging_198be850-92b5-4683-964e-34fac5eeb9e9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lower-leg-resting-in-a-support'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    semantic_role = "MAIN"
    semantic_kind = "noun"
    aliases = ["Leg in Medical Traction"]
    keywords = ["leg", "foot", "support", "traction", "heel", "medical", "injury"]
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

        line('shin',(22,6),(22,20))
        line('instep',(22,20),(10,24))
        bez('toes',(10,24),((7,25),(6,27),(6,30)),((6,33),(8,33),(10,33)))
        line('sole',(10,33),(24,33))
        self.add_arc('heel',(24,33),(32,25),radius_x=8,sweep=False)
        line('calf',(32,25),(30,6))
        self.add_contour('foot-leg','shin','instep','toes','sole','heel','calf')
        path('support',(6,42),[(34,42),((42,34),8,8,False),(42,24)])
