'Sun above two overlapping rolling hills; smallest ridgeline omitted. Natural landscape scene; retain overlapping ridge rhythm and straight lower boundary.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_L uses exact SOLO48 contract bounds. Lucide mountain supplies the baseline-enclosed terrain principle; curves come from the source.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1399e326-2431-4b64-b3d4-29a2736f0ad3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/range_1399e326-2431-4b64-b3d4-29a2736f0ad3.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'rolling-hills-beneath-the-sun'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    aliases = ("Landscape with Mountains and Sun",)
    keywords = ("hill", "landscape", "sun", "countryside", "terrain", "nature")
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
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
        bez('front-left',(4,30),((10,30),(14,30),(18,32)))
        bez('front-right',(18,32),((24,34),(28,37),(32,40)))
        bez('rear',(18,32),((26,22),(34,20),(44,22)))
        poly('boundary',(44,22),(44,40),(32,40),(4,40),(4,30))
        self.add_contour('front','front-left','front-right')
        join('rear','front-left','front-right')
        join('rear','boundary-1');join('front-right','boundary-2','boundary-3')
        join('front-left','boundary-4')
