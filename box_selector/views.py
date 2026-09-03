from django.shortcuts import render, get_object_or_404
from .models import Product, Box
from .services import recommend_box


def recommend(request):
    result = None
    selected_product = None

    if request.method == "POST":
        product_id = request.POST.get("product")

        if product_id:
            selected_product = get_object_or_404(
                Product,
                id=product_id
            )

            boxes = Box.objects.all()

            result = recommend_box(
                selected_product,
                boxes
            )

    products = Product.objects.all()

    return render(
        request,
        "box_selector/recommend.html",
        {
            "products": products,
            "result": result,
            "selected_product": selected_product,
        }
    )