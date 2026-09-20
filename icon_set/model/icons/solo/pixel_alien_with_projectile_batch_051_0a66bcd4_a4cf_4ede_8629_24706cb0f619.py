'Pixel Art Alien Invader. Restored three lower feet to the stepped alien silhouette. Retained raised crown, paired eyes and detached projectile; square source eyes/projectile reduced to dots. HRECT_L fits the broad symmetrical subject and lower projectile. Lucide bot original and atomic-debug inspected for simple paired eye marks and coherent outline construction; pixel silhouette follows the supplied original. SOLO48, stroke4, HRECT_L centerline bounds (4,8)-(44,40).'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a66bcd4-a4cf-4ede-8629-24706cb0f619'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/gamasutra 2_0a66bcd4-a4cf-4ede-8629-24706cb0f619.svg'
AUTHOR = 'gpt-6'

def _circle(icon, name, x, y, r):
    icon.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
    icon.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
    icon.add_contour(name,name+'-top',name+'-bottom',closed=True)

def _path(icon, name, start, commands, closed=False):
    members=[]; p=start
    for i,c in enumerate(commands):
        n=f'{name}-{i}'; q=c[1]
        if c[0]=='L': icon.add_line(n,p,q)
        else: icon.add_arc(n,p,q,radius_x=c[2],radius_y=c[3] if len(c)>3 else c[2],sweep=c[4] if len(c)>4 else True)
        p=q; members.append(n)
    icon.add_contour(name,*members,closed=closed)

class Batch051Icon(Solo48):
    icon_id = 'pixel-alien-with-projectile-batch-051'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('alien', 'pixel', 'invader', 'game', 'projectile', 'arcade', 'space')

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

        # Preserve the stepped crown, three lower feet, two eyes, and detached projectile.
        path('alien',(4,30),[(4,18),(10,18),(10,8),(38,8),(38,18),(44,18),(44,30),(36,30),(36,26),(28,26),(28,30),(20,30),(20,26),(12,26),(12,30),(4,30)],True)
        self.add_dot('eye-left',(20,17))
        self.add_dot('eye-right',(28,17))
        self.add_dot('projectile',(24,40))
