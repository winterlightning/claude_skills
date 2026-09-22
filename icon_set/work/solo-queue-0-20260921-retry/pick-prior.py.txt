'Handled lock pick enters an open padlock keyhole. Natural tool interaction; preserve open shackle and bent pick.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f4d0d07-e981-4efd-ae8c-b673077a9b75'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/crime tools loackpick unlock_7f4d0d07-e981-4efd-ae8c-b673077a9b75.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pick-entering-open-padlock'
    keyshape = Keyshape.VRECT_L
    category = "objects"
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

        path('lock',(18,28),[(18,24),((22,20),4,4,True),(36,20),((40,24),4,4,True),(40,40),((36,44),4,4,True),(24,44)])
        path('shackle',(22,20),[(22,13),((40,13),9,9,True)]);join('lock','shackle')
        circle('keyhole',29,32,2)
        bez('handle',(8,38),((8,35),(11,32),(14,32)),((17,32),(20,35),(20,38)),((20,41),(17,44),(14,44)),((11,44),(8,41),(8,38)))
        poly('pick',(18,33),(23,29),(27,32));join('pick','handle');join('pick','keyhole')
