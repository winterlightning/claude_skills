'Lucide ear informs separated helix and inner fold. Long lobe silhouette and open lower break preserved.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_M uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8126e9a2-22b5-4d46-a54c-c4a899d830a2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/cartilage_8126e9a2-22b5-4d46-a54c-c4a899d830a2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'outer-ear-with-curved-folds'
    keyshape = Keyshape.VRECT_M
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

        bez('outer',(10,22),((10,10),(15,4),(24,4)),((33,4),(38,10),(38,20)),((38,28),(31,33),(28,39)),((26,43),(24,44),(20,44)),((15,44),(12,40),(12,35)))
        bez('inner',(20,29),((20,25),(27,24),(28,20)),((29,14),(20,12),(19,19)))
