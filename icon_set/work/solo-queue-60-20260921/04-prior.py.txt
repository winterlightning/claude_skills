'Tapered berry cluster and one pointed upper-right leaf. Rounded drupelet lobes define the fruit; simplify the internal cell count coherently.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd0fd2f9-cb2d-40e6-8f25-806b358d94e5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/marionberry_cd0fd2f9-cb2d-40e6-8f25-806b358d94e5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clustered-marionberry-with-pointed-leaf'
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

        for name,x,y in [('top-left',16,20),('top-right',28,20),('mid-left',14,30),('mid-right',30,30),('bottom',22,38)]:circle(name,x,y,6)
        for a,b in [('top-left','top-right'),('top-left','mid-left'),('top-right','mid-right'),('mid-left','bottom'),('mid-right','bottom')]:join(a,b)
        bez('leaf',(26,14),((26,6),(32,4),(40,4)),((40,12),(34,16),(26,14)));join('leaf','top-right')
