'AdMob mark: smooth arch and return, consistent verticals and a clear inner counter.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '166238e9-fe64-4404-9aa2-ae5f4b82de80'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_01/admob logo_166238e9-fe64-4404-9aa2-ae5f4b82de80.svg'
AUTHOR = 'gpt-6'

class AdmobLogo(Solo48):
    icon_id = 'admob-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('admob', 'logo', '_uncategorized_01')

    def build(self):
        # AdMob mark: smooth arch and return, consistent verticals and a clear inner counter.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        l('outer-start',(22,44),(16,44))
        a('outer-bl',(16,44),(8,36),8)
        l('outer-left',(8,36),(8,20))
        a('outer-top',(8,20),(40,20),16)
        l('outer-right',(40,20),(40,38))
        a('outer-br',(40,38),(34,44),6)
        a('tail',(34,44),(28,38),6)
        l('inner-right',(28,38),(28,20))
        a('inner-top',(28,20),(18,20),5,sweep=False)
        l('inner-left',(18,20),(18,34))
        l('inner-bottom',(18,34),(28,34))
        self.add_contour('outer','outer-start','outer-bl','outer-left','outer-top','outer-right','outer-br','tail','inner-right','inner-top','inner-left','inner-bottom')
