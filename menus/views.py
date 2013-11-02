from django.http import Http404
from django.http import HttpResponse
from menus.models import User
from menus.models import Menu
from menus.models import Option
import json
from pprint import *

def home(request):
    return HttpResponse("Home works")

def is_user(request, num):
    try:
        User.objects.get(number=num)
    except User.DoesNotExist:
        raise Http404
    return HttpResponse(num)

def get_menu(request, num):
    json_menu = None
    try:
        menu = Menu.objects.get(number=num)
        json_menu = menu_to_json(menu)
    except Menu.DoesNotExist:
        raise Http404
    return HttpResponse(json.dumps(json_menu), content_type="application/json")

def menu_to_json(menu):
    json_menu = {}
    json_menu['name'] = menu.name
    print menu.name
    json_menu['number'] = menu.number
    print menu.number

    def add_menu_to_hash(opt, key):
	try:
	    lagtime = ','*(opt.lag/2)
            if (key != '~') and opt.lag > 2:
		print key+'~', lagtime
                json_menu[key+'~'] = lagtime
	    if key == '~':
		print key, lagtime
		json_menu[key] = lagtime
		key = ''
	    else:
		print key, opt.name
                json_menu[key] = opt.name
            i = 0
	    if opt.one != 0 and Option.objects.get(id=opt.one):
		#print Option.objects.get(id=opt.one), "1"
		add_menu_to_hash(Option.objects.get(id=opt.one), key+'1')
            if opt.two != 0 and Option.objects.get(id=opt.two):                
		#print Option.objects.get(id=opt.two), "2"
                add_menu_to_hash(Option.objects.get(id=opt.two), key+'2')
	    if opt.three != 0 and Option.objects.get(id=opt.three):
                #print Option.objects.get(id=opt.three), "3"
                add_menu_to_hash(Option.objects.get(id=opt.three), key+'3')
	    if opt.four != 0 and Option.objects.get(id=opt.four): 
		#print Option.objects.get(id=opt.four), "4"
		add_menu_to_hash(Option.objects.get(id=opt.four), key+'4')
	    if opt.five != 0 and Option.objects.get(id=opt.five):
		#print Option.objects.get(id=opt.five), "5"
		add_menu_to_hash(Option.objects.get(id=opt.five), key+'5')
	    if opt.six != 0 and Option.objects.get(id=opt.six):
		#print Option.objects.get(id=opt.six), "6"
		add_menu_to_hash(Option.objects.get(id=opt.six), key+'6')
	    if opt.seven != 0 and Option.objects.get(id=opt.seven):
		#print Option.objects.get(id=opt.seven), "7"
		add_menu_to_hash(Option.objects.get(id=opt.seven), key+'7')
	    if opt.eight != 0 and Option.objects.get(id=opt.eight):
		#print Option.objects.get(id=opt.eight), "8"
		add_menu_to_hash(Option.objects.get(id=opt.eight), key+'8')
	    if opt.nine != 0 and Option.objects.get(id=opt.nine):
		#print Option.objects.get(id=opt.nine), "9"
		add_menu_to_hash(Option.objects.get(id=opt.nine), key+'9')
	    if opt.star != 0 and Option.objects.get(id=opt.star):
		#print Option.objects.get(id=opt.star), "*"
		add_menu_to_hash(Option.objects.get(id=opt.star), key+'*')
	    if opt.zero != 0 and Option.objects.get(id=opt.zero):
		#print Option.objects.get(id=opt.zero), "0"
		add_menu_to_hash(Option.objects.get(id=opt.zero), key+'0')
	    if opt.hash != 0 and Option.objects.get(id=opt.hash):
		#print Option.objects.get(id=opt.hash), "#"
		add_menu_to_hash(Option.objects.get(id=opt.hash), key+'#')

	except Option.DoesNotExist:
	    raise Http404
        return

    try:
        all_options = Option.objects.filter(menu=menu)#check to make sure this works
        for opt in all_options:
	    if opt.level == 0:
	        add_menu_to_hash(opt, opt.tag)  
    except Option.DoesNotExist:
	raise Http404
    print json.dumps(json_menu)
    return json_menu

#fn to add menus into db
def add_menu:
    pass
