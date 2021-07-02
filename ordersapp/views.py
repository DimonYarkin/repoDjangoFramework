
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from basketapp.models import Basket
from ordersapp.forms import OrderItemForm
from ordersapp.models import Order, OrderItem


class OrderList(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderCreate(CreateView):
    pass
    # model = Order
    # fields = []
    # success_url = reverse_lazy('ordersapp:orders_list')
    # OrderFormSet = inlineformset_factory(Order,
    #                                      OrderItem,
    #                                      form=OrderItemForm,
    #                                      extra=1)
    #
    # basket_items = Basket.get_items(self.request.user)
    # if len(basket_items):
    #    OrderFormSet = inlineformset_factory(Order,
    #                                         OrderItem,
    #                                         form=OrderItemForm,
    #                                         extra=len(basket_items))
    #    formset = OrderFormSet()
    #    for num, form in enumerate(formset.forms):
    #        form.initial['product'] = basket_items[num].product
    #        form.initial['quantity'] = basket_items[num].quantity
    #    basket_items.delete()
    # else:
    #    formset = OrderFormSet()


class OrderUpdate(UpdateView):
    pass


class OrderDelete(DeleteView):
    pass


class OrderRead(DetailView):
    pass


def forming_complete(request, pk):
    pass
