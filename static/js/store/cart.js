$(function () {
    // hide the cart table on page load
    $("#cart_div").dialog({
        autoOpen: false,
    });

    cart_size();
});

// update cart quantity or replace
function update_quantity(status) {
    return status ? false : true;
}

const openCart = () => {
    const cart_size = $(".cart_size").text() + " ITEMS READY FOR POSTING";
    $("#cart_div")
        .dialog("open")
        .dialog({
            title: cart_size,
            height: 800,
            width: 1000,
            minHeight: 500,
            minWidth: 600,
            closeOnEscape: true,
        })
        .effect("shake", "fast");

    view_cart();
}; //end of function

// add item(s) to cart
//please check the receivingparameters
const addToCart = (pk,cart_name='cart') => {
    if (event.which == 13 || event.which == 32) {
        event.preventDefault();
        // product_price = price
        quantity = event.target.value;
        price = event.target.name;
        pk = pk;
        // const cart_name_ = $(event.target).attr("data-cart_name")
        // const cart_name = cart_session_name(cart_name_);

        // console.log(cart_name)

        // sessionStorage.setItem('cart_name', cart_name)

        url = `/cart/add/${cart_name}/`

        // console.log(url)

        // AJAX CALL START
        $.ajax({
            url: url,
            type: "POST",
            data: {
                id: pk,
                quantity: quantity,
                price: price,
                update_quantity: true,
                // cart_session_name: _cart_name,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
            },

            success: function (data) {
                // console.log("pk",pk)

                if (data) {
                    swallAlerts(
                        "value saved for posting",
                        "success",
                        "bottom-end",
                        1000,
                        false
                    );
                    // $('#products_cart').DataTable().ajax.reload();
                }

                view_cart(cart_name);
                cart_size(cart_name);


                console.log("session_name",cart_name)

                setTimeout(() => {
                    $(".add_to_cart").val("");
                }, 1000);
            },
        });

        // AJAX CALL END
    }

    //   });
};

// check if default cart variable else set new cart  name for django session
function cart_session_name(status) {
    return status ? status : "cart";
}

// list items in cart
function view_cart(cart_name='cart') {
    // const cart_name = sessionStorage.getItem('cart_name')
    url = `/cart/${cart_name}/`

    // console.log(url)
    var table = "";
    $.ajax({
        type: "GET",
        url: url,
        success: function (response) {
            for (var i in response) {
                count = +i + 1;
                table += "<tr>";

                table +=
                    `` +
                    `<td >` +
                    count +
                    `</td>` +
                    `<td >` +
                    response[i].name +
                    `</td>` +
                    `<td >` +
                    response[i].quantity +
                    `</td>` +
                    // + `<td >` + response[i].quantity_in_cart + `</td>`

                    `<td class="" placeholder="press enter or space to save">` +
                    `<input type="number" onKeyUp="addToCart(${response[i].pk},'cart')" data-cart_name="re_order"  name="${response[i].price}"  value="${response[i].quantity_in_cart}">` +
                    `</td>` +
                    `<td >` +
                    response[i].total +
                    `</td>` +
                    `<td class="trash_cart"   title="trash item" onclick="removeItemFromCart(${response[i].pk},'cart')">` +
                    `<i class="fa fa-trash  mx-4"   aria-hidden="true"></i>` +
                    `</td>`;

                table += "</tr>";
            }

            document.getElementById("cart_body").innerHTML = table;

            table = document.getElementById("cart_table");
        },
    });
}

// get cart size
const cart_size = (cart_name='cart') => {
    // const cart_name = sessionStorage.getItem('cart_name')
    $.get(`/cart/cart_length/${cart_name}`, function (data) {
        $(".cart_size").html(data.total_cart);

        $("#cart_div").dialog(
            "option",
            "title",
            `${data.total_cart} ITEMS READY FOR POSTING`
        );

        if (data.total_cart < 1) {
            document.getElementById("cart_post_btn").disabled = true;
        } else {
            document.getElementById("cart_post_btn").disabled = false;
        }
    }); //end of ajax
}; //end of function

// close the dialog box
const cart_close_btn = () => {
    $("#cart_div").dialog("close");
};

// live search on cart table
// live search on cart

$(document).ready(function () {
    $("#cart_items_search").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#cart_body  tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    });
});

function removeItemFromCart(item,cart_name='cart') {
    // console.log("cart_new",cart_name)
    // const cart_name = sessionStorage.getItem('cart_name')
    url = `/cart/remove/${item}/${cart_name}/`;
    $.ajax({
        url: url,
        type: "POST",
        data: {
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },

        success: function () {
            cart_size();
            swallAlerts(
                "Deleted" + " - " + "successfully",
                "success",
                "bottom-end",
                1000,
                false
            );
            view_cart();
        },
        error: function (jqXHR, textStatus, errorThrown) {
            // alert(textStatus + ' - ' + errorThrown);
            swallAlerts(
                textStatus + " - " + errorThrown,
                "error",
                "bottom-end",
                3000,
                false
            );
        },
    });
}



// post cart data
const post_cart = (cart_name='cart') => {
    $("#cart_div").dialog("close");

    $.ajax({
        url: `/cart/post_cart/${cart_name}/`,
        dataType: "json",
        type: "POST",
        data: {
            val: $(":input").serializeArray(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },

        success: function (response) {
            console.log(response.data)
            cart_size();
            swallAlerts(
                "Data saved" + " - " + "successfully",
                "success",
                "bottom-end",
                1000,
                false
            );
        },
        error: function (jqXHR, textStatus, errorThrown) {
            // alert(textStatus + ' - ' + errorThrown);
            swallAlerts(
                textStatus + " - " + errorThrown,
                "error",
                "bottom-end",
                3000,
                false
            );
        },
    });
}

