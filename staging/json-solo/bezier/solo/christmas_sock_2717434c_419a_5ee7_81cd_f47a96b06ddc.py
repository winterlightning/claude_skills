"""Christmas sock (holidays), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2717434c-419a-5ee7-81cd-f47a96b06ddc'
SOURCE_PATH = 'icons-json/holidays/christmas sock_2717434c-419a-5ee7-81cd-f47a96b06ddc.json'
AUTHOR = 'json_to_solo'

class ChristmasSockHolidays(Solo48):
    icon_id = 'christmas-sock-holidays'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('christmas', 'sock', 'holidays')

    def build(self):
        self.add_line('e0', (37, 13), (37, 31))
        self.add_line('e1', (29, 41), (17, 44))
        self.add_line('e2', (20, 21), (20, 13))
        self.add_line('e3', (21, 13), (36, 13))
        self.add_line('e4', (37, 4), (20, 4))
        self.add_bezier('e5', (37, 31), ((37, 34.818), (34.813, 39.136), (31.444, 40.682)), ((30.653, 41.045), (29.825, 40.809), (29, 41)))
        self.add_bezier('e6', (17, 44), ((16.402, 44), (16.067, 43.982), (15.469, 43.982)), ((14.72, 43.982), (13.987, 43.727), (13.297, 43.436)), ((10.307, 42.164), (8.008, 38.945), (8.008, 35.382)), ((8.008, 35.31), (8, 35.247), (8, 35.185)), ((8, 35.184), (8, 35.183), (8, 35.182)), ((8, 35.091), (8.008, 35), (8.008, 34.918)), ((8.008, 32.064), (9.322, 29.282), (11.604, 27.8)), ((12.362, 27.309), (13.272, 27), (14.088, 26.645)), ((16.16, 25.764), (18.678, 24.864), (19.469, 22.373)), ((19.571, 22.073), (20, 21.309), (20, 21)))
        self.add_bezier('e7', (36, 13), ((36.278, 13), (36.354, 13.118), (36.632, 13.091)), ((39.947, 12.778), (40, 10.157), (40, 6.953)), ((40, 6.902), (40, 6.851), (40, 6.8)), ((40, 5.127), (38.568, 4.009), (37.145, 4.009)), ((37.061, 4.009), (36.977, 4), (36.901, 4)), ((36.808, 4), (37.093, 4), (37, 4)))
        self.add_bezier('e8', (20, 4), ((16.707, 4), (16.766, 7.373), (16.758, 9.973)), ((16.749, 11.936), (18.156, 12.936), (19.789, 13.091)), ((20.067, 13.118), (20.722, 13), (21, 13)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2')
        self.add_contour('c1', 'e3', 'e7', 'e4', 'e8', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
