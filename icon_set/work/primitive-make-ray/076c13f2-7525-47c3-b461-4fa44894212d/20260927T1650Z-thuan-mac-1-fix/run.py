import importlib.util, json, sys, cairosvg
R='icon_set/work/primitive-make-ray/076c13f2-7525-47c3-b461-4fa44894212d/20260927T1650Z-thuan-mac-1-fix'
spec=importlib.util.spec_from_file_location('m', R+'/bare_three_arm_chandelier_076c13f2_7525_47c3_b461_4fa44894212d.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
icon=m.BareThreeArmChandelier(); rep=icon.validate_icon(); d=rep.describe(); print(d)
open(R+'/validation.txt','w').write(d)
svg=icon.to_svg(); open(R+'/bare-three-arm-chandelier.svg','w').write(svg)
for th,bg,fg in (('light','white','black'),('dark','#111','white')):
    s=svg.replace('currentColor',fg)
    for size,suf in ((48,''),(384,'-x8')):
        cairosvg.svg2png(bytestring=s.encode(),write_to=f'{R}/preview-{th}{suf}.png',output_width=size,output_height=size,background_color=bg)
