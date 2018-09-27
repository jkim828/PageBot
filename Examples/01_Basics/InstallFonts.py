from pagebot.fonttoolbox.objects.font import findFont
from pagebot import getContext
context = getContext()        
#installed = context.installedFonts()
#print(installed) # No fonts installed?
font = findFont('Roboto-Regular')
path = '/Library/Fonts/Georgia.ttf'
context.font(font.path)
#print(context.installedFonts())

bs = context.newString('aaa', style=dict(font=font.path, fontSize=100))
context.text(bs, (120, 120))
