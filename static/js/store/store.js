// populate list with cetegories response

const get_cetegories = () => {

    category_url = '/store/category-home/category-list/'
    $.get(category_url, function (data) {


        var arr = $.each(data, function (key, value) {

            return $("#myList").append(`
            <li class='list-unstyled list-group-item my-1 mx-4'  tittle='${value.description}' id=${value.pk} data-name='${value.name}'> ${value.name} 
            
             <i data-category='${value.pk}' class="fa fa-edit edit_category text-dark fx-3 " title="edit" aria-hidden="true" style="float: right;cursor:copy;"></i>

            </li>
            `)


        });

    });
}


// GET ALL CATEGORIES WHEN PAGE STARTS
$(function () {
    get_cetegories()
    edit_category()
    $("#search_div").fadeOut()


});

$(function () {

    // $("#myList ,li").click(function (e) {
    $('#myList').delegate('.list-group-item', 'click', function (e) {

        e.preventDefault();
        $("#search_div").fadeIn();
        $( "#cart_div" ).dialog( "close" )



        var category_id = $(e.target).attr('id');
        var data_name = $(e.target).attr('data-name');

        localStorage.setItem('category_id', category_id)
        sessionStorage.setItem('category_name', data_name)



        $("#add_category_title").text(`ADD TO ${data_name}`).addClass("text-uppercase")


        url = `/store/products-in-category/${category_id}/`,
            $.ajax({
                url: url,
                type: 'GET',

                success: function (response) {
                    populateProductTable(response)

                },
                error: function (jqXHR, textStatus, errorThrown) {
                    // alert(textStatus + ' - ' + errorThrown);
                    // swallAlerts(textStatus + ' - ' + errorThrown, 'error', "bottom-end", 3000, false);

                }
            });

    });
});


const populateProductTable = (data) => {
    $("#items_search").focus();
    const category_name = sessionStorage.getItem('category_name');

    $("#product_title").text(category_name)
    var table = "";

    for (var i in data) {


        table += "<tr>";

        table += ``
            + `<td >` + data[i].name + `</td>`
            + `<td >` + data[i].price + `</td>`
            + `<td >` + data[i].quantity + `</td>`
            + `<td >` + data[i].description + `</td>`
            + `<td >` + convertNullValues(data[i].unit_name) + `</td>`
            + `<td >` + data[i].supplier + `</td>`
            // + `<td >` + data[i].stock_level + `</td>`
            // + `<td >` + data[i].original_stock + `</td>`
            + `<td >` + convertNullValues(data[i].shelf_number) + `</td>`
            // + `<td >` + has_expire_date_(data[i].has_expire_date) + `</td>`
            // + `<td >` + convertNullValues(data[i].expire_date) + `</td>`
            // + `<td >` + data[i].months_to_expire + `</td>`
            // + `<td >` + has_expired(data[i].has_expired) + `</td>`
            + `<td class="edit_product  btn btn-light btn-outline-info"  title="edit items" onclick="getProduct(${data[i].pk})"  data-edit-product="${data[i].pk}">` + `<i class="fa fa-edit  mx-4"  style="cursor:pointer"  aria-hidden="true"></i>` + `</td>`

            + `<td class="" placeholder="press enter or space to save">` + `<input type="number" placeholder='quantity' class="add_to_cart" name="${data[i].pk}"  onKeyUp="addToCart(${data[i].price})"  style="width:100%;">` + `</td>`



        table += "</tr>";
    }


    document.getElementById("products_in_categories").innerHTML = table;

    table = document.getElementById("categories_table");
    const table_size = $(".view_products").length



    view_products_table()

}

function edit_category() {


    $('#myList').delegate('.edit_category', 'click', function (ev) {

        $("#editGeneric").click();


        var category_id = $(this).attr('data-category');
        sessionStorage.setItem('category_id', category_id)

        category_url = `/store/category-home/category-list/${category_id}/`
        $.get(category_url, function (data) {
            $("#generics_name_edit").val(data.name)
            $("#generics_description_edit").val(data.description)


        });


    });//end of delegation


}//end of function

function view_products_table(event) {


    $('#products_in_categories').delegate('.view_products', 'click', function () {
        const category_name = sessionStorage.getItem('category_name');
        var product_name = $(this).attr('data-product-name');
        products = category_name + ' > ' + product_name
       
        var products_url = $(this).attr('data-view');

        localStorage.setItem('category_url', products_url);

        $.ajax({
            type: 'GET',
            url: `/store/products-in-category/${products_url}/`,


            success: function (response) {
                populateProductTable(response)
                // console.log(response)

            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log(jqXHR, textStatus, errorThrown)

            }

        })//end of ajax
    });//end of delegation
}//end of function


function add_category() {
    order_number = '{{request_.order_number}}'
    // console.log("order_number",order_number)
    $.ajax({
        type: 'GET',
        url: `/get_requisition_size/${order_number}/`,
        success: function (response) {
            $('#cart_size').text(response.cartlen_in + ' Items View ')
            // console.log("cart sixe ", response.cart_len)

        }
    })

}


// get data into category table after ajax call on add or edit

const displayCategoryTable = (category_id) => {

    url = `/store/category-in-generics/${category_id}/`,
        $.ajax({
            url: url,
            type: 'GET',

            success: function (response) {

                populateProductTable(response)
                console.log(response)

            },
            error: function (jqXHR, textStatus, errorThrown) {
                // alert(textStatus + ' - ' + errorThrown);
                swallAlerts(textStatus + ' - ' + errorThrown, 'error', "bottom-end", 3000, false);

            }
        });

}

// live search on table

$(document).ready(function () {
    $("#items_search").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#products_in_categories  tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});


// live search on list

$(document).ready(function () {
    $("#myInput").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#myList li").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});


// open all products in generic page
function openProdcuts() {
    window.open('/store/products/', '', 'width=1000,height=900', 'true')
}








