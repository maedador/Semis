from django.shortcuts import render

def about(request):

    context = {
        'user' : 'Mae De Mesa',
        'fname' : 'Mae',
        'lname' : 'De Mesa',
        'age' : '21',
        'paragraph' : 'Video provides a powerful way to help you prove your point. When you click Online Video, \
        you can paste in the embed code for the video you want to add. \
        You can also type a keyword to search online for the video that best fits your document.',
        'paragraph1' : 'Video provides a powerful way to help you prove your point. When you click Online Video, \
        you can paste in the embed code for the video you want to add. \
        You can also type a keyword to search online for the video that best fits your document.'

    }

    return render(request,'about.html',context)
# Create your views here.
