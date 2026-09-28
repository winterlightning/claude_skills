'Left-facing pheasant with raised long tail, wing and two legs. Lucide bird informs simplified breast and wing; tail remains deliberately asymmetric.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ec3f373-1143-413c-9c5d-6a91026ab479'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pheasant_7ec3f373-1143-413c-9c5d-6a91026ab479.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pheasant-raised-tail'
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

        bez('body',(6,14),((12,3),(20,6),(20,16)),((20,22),(31,22),(34,32)),((32,33),(31,34),(30,34)),((26,36),(20,36),(18,34)),((14,32),(12,29),(12,23)),((12,17),(11,14),(6,14)))
        bez('tail',(28,25),((34,19),(38,12),(42,6)),((40,20),(38,26),(34,32)));join('tail','body')
        line('leg-left',(18,34),(14,42));line('leg-right',(30,34),(28,42));join('leg-left','body');join('leg-right','body')
