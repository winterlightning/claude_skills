"""Weather cloud (weather), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '361882de-5b14-5b65-b55b-5cd35ffd633c'
SOURCE_PATH = 'icons-json/weather/weather cloud_361882de-5b14-5b65-b55b-5cd35ffd633c.json'
AUTHOR = 'json_to_solo'

class WeatherCloudWeather(Solo48):
    icon_id = 'weather-cloud-weather'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('weather', 'cloud')

    def build(self):
        self.add_line('e0', (35, 40), (10, 40))
        self.add_bezier('e1', (33, 18), ((31.364, 12.622), (27.8, 8.025), (23.273, 8.025)), ((23.055, 8.025), (22.845, 8), (22.627, 8)), ((22.624, 8), (22.62, 8), (22.617, 8)), ((22.402, 8), (22.188, 8.025), (21.973, 8.025)), ((16.364, 8.025), (11.818, 14.898), (11, 22)))
        self.add_bezier('e2', (33, 18), ((36.955, 17.151), (41.291, 18.831), (43.173, 23.975)), ((43.618, 25.206), (43.982, 26.695), (43.982, 28.086)), ((43.991, 28.271), (43.991, 28.468), (44, 28.652)), ((44, 28.655), (44, 28.658), (44, 28.661)), ((44, 28.843), (43.991, 29.037), (43.991, 29.218)), ((43.991, 34.954), (39.7, 39.975), (35.582, 39.975)), ((35.427, 39.988), (35.282, 39.988), (35.136, 40)), ((35.055, 40), (35.073, 40), (35, 40)))
        self.add_bezier('e3', (10, 40), ((9.555, 40), (9.491, 39.754), (9.073, 39.594)), ((6.418, 38.597), (4.018, 35.348), (4.018, 31.434)), ((4.009, 31.249), (4.009, 31.065), (4, 30.892)), ((4, 30.888), (4, 30.884), (4, 30.88)), ((4, 30.613), (4.018, 30.334), (4.018, 30.068)), ((4.018, 24.677), (7.509, 22.308), (11, 22)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2', 'e0', 'e3')
