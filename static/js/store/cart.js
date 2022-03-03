$(function () {

    // hide the cart table on page load
    $("#cart_div").dialog({
        autoOpen: false,
    });

    cart_size()



})

const openCart = () => {
    const cart_size = $(".cart_size").text() + ' ITEMS READY FOR POSTING'
    $("#cart_div").dialog("open").dialog({

        title: (cart_size),
        height: 800,
        width: 1000,
        minHeight: 500,
        minWidth: 600,
        closeOnEscape: true,

    }).effect('shake', 'fast');


    view_cart()

}//end of function

// add item(s) to cart
const addToCart = (price) => {


    if (event.which == 13 || event.which == 32) {
        event.preventDefault();
        product_price = price
        quantity = event.target.value
        id = event.target.name
        // AJAX CALL START
        $.ajax({
            url: '/cart/add/',
            type: 'POST',
            data: {
                id: id,
                quantity: quantity,
                price: price,
                update_quantity: true,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },

            success: function (data) {

                if (data) {
                    swallAlerts('value saved for posting', 'success', "bottom-end", 1000, false);
                    // $('#products_cart').DataTable().ajax.reload();
                }

                view_cart()
                cart_size()

                setTimeout(() => {

                    $('.add_to_cart').val('')

                }, 1000);

            }

        });

        // AJAX CALL END
    }

    //   });
}

// list items in cart
function view_cart() {
    var table = "";
    $.ajax({
        type: 'GET',
        url: `/cart/`,
        success: function (response) {

            for (var i in response) {

                count = +i + 1
                table += "<tr>";

                table += ``
                    + `<td >` + count + `</td>`
                    + `<td >` + response[i].name + `</td>`
                    + `<td >` + response[i].quantity + `</td>`
                    + `<td >` + response[i].quantity_in_cart + `</td>`
                    + `<td >` + response[i].variance + `</td>`
                    + `<td class="trash_cart"  title="trash item" onclick="removeItemFromCart(${response[i].pk})">` + `<i class="fa fa-trash  mx-4"   aria-hidden="true"></i>` + `</td>`

                table += "</tr>";
            }

            document.getElementById("cart_body").innerHTML = table;

            table = document.getElementById("cart_table");
        }
    })

}

// get cart size
const cart_size = () => {

    $.get("/cart/cart_length/", function (data) {
        $(".cart_size").html(data.total_cart);

        $("#cart_div").dialog("option", "title", `${data.total_cart} ITEMS READY FOR POSTING`);

        if (data.total_cart < 1) {
            document.getElementById("cart_post_btn").disabled = true;
        }
        else {
            document.getElementById("cart_post_btn").disabled = false;
        }


    });//end of ajax

}//end of function

// close the dialog box
const cart_close_btn = () => {
    $("#cart_div").dialog("close")
}

// live search on cart table
// live search on table

$(document).ready(function () {
    $("#cart_items_search").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#cart_body  tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});


function removeItemFromCart(item) {

    url = `/cart/remove/${item}/`;
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },

        success: function () {

            cart_size()
            swallAlerts('Deleted' + ' - ' + 'successfully', 'success', "bottom-end", 1000, false);
            view_cart()


        },
        error: function (jqXHR, textStatus, errorThrown) {
            // alert(textStatus + ' - ' + errorThrown);
            swallAlerts(textStatus + ' - ' + errorThrown, 'error', "bottom-end", 3000, false);

        }
    })

}