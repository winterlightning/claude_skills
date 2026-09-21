'Sun above several overlapping rolling hills. Natural landscape scene; retain overlapping ridge rhythm and straight lower boundary.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1399e326-2431-4b64-b3d4-29a2736f0ad3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/range_1399e326-2431-4b64-b3d4-29a2736f0ad3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rolling-hills-beneath-the-sun'
    keyshape = Keyshape.HRECT_L
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

        circle('sun',12,14,6)
        bez('back',(24,28),((30,14),(40,14),(44,22)))
        bez('middle',(4,28),((10,27),(16,29),(24,34)))
        bez('front',(4,40),((16,40),(22,27),(44,30)))
        poly('base',(4,40),(44,40),(44,30));join('front','base')
