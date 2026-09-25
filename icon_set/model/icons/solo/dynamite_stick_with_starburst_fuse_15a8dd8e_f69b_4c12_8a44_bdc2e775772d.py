"""dynamite-stick-with-starburst-fuse.
Plan: Rounded diagonal dynamite cylinder with a clearly detached six-ray spark joined by a fuse. Sparse ignition rays retain the starburst without a cramped outlined center.
Keyshape: VRECT_L, exact SOLO48 inset envelope.
Reference construction: Lucide bomb: a visible fuse and simple spark strokes.
Omissions: Outlined starburst replaced by six open ignition rays.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '15a8dd8e-f69b-4c12-8a44-bdc2e775772d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/dynamite_15a8dd8e-f69b-4c12-8a44-bdc2e775772d.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'dynamite-stick-with-starburst-fuse'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('dynamite',)

    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; point=start
            for index, step in enumerate(steps):
                member=f"{name}-{index}"
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def curve(name,start,*segments):
            self.add_bezier(name,start,*segments)

        self.add_line('left-edge',(8,36),(18,26))
        curve('top-cap',(18,26),((20,24),(22,26),(24,28)))
        self.add_line('top-edge',(24,28),(28,32))
        curve('right-corner',(28,32),((30,34),(28,36),(26,38)))
        self.add_line('right-edge',(26,38),(20,44))
        curve('bottom-cap',(20,44),((16,44),(8,40),(8,36)))
        self.add_contour('body','left-edge','top-cap','top-edge','right-corner','right-edge','bottom-cap',closed=True)
        self.add_line('spark-vertical',(32,4),(32,20))
        self.add_line('spark-up',(24,16),(40,8))
        self.add_line('spark-down',(24,8),(40,16))
        for a,b in [('spark-vertical','spark-up'),('spark-vertical','spark-down'),('spark-up','spark-down')]:self.relate('connect',a,b)
        self.add_line('fuse',(24,28),(32,20));self.relate('connect','fuse','body');self.relate('connect','fuse','spark-vertical')
