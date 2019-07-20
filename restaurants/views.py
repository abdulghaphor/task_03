from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    'my_list' : [
    {'restaurant_name' : 'Slider Station',
    'food_type' : 'Fusion Food'
    },
    {'restaurant_name' : 'Biryani Express',
    'food_type' : 'Indian Cuisine'
    },
    {'restaurant_name' : 'KFC',
    'food_type' : 'Fast Food'
    },
    ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    'my_object' : {
    'restaurant_name' : 'KFC',
    'food_type' : 'Fast Food'
    },
    }
    return render(request, 'detail.html', context)
