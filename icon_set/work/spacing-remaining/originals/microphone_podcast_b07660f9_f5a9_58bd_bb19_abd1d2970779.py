'Microphone: circular capsule ends, a concentric cradle and no cramped grille ticks.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b07660f9-f5a9-58bd-bb19-abd1d2970779'
SOURCE_PATH = 'icons-json/audio/microphone podcast_b07660f9-f5a9-58bd-bb19-abd1d2970779.json'
AUTHOR = 'gpt-6'

class MicrophonePodcast(Solo48):
    icon_id = 'microphone-podcast'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'podcast', 'audio')

    def build(self):
        # Microphone: circular capsule ends, a concentric cradle and no cramped grille ticks.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        def r(name, x0, y0, x1, y1, radius=4):
            # Equal corner radii and shared tangent endpoints own the rounded box.
            points = [(x0+radius,y0),(x1-radius,y0),(x1,y0+radius),
                      (x1,y1-radius),(x1-radius,y1),(x0+radius,y1),
                      (x0,y1-radius),(x0,y0+radius)]
            ids=[]
            for index,start in enumerate(points):
                end=points[(index+1)%8]
                if start==end:
                    continue
                part=f'{name}-{index}'
                if index%2:
                    a(part,start,end,radius)
                else:
                    l(part,start,end)
                ids.append(part)
            self.add_contour(name,*ids,closed=True)

        r('capsule',17,4,31,28,7)
        l('support-left',(8,22),(8,24))
        a('support-bottom',(8,24),(40,24),16,sweep=False)
        l('support-right',(40,24),(40,22))
        self.add_contour('support','support-left','support-bottom','support-right')
        l('stem',(24,40),(24,44))
        link('connect','stem','support')
