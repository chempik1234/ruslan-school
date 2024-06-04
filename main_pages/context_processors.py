from .models import News


def default_context(request):
    return {
        'company_address': "123456, респ. Башкортостан, г. Туймазы, ул. Уличная, д. 1",
        'company_phone': "+7 (999) 777-77-77",
        "company_email": "school0@email.ru",
        "company_name": "МБОУ средняя общая образовательная школа №0 г.Туймазы",
        "news": News.objects.all()
        # "side_pictures":
    }
