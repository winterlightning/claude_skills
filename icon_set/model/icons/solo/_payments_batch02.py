"""Shared directly authored SOLO48 currency construction for payment batch 02."""
SOURCE_ICON_ID=None
SOURCE_PATH='work/payments-solo/batch-02/briefs'
AUTHOR='gpt-6'

def small_dollar(icon,x,y):
    rx,ry=3,3
    icon.add_line('dollar-top',(x+rx,y-2*ry),(x,y-2*ry))
    icon.add_arc('dollar-upper',(x,y-2*ry),(x,y),radius_x=rx,radius_y=ry,sweep=False)
    icon.add_arc('dollar-lower',(x,y),(x,y+2*ry),radius_x=rx,radius_y=ry)
    icon.add_line('dollar-bottom',(x,y+2*ry),(x-rx,y+2*ry))
    icon.add_contour('dollar','dollar-top','dollar-upper','dollar-lower','dollar-bottom')
    icon.add_line('dollar-stem-top',(x,y-7),(x,y-6))
    icon.add_line('dollar-stem-bottom',(x,y+6),(x,y+7))
    icon.relate('connect','dollar','dollar-stem-top')
    icon.relate('connect','dollar','dollar-stem-bottom')
