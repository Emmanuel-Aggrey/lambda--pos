

// populate list with generics

const get_cetegories = () => {
    
    $("#categories_div").fadeOut()
    generic_url= '//store/products-in-category/10/'
    
    category_url='/store/category-home/category-list/'
    $.get(category_url, function (data) {
        // console.log(data)
        // <span class="badge bg-primary rounded-pill">${value.get_total_category}</span>

        var arr = $.each(data, function (key, value) {
            
            return $("#myList").append(`
            <li class='list-unstyled list-group-item my-1 mx-4'  tittle='${value.description}' id=${value.pk} data-name='${value.name}'> ${value.name} 
            
             <i data-generic='${value.pk}' class="fa fa-edit edit_generic text-dark fx-3 " title="edit" aria-hidden="true" style="float: right;cursor:copy;"></i>

            </li>
            `)
           
        });
       

    });
}


// GET ALL GENERICS WHEN PAGE STARTS
$(function () {
    get_cetegories()
    edit_generic()
    // $("#products_div").fadeOut()
    // $( "#products_div" ).dialog({ autoOpen: true });
    
    
});





$(function () {

    // $("#myList ,li").click(function (e) {
        $('#myList').delegate('.list-group-item', 'click', function (e) {


        // $( "#products_div" ).dialog({ autoOpen: false });


        e.preventDefault();
        $("#categories_div").fadeIn()

        var category_id = $(e.target).attr('id');
        var data_name = $(e.target).attr('data-name');

        localStorage.setItem('category_id', category_id)
        sessionStorage.setItem('category_name', data_name)


        // const category_name = sessionStorage.getItem('category_name');

        $("#add_category_title").text(`ADD TO ${data_name}`).addClass("text-uppercase")

        // console.log("category_id", category_id, data_name)
            // url ="/store/products-in-category/10/";
        url = `/store/products-in-category/${category_id}/`,
            $.ajax({
                url: url,
                type: 'GET',

                success: function (response) {
                    console.log(response)
                    populateCategoryTable(response)

                },
                error: function (jqXHR, textStatus, errorThrown) {
                    // alert(textStatus + ' - ' + errorThrown);
                    // swallAlerts(textStatus + ' - ' + errorThrown, 'error', "bottom-end", 3000, false);

                }
            });


    });
});







const populateCategoryTable = (data) => {
    $("#items_search").focus();
    const category_name = sessionStorage.getItem('category_name');

    $("#categories_title").text(category_name)
    var table = "";

    for (var i in data) {
        // console.log(data)

        // console.log("data >",parseInt(i)+1)

        table += "<tr>";

        table += `<td>` + `${parseInt(i) + 1}` + `</td>`
            + `<td >` + data[i].name + `</td>`
            + `<td >` + data[i].description + `</td>`
            + `<td class="edit_category  btn btn-light btn-outline-info"  title="edit items" data-edit="${data[i].pk}">` + `<i class="fa fa-edit  mx-4" title="edit items" style="cursor:pointer"  aria-hidden="true"></i>` + `</td>`

            + `<td class="view_products btn btn-light btn-outline-primary" title="view data"  data-view="${data[i].pk}" data-product-name="${data[i].name}" >` + `<i  class="fa fa-eye mx-4 " style="cursor:pointer"  aria-hidden="true"></i>` + `</td>`



        table += "</tr>";
    }


    document.getElementById("categories_in_generics").innerHTML = table;

    table = document.getElementById("categories_table");
    const table_size = $(".view_products").length



    view_products_table()
    add_product()
    edit_category()

}




function edit_generic() {


    $('#myList').delegate('.edit_generic', 'click', function (ev) {

        $("#editGeneric").click();


        var category_id = $(this).attr('data-generic');
        localStorage.setItem('generic_id', category_id)
        console.log("category_id",category_id)
        // console.log("generic_id",generic_id)
        // generic_url =`/store/generic-home/generic-list/${generic_id}/`
        category_url =`/store/category-home/category-list/${category_id}/`
        $.get(category_url, function (data) {
            $("#generics_name_edit").val(data.name)
            $("#generics_description_edit").val(data.description)
            $("#categories_div").fadeOut()

            // console.log(data)

        });

    });//end of delegation
}//end of function








function add_product() {


    $('#categories_in_generics').delegate('.add_product', 'click', function () {

        var product_url = $(this).attr('data-add');

        console.log('add_product', product_url);

        // localStorage.setItem('product_id', product_id)


        $.ajax({
            type: 'GET',
            url: product_url,


            success: function (response) {
                console.log(response)


            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log(jqXHR, textStatus, errorThrown)

            }

        })//end of ajax
    });//end of delegation
}//end of function





function view_products_table(event) {


    $('#categories_in_generics').delegate('.view_products', 'click', function () {
        const category_name = sessionStorage.getItem('category_name');
        var product_name = $(this).attr('data-product-name');
        products = category_name+' > '+product_name
        // $( "#products_div" ).dialog( "open" ).dialog({
           
        //     title: (products),
        //     height:800,
        //     width:1450,
        //     minHeight: 900,
        //     minWidth: 1300,
            
        // })//.effect('shake','fast');
        


        // $("#products_div").fadeIn()
        var products_url = $(this).attr('data-view');
      


        // console.log(products_url)
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



function edit_category() {

    $('#categories_in_generics').delegate('.edit_category', 'click', function () {

        $("#editCategory").click()

        // $( "#products_div" ).dialog( "close" );
        

        var category_url = $(this).attr('data-edit');
        // /store/category-home/category-list/3/


        console.log('category_url', category_url);

        localStorage.setItem('category_url', category_url);

        $.ajax({
            type: 'GET',
            url: `/store/category-home/category-list/${category_url}/`,


            success: function (data) {
                // console.log(data)
                $("#category_name_edit").val(data.name);
                $("#category_description_edit").val(data.description)
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

function view_category() {
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

                populateCategoryTable(response)
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
        $("#categories_in_generics  tr").filter(function () {
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
        window.open('/store/products/','', 'width=800,height=800','true')
        }
        

