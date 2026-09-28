'Forward-leaning person placing luggage on a conveyor. human_ref/full_body_ref.png informs round head, coherent torso and bent arm; head bottom14 / torso start22 gives exact4 ink gap on the vertical upper-torso axis. Omit the second leg absent from the source; preserve bag handle and conveyor.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '628e2485-fa55-4e32-b7c2-f281f700d7b3'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/baggage leave_628e2485-fa55-4e32-b7c2-f281f700d7b3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'traveler-reaching-toward-a-conveyor-bag'
    keyshape = Keyshape.SQUARE
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    semantic_role = "MAIN"
    semantic_kind = "noun"
    aliases = ["Luggage Drop-off"]
    keywords = ["traveler", "luggage", "conveyor", "bag", "person", "airport", "drop-off"]
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

        circle('head',14,10,4)
        bez('torso',(14,22),((14,27),(6,30),(6,34)))
        line('leg',(6,34),(6,42));join('torso','leg')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        poly('arm',(14,22),(22,26),(30,26));join('arm','torso');join('arm','case')
        poly('case',(30,26),(30,22),(32,22),(40,22),(42,22),(42,34),(30,34),(30,26))
        poly('handle',(32,22),(32,14),(40,14),(40,22));join('handle','case')
        path('conveyor',(30,34),[((30,42),4,4,False),(42,42)]);join('conveyor','case')
