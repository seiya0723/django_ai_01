from django.shortcuts import render,redirect

## Create your views here.
#from django.shortcuts import render
from django.views import View

from .models import Design

class illustView(View):

    def get(self, request, *args, **kwargs):

        #Designクラスを使用し、DBへアクセス、データ全件閲覧
        designs = Design.objects.all()

        button1     = "Prev"
        data        = "データのプレビュー"
        category    = "カテゴリ−１"
        category2   = "カテゴリ−2"
        category3   = "カテゴリ−3"

        context = {
                   "button1":button1,
                   "data":data,
                   "category1":category,
                   "category2": category2,
                   "category3": category3,

                   "designs":designs,

                   }

        return render(request,"illust/index.html",context)

    def post(self, request, *args, **kwargs):

        if "title" in request.POST:
            posted  = Design( title = request.POST["title"] )
            posted.save()

        return redirect("illust:index")

index   = illustView.as_view()
