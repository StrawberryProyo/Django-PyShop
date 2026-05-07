from django.http import HttpResponse
from django.utils.html import escape
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all().order_by('prodname')
    items = []
    for product in products:
        items.append(
            "<article style='background:#fff;border:1px solid #e5e7eb;border-radius:10px;padding:1rem;margin-bottom:0.8rem;display:grid;grid-template-columns:120px 1fr;gap:1rem;align-items:start;'>"
            f"<div style='width:120px;height:120px;border-radius:10px;overflow:hidden;background:#f3f4f6;border:1px solid #e5e7eb;'>"
            f"<img src='{escape(product.image_url)}' alt='{escape(product.prodname)}' style='width:100%;height:100%;object-fit:cover;display:block;' loading='lazy'>"
            "</div>"
            "<div>"
            f"<h2 style='margin:0 0 0.4rem;'>{escape(product.prodname)}</h2>"
            f"<p style='margin:0 0 0.6rem;color:#4b5563;'>{escape(product.description)}</p>"
            f"<div>Price: ${escape(str(product.price))}</div>"
            f"<div>Stock: {escape(str(product.stock))}</div>"
            "</div>"
            "</article>"
        )

    if not items:
        items_html = "<div style='padding:1rem;border:1px dashed #cbd5e1;border-radius:8px;background:#fff;'>No products yet. Add one in admin to see it here.</div>"
    else:
        items_html = "".join(items)

    html = (
        "<!DOCTYPE html>"
        "<html lang='en'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'>"
        "<title>Products</title></head>"
        "<body style='font-family:Segoe UI,Tahoma,Verdana,sans-serif;margin:0;padding:2rem;background:#f7f8fa;color:#222;'>"
        "<main style='max-width:900px;margin:0 auto;'>"
        "<h1 style='margin-top:0;'>Product List</h1>"
        f"{items_html}"
        "</main></body></html>"
    )
    return HttpResponse(html)