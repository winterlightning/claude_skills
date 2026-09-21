'Curved spleen with indented medial edge and descending extension. Preserve recognizability without fabricated internal texture.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e86ab8c8-6204-4bb3-92c1-62c6cc35d7cc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/spleen_e86ab8c8-6204-4bb3-92c1-62c6cc35d7cc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-spleen-with-indented-inner-edge'
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

        bez('spleen',(8,44),((8,30),(22,30),(20,20)),((17,9),(22,4),(28,4)),((37,4),(40,13),(40,24)),((40,38),(32,44),(25,44)),((21,44),(19,42),(18,40)))
        bez('inner',(18,40),((12,31),(27,29),(27,23)))
        join('spleen','inner')
