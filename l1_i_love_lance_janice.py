def answer(s):
  x=""
  for idx,c in enumerate(s):
    if(ord(c)<=122) and (ord(c)>=97):
      x=x+chr(219-ord(c))
    else:
      x+=c
  return x

i1="wrw blf hvv ozhg mrtsg'h vkrhlwv?"
print answer(i1) 
i2="Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
print answer(i2)