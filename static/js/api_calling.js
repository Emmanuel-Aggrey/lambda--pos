    // $(document).ready(function () {

    
    //     //
    //     get_cart_size()

 

    // function populateTable(data) {
    //     var table = "";

    //     for (var i in data) {
    //         table += "<tr>";
    //         table += `<td id='${data[i].id}'>` + data[i].name + "</td>"
    //             + `<td>` + `<input type="number" class="form-control quantity">` + `</td>`
    //             + `<td class="btn btn-light btn-outline-dark" id="${data[i].id}s">` + 'save' + `</td>`;
    //         table += "</tr>";
    //     }

    //    document.getElementById("result").innerHTML = table;




    //     table = document.getElementById("products");
    //     var rows = table.rows;
    //     for (var i = 1; i < rows.length; i++) {

    //         rows[i].cells[2].onclick = function (ev) {

    //             // console.log('i is ',i)
    //             ev.preventDefault()
    //             id = ev.target.previousElementSibling.previousElementSibling.id;
    //             quantity =document.getElementById(id).nextElementSibling.children[0].value
    //             // console.log("id ",id, "quantity ",quantity)
                
    //             document.getElementById(id).nextElementSibling.children[0].value=''
    //             saveToCart(id,quantity)
              

    //         }
        
    //     }
    // }


    // function saveToCart(id,quantity) {
    // order_number ='{{request_.order_number}}'
    // order_id='{{request_.id}}'
    // // console.log(order_number,order_id)
   
    // product =id
  
     
    //   $.ajax({
    //     type: 'POST',
    //     url: `/requestitem/${order_number}/${order_id}/`,

    //     data: {
    //       product: product,
    //       quantity: quantity,
    //       csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    //     },
    //     beforeSend: function(){
    //         console.log("saving")
         

    //     },
    //     success: function () {
    //         // SuccessMessage('Saved To Cart')


    //     },
    //     error: function (jqXHR, textStatus, errorThrown) {

    //     //  alert( textStatus + ' - ' + errorThrown);
    //     //  ErrorMessage('error please try again ' +textStatus + ' - ' + errorThrown)

    //  }

    // })
    // }
    // })





function callApi() {

   
    $(document).ready(function() {
        $('#employees_table').DataTable( {
            "ajax": "/static/js/json.txt",
            "columns": [
                { "data": "name" },
                { "data": "position" },
                { "data": "office" },
                { "data": "extn" },
                { "data": "start_date" },
                { "data": "salary" }
            ]
        } );
    } );


}

