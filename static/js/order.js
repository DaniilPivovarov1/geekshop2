let _quantity, _price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost;
let quantity_arr = [];
let price_arr = [];

let TOTAL_FORMS = parseInt(document.querySelector('input[name="orderitems-TOTAL_FORMS"]').value);

let order_total_quantity = parseInt(document.querySelector('.order_total_quantity').textContent) || 0;
let order_total_cost = parseFloat(document.querySelector('.order_total_cost').textContent.replace(',', '.')) || 0;

for (let i = 0; i < TOTAL_FORMS-1; i++) {
    _quantity = parseInt(document.querySelector('input[name="orderitems-' + i + '-quantity"]').value);
    _price = parseFloat(document.querySelector('.orderitems-' + i + '-price').textContent.replace(',', '.'));
    quantity_arr[i] = _quantity;
    if (_price) {
        price_arr[i] = _price;
    } else {
        price_arr[i] = 0;
    }
}
if (!order_total_quantity) {
    for (let i = 0; i < TOTAL_FORMS-1; i++) {
        order_total_quantity += quantity_arr[i];
        order_total_cost += quantity_arr[i] * price_arr[i];
    }
    document.querySelector('.order_total_quantity').innerHTML = order_total_quantity.toString();
    document.querySelector('.order_total_cost').innerHTML = Number(order_total_cost.toFixed(2)).toString();
}

document.querySelector('.order_form').querySelectorAll('input[type="number"]').forEach(function (inp) {
    inp.addEventListener('click', function (event) {
        let target = event.target;
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''));
        if (price_arr[orderitem_num]) {
            orderitem_quantity = parseInt(target.value);
            delta_quantity = orderitem_quantity - quantity_arr[orderitem_num];
            quantity_arr[orderitem_num] = orderitem_quantity;
            orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
        }
    })
});

document.querySelector('.order_form').querySelectorAll('input[type="checkbox"]').forEach(function (inp) {
    inp.addEventListener('click', deleteOrderItem)
});

function orderSummaryUpdate(orderitem_price, delta_quantity) {
    delta_cost = orderitem_price * delta_quantity;

    order_total_cost = Number((order_total_cost + delta_cost).toFixed(2));
    order_total_quantity = order_total_quantity + delta_quantity;

    document.querySelector('.order_total_cost').innerHTML = order_total_cost.toString();
    document.querySelector('.order_total_quantity').innerHTML = order_total_quantity.toString();
}

$('.formset_row').formset({
   addText: 'добавить продукт',
   deleteText: 'удалить',
   prefix: 'orderitems',
   removed: deleteOrderItem
})

function deleteOrderItem(row) {
   let target_name = row[0].querySelector('input[type="number"]').name;
   orderitem_num = parseInt(target_name.replace('orderitems-', '').replace('-quantity', ''));
   delta_quantity = -quantity_arr[orderitem_num];
   orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
}
