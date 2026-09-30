from refine2 import *
D['traditional-japanese-mochi']['shape']='SQUARE'
D['traditional-japanese-mochi']['code']='''
path('dumpling',(20,42),[('C',(6,24),(12,42),(6,34)),('A',(24,6),18,18,True),('A',(42,24),18,18,True),('C',(28,42),(42,34),(36,42))])
path('inset',(19,33),[('C',(15,28),(16,33),(15,31)),('A',(33,28),9,6,True),('C',(29,33),(33,31),(32,33))])
'''
if __name__=='__main__':generate(['traditional-japanese-mochi'])
