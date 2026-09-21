'Single candle on broad altar with pedestal foot. Preserve flame, candle, tabletop and lower body as one ritual object.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aab703f2-f6b1-439b-ab60-34abe9968c63'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/altar_aab703f2-f6b1-439b-ab60-34abe9968c63.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'candle-on-a-pedestal-altar'
    keyshape = Keyshape.SQUARE
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

        bez('flame',(24,6),((20,10),(18,12),(18,15)),((18,18),(21,20),(24,20)),((27,20),(30,18),(30,15)),((30,12),(28,10),(24,6)))
        poly('candle',(20,30),(20,20),(28,20),(28,30));join('candle','flame')
        poly('top',(6,30),(42,30),(42,38),(6,38),(6,30));join('candle','top')
        poly('plinth',(12,38),(10,42),(38,42),(36,38));join('plinth','top')
