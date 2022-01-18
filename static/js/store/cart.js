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
        height: 500,
        width: 600,
        minHeight: 500,
        minWidth: 600,

    }).effect('shake', 'fast');

    view_cart()

}


function view_cart() {
    var table = "";
    $.ajax({
        type: 'GET',
        url: `/cart/`,
        success: function (response) {


            for (var i in response) {

                // console.log("data >",parseInt(i)+1)

                table += "<tr>";



                table += ``
                    + `<td >` + parseInt(i) + `</td>`
                    + `<td >` + response[i].name + `</td>`
                    + `<td >` + response[i].quantity + `</td>`
                    + `<td >` + response[i].quantity_in_cart + `</td>`
                    + `<td >` + response[i].variance + `</td>`



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
        const cart_zize = $(".cart_size").html(data.total_cart);
        return cart_zize.text()
    });

}
