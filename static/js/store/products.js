const populateProductTable = (data) => {
    $("#items_search").focus();
    const category_name = sessionStorage.getItem('category_name');

    $("#categories_title").text(category_name)
    var table = "";

    for (var i in data) {


        var arr = $.each(data[i].supplier, function (key, value) {
            // console.log(value)

        })
        table += "<tr>";

        table += `<td>` + `${parseInt(i) + 1}` + `</td>`
            + `<td >` + data[i].name + `</td>`
            + `<td >` + data[i].price + `</td>`
            + `<td >` + data[i].quantity + `</td>`
            + `<td >` + data[i].description + `</td>`
            + `<td >` + convertNullValues(data[i].unit_name) + `</td>`
            + `<td >` + data[i].supplier + `</td>`
            + `<td >` + data[i].stock_level + `</td>`
            + `<td >` + data[i].original_stock + `</td>`
            + `<td >` + convertNullValues(data[i].shelf_number) + `</td>`
            + `<td >` + has_expire_date_(data[i].has_expire_date) + `</td>`
            + `<td >` + convertNullValues(data[i].expire_date) + `</td>`
            + `<td >` + data[i].months_to_expire + `</td>`
            + `<td >` + has_expired(data[i].has_expired) + `</td>`
            + `<td class="edit_product  btn btn-light btn-outline-info"  title="edit items" onclick="getProduct(${data[i].pk})"  data-edit-product="${data[i].pk}">` + `<i class="fa fa-edit  mx-4"  style="cursor:pointer"  aria-hidden="true"></i>` + `</td>`

        + `<td class="">` + `<input type="text" class="add_to_cart" name="${data[i].pk}"  onKeydown="addToCart(${data[i].price})"  style="width:100%;">` + `</td>`

        // + `<td class="view_products btn btn-light btn-outline-primary" title="a items" data-add="${data[i].get_absolute_url}" >` + `<i  class="fa fa-plus mx-4 " style="cursor:pointer"  aria-hidden="true"></i>` + `</td>`

        // + `<td class="add_product  btn-sm  btn-outline-info" data-view="${data[i].get_absolute_url}">` + `<i class="fa fa-plus my-2 mx-4" title="add new item" style="color:red;cursor:pointer"  aria-hidden="true"></i>` + `</td>`


        table += "</tr>";
    }


    document.getElementById("products_in_categories").innerHTML = table;

    table = document.getElementById("products_table");
    const table_size = $(".view_products").length
    // console.log("table_size",table_size)


    // view_products()
    // add_product()
    // edit_category()
    loadUnit()
    loadSupliers()
    exitModelAdd()
 

}



function has_expire_date_(status) {
    return (status ? 'YES' : 'NO');
}

function has_expired(expired) {
    if (expired === true) {
        return 'YES'
    }
    else if (expired === false) {
        return 'NO'
    }
    else {
        return 'No Expire Date'
    }

}

function convertNullValues(status) {
    return (status ? status : '')
}

// get data into product table after ajax call on add or edit

const displayProductTable = (category_id) => {


    $.ajax({
        
        url: `/store/products-in-category/${category_id}/`,
        type: 'GET',

        success: function (response) {

            populateProductTable(response)
            // console.log(response)

        },
        error: function (jqXHR, textStatus, errorThrown) {
            // alert(textStatus + ' - ' + errorThrown);
            swallAlerts(textStatus + ' - ' + errorThrown, 'error', "bottom-end", 3000, false);

        }
    });

}


function getProduct(product_id) {
    // $('#products_in_categories').delegate('.edit_product', 'click', function () {
    $("#editProductBtn").click();
    // $(".inputUnit").empty()
    // $(".inputSupplier").empty()
    // var product_id = $(this).attr('data-edit-product');

    console.log('product_id', product_id)
    sessionStorage.setItem('product_id', product_id);


    $.ajax({
        type: 'GET',
        url: `/store/product-home/product-list/${product_id}/`,


        success: function (data) {
            // console.log(data.name,data.unit)
            // var unit = $("#inputUnitEdit").prop('selectedIndex', data.unit)
            // console.log("supplier", data.supplier)

            $('#inputnameEdit').val(data.name),
                $('#inputPriceEdit').val(data.price),
                $("#inputDescriptionEdit").val(data.description),
                $('#inputQuantityEdit').val(data.quantity),
                $('#inputUnitEdit').val(data.unit),

                // $('#inputSupplierEdit').val(data.supplier),


                $("#inputSupplierEdit option").prop("selected", function () {
                    return ~$.inArray(this.text, data.supplier);
                });

            $('#inputStockLevelEdit').val(data.stock_level),
                $("#inputShelfNumberEdit").val(data.shelf_number),
                $("#inputMonthsToExpireEdit").val(data.months_to_expire),

                $('#inputHasExpireDateEdit').prop('checked', data.has_expire_date)
            // console.log('has_expire_date',data.has_expire_date)
            has_expire_date(data.has_expire_date)


            $("#inputExpireDateEdit").val(data.expire_date)


        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(jqXHR, textStatus, errorThrown)

        }

    })//end of ajax       

    // })
}


// add to cart
// space = 32, enter= 13



const addToCart = (price) => {
    // $('.add_to_cart').keypress(function( event ) {

        
        if ( event.which == 13 || event.which ==32) {
            event.preventDefault();
             product_price = price
             quantity =  event.target.value
             id = event.target.name
            // AJAX CALL START
            $.ajax({
                url: '/cart/add/',
                type: 'POST',
                data: {
                    id:id,
                    quantity:quantity,
                    price:price,
                    update_quantity:true,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    
                },
    
                success: function (data) {
                   

                    // console.log('product_price =', product_price,'quantity = ',quantity,'id= ',id);

                    if (data) {
                        swallAlerts('saved for posting', 'success', "bottom-end", 3000, false);
                         console.log(data)
                        $('#products_cart').DataTable().ajax.reload();
                    }
                    setTimeout(() => {
                        // console.log(this)
                        // console.log($($`.add_to_cart id{}`).val(''))

                        
                    }, 2000);
    
                }
    
            });
    


            // AJAX CALL END
        }
      
    //   });
}



// load unit of measurements to select field

const loadUnit = () => {
    $(".inputUnit").empty()


    $(".inputUnit").css('width', '370', 'height', '100').addClass('form-control')
    $.get("/store/unit-home/units/", function (data) {

        for (var index in data.data) {

            $('.inputUnit').append('<option value="' + data.data[index].id + '">' + data.data[index].unit + '</option>');
            // $('#inputUnitEdit').append('<option value="' + data.data[index].id + '">' + data.data[index].unit + '</option>');


            $("#inputUnit").select2({
                placeholder: 'Select Unit',
                dropdownParent: $('#modelProductAdd'),

            });
            // $("#inputUnitEdit").select2({
            //     placeholder: 'Select Unit',
            //     dropdownParent: $('#modelProductEdit')

            // });'

        }

    });
}

// load supliers  to select field

const loadSupliers = () => {
    $(".inputSupplier").css('width', '370', 'height', '100').addClass('form-control')
    $(".inputSupplier").empty()
    $.get("/business/all-supliers/", function (data) {

        for (var index in data.data) {
            // console.log(data.data)

            $('.inputSupplier').append('<option value="' + data.data[index].id + '">' + data.data[index].name + '</option>');
            // $('#inputSupplierEdit').append('<option value="' + data.data[index].id + '">' + data.data[index].name + '</option>');


            $("#inputSupplier").select2({
                placeholder: 'Select Suppliers',
                dropdownParent: $('#modelProductAdd'),

            });
            // $("#inputSupplierEdit").select2({
            //     placeholder: 'Select Suppliers',
            //     dropdownParent: $('#modelProductEdit')

            // });

        }
    });

}



// closs product table on escape key press



const exitModelAdd = () => {
    $(document).keydown(function (event) {
        // const isOpen = $("#products_div").dialog("isOpen");
        const isShown = $("#modelProductAdd").hasClass("show");
        // console.log(isOpen,isShown)

        if (event.keyCode === 27 & isOpen & isShown) {

            console.log(isOpen, isShown)

        }
        else if (event.keyCode === 27 & isOpen) {
            console.log(isOpen, isShown)
            // $("#products_div").dialog("close");

        }

    })
}

// check if product has a expire  date

function has_expire_date(status) {

    if (status) {
        // console.log(status)
        $("#months_to_expireEdit").fadeIn()

        $("#expireDateColEdit").fadeIn()
    }
    else {
        console.log('status', status)
        $("#months_to_expireEdit").fadeOut()
        $("#inputMonthsToExpireEdit").val('')
        $("#expireDateColEdit").fadeOut()
        $("#inputExpireDateEdit").val('')
    }
    $("#has_expire_dateEdit").on("click", function () {
        expire_date = $('#inputHasExpireDateEdit').is(':checked')
        if (expire_date) {
            console.log('if ', expire_date)
            $("#months_to_expireEdit").fadeOut()
            $("#inputMonthsToExpireEdit").val('')
            $("#expireDateColEdit").fadeOut()
            $("#inputExpireDateEdit").val('')
        }
        else {
            console.log('else', expire_date)
            $("#months_to_expireEdit").fadeIn()

            $("#expireDateColEdit").fadeIn()

        }

    })

}





// live search on table
$(document).ready(function () {



    $("#product_search").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#products_in_categories  tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});


