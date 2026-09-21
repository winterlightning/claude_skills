'Litter tray and slotted scoop on a diagonal long handle. Keep physical tool-and-tray pairing, not a state modifier.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6e7ff28-6ade-4296-95f7-4a6c7bd1ce2a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/cat litter_e6e7ff28-6ade-4296-95f7-4a6c7bd1ce2a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'litter-tray-with-slotted-scoop'
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

        path('tray',(6,26),[(42,26),(38,38),((34,42),4,4,True),(14,42),((10,38),4,4,True),(6,26)],True)
        bez('scoop',(18,26),((19,18),(22,13),(27,14)),((28,14),(29,15),(30,16)),((35,18),(35,21),(32,26)))
        path('handle',(27,14),[(32,8),((40,8),4,4,True),(34,21)]);join('handle','scoop');join('scoop','tray')
        line('slot',(24,18),(24,18))
