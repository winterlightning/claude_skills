'Sonic Hedgehog Character Head. Plan and review: Left-facing hedgehog keeps a projecting muzzle, tall eye, swept rear spines and smile. Ear and fine muzzle partitions are omitted; intentional left-facing asymmetry retained. Keyshape HRECT_L centerline envelope (4,8)-(44,40). Chosen to fit the complete subject silhouette. Reference: No useful Lucide character match; original silhouette and identifying features guide construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1523257c-f68a-456e-8c4e-d496652940a0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-10/sonic_1523257c-f68a-456e-8c4e-d496652940a0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sonic-head-in-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('sonic', 'head', 'in', 'profile')

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

        path('head',(4,26),[(10,26),(10,20),((22,8),12,12,True),(36,8),(30,16),(40,20),(34,26),(44,32),(34,32),(28,40),(16,40),((4,28),12,12,True),(4,26)],True)
        self.add_line('eye',(19,20),(19,22))
        curve('smile',(17,31),((19,32),(21,32),(23,30)))
