'Heart-shaped bow opening is intrinsic to key. Keep shaft and teeth.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape SQUARE uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a99dc4a0-50a0-4f59-b6d5-d30eb8b0581c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/love heart key_a99dc4a0-50a0-4f59-b6d5-d30eb8b0581c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'key-with-heart-shaped-bow-opening'
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
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points): self.add_polyline(name,*points)
        def join(*names): self.relate('connect',*names)

        circle('bow',21,27,15)
        poly('shaft',(21,12),(32,12),(42,6));join('shaft','bow')
        poly('tooth',(37,9),(42,15));join('shaft','tooth')
        self.add_arc('heart-left',(21,26),(15,26),radius_x=3,sweep=False)
        line('heart-side1',(15,26),(21,32));line('heart-side2',(21,32),(27,26))
        self.add_arc('heart-right',(27,26),(21,26),radius_x=3,sweep=False)
        self.add_contour('heart','heart-left','heart-side1','heart-side2','heart-right',closed=True)
