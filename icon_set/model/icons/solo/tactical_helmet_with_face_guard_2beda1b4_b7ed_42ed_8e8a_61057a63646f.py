'Tactical Battle Royale Helmet. Plan and review: Side-view combat shell, projecting visor and lower guard retained. Fine visor subdivision is omitted; asymmetric forward projection preserves direction. Keyshape HRECT_L centerline envelope (4,8)-(44,40). Chosen to fit the complete subject silhouette. Reference: No useful Lucide character match; original silhouette and identifying features guide construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2beda1b4-b7ed-42ed-8e8a-61057a63646f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-10/sport esport battle royal public unknown battlegound pubg_2beda1b4-b7ed-42ed-8e8a-61057a63646f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tactical-helmet-with-face-guard'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('tactical', 'helmet', 'with', 'face', 'guard')

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

        curve('shell',(8,20),((12,12),(20,8),(28,8)),((38,8),(44,16),(44,26)),((44,30),(44,34),(40,34)))
        path('guard',(40,34),[(30,34),(30,40),(8,40),(8,30)])
        self.relate('connect','shell','guard')
        box('visor',4,20,30,30,4);self.relate('connect','shell','visor');self.relate('connect','guard','visor')
