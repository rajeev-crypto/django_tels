from django.shortcuts import render
# from .models import Destination

# Create your views here.
def index(request):
#
# 	dest1 = Destination()
# 	dest1.name = 'FIRST PERSON'
# 	dest1.desc = 'efbwfobwoif aofiwe adficnf dd'
# 	dest1.img = 'air-balloon.png'
#
# 	dest2 = Destination()
# 	dest2.name = 'SECOND PERSON'
# 	dest2.desc = 'efbwfobwoif aofiwe adficnf ddf'
# 	dest2.img = 'air-balloon.png'
#
# 	dest3 = Destination()
# 	dest3.name = 'THIRD PERSON'
# 	dest3.desc = 'efbwfobwoif aofiwe adficnf ddf'
# 	dest3.img = 'air-balloon.png'
#
# 	dests = [dest1,dest2,dest3]
# 	return render(request,"index.html",{"dests": dests })
    return render(request,"index.html")
