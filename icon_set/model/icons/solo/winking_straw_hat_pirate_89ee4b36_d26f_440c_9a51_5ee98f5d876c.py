'Winking Straw Hat Pirate. Plan and review: Wide straw-hat brim, rounded crown, round face and wink retained. Small smile, ears and hairline omitted to keep the wink clear. Keyshape HRECT_L centerline envelope (4,8)-(44,40). Chosen to fit the complete subject silhouette. Reference: No useful Lucide character match; original silhouette and identifying features guide construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89ee4b36-d26f-440c-9a51-5ee98f5d876c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-08/pirate luffy onepiece_89ee4b36-d26f-440c-9a51-5ee98f5d876c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'winking-straw-hat-pirate'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('winking', 'straw', 'hat', 'pirate')

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

        path('crown',(8,18),[((24,8),16,10,True),((40,18),16,10,True)]);self.relate('connect','crown','face')
        self.add_line('brim',(4,18),(44,18));self.relate('connect','crown','brim')
        curve('face',(8,18),((8,30),(12,40),(24,40)),((36,40),(40,30),(40,18)));self.relate('connect','face','brim')
        self.add_dot('eye',(18,27));self.add_line('wink',(28,27),(31,26))
        
