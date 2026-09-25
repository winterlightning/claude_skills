'Three groups of toe marks form a triangular bird-track pattern. HRECT_L centers the natural repeated group, extremes 4,8,44,40. All groups derive from the same joined three-toe fan and short heel; lower groups are translated symmetrically. Source supplies the three-toe identity and triangular arrangement; no useful Lucide track match. Join the three toes at their heel for native-size recognition; no toes omitted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6107dfed-38bb-4868-8bec-237b30cef327'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/animal print bird 1_6107dfed-38bb-4868-8bec-237b30cef327.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'three-scattered-bird-tracks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('Three Scattered Bird Tracks',)
    keywords = ('bird', 'tracks', 'footprints', 'toes', 'pattern', 'animal', 'wildlife')
    def build(self):
        def path(name,start,steps,closed=False):
            members=[];point=start
            for j,step in enumerate(steps):
                member=f"{name}-{j}"
                if len(step)==2:self.add_line(member,point,step);point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        for i,(x,y) in enumerate([(24,8),(12,28),(36,28)]):
            heel=(x,y+8)
            self.add_polyline(f'track-{i}-fan',(x-8,y+2),heel,(x+8,y+2))
            self.add_polyline(f'track-{i}-middle',(x,y),heel,(x,y+12))
            self.relate('connect',f'track-{i}-fan',f'track-{i}-middle')
