'Round banded planet with a distinct lower spot. Retain a sparse band count suitable for native48; source planet identity depends on both bands and spot.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape CIRCLE uses exact SOLO48 contract bounds. Lucide orbit informs the closed circular contours; the supplied reference sets band placement and the lower storm spot. Extra thin bands omitted for clearance.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e44ac12f-4749-48aa-9071-2f48962ca3f8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/astronomy planet jupiter_e44ac12f-4749-48aa-9071-2f48962ca3f8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'banded-planet-with-a-large-round-spot'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("Jupiter Planet with Great Red Spot",)
    keywords = ("planet", "jupiter", "bands", "spot", "astronomy", "space", "sphere")
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

        # Split the ring at each physical band attachment.
        nodes=[(4,24),(8,12),(40,12),(44,24),(24,44),(8,36),(4,24)]
        for i,(a,b) in enumerate(zip(nodes,nodes[1:])):
            self.add_arc(f'rim-{i}',a,b,radius_x=20,sweep=True)
        self.add_contour('planet',*[f'rim-{i}' for i in range(6)],closed=True)
        line('top-band',(8,12),(40,12));join('top-band','planet')
        line('middle-band',(4,24),(15,24));join('middle-band','planet')
        line('lower-band',(8,36),(14,36));join('lower-band','planet')
        circle('spot',28,29,5)
