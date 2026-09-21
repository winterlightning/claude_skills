'Natural bathtub with faucet, three steam curls and feet. Adapt round tub construction; no exact useful Lucide match.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape HRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa441210-00d8-47d0-bf85-1fd419ba1372'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bath_aa441210-00d8-47d0-bf85-1fd419ba1372.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steaming-bathtub-with-a-curved-faucet'
    keyshape = Keyshape.HRECT_L
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

        path('basin',(4,26),[(42,26),(44,26),(41,34),((35,38),6,6,True),(13,38),((7,34),6,6,True),(4,26)],True)
        bez('faucet',(42,26),((42,20),(44,8),(38,8)),((33,8),(34,14),(34,16)))
        join('basin','faucet')
        for x in (6,15,24):
            bez(f'steam{x}',(x,9),((x-2,12),(x+2,14),(x,17)))
        line('foot1',(13,38),(10,40));line('foot2',(35,38),(38,40));join('basin','foot1');join('basin','foot2')
