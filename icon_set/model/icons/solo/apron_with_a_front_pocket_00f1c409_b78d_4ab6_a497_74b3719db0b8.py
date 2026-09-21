'Looped bib apron with curved sides, waist ties and rounded pocket. Curved tailored silhouette, no invented decoration.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00f1c409-b78d-4ab6-a497-74b3719db0b8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/apron_00f1c409-b78d-4ab6-a497-74b3719db0b8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'apron-with-a-front-pocket'
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

        path('strap',(18,14),[(18,10),((30,10),6,6,True),(30,14)])
        bez('apron',(18,14),((18,20),(12,21),(8,22)),((8,25),(8,25),(8,28)),((8,36),(8,44),(14,44)),((20,44),(28,44),(34,44)),((40,44),(40,36),(40,28)),((40,25),(40,25),(40,22)),((36,21),(30,20),(30,14)))
        line('bib',(18,14),(30,14));join('bib','apron');join('strap','apron');join('strap','bib')
        path('pocket',(19,27),[(29,27),(29,31),((25,35),4,4,True),(23,35),((19,31),4,4,True),(19,27)],True)
