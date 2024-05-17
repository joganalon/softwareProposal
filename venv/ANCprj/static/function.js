//adding review
console.log("working fine");

const monthNames = [
    "Jan","Feb","Mar","Apr","May","June",
    "July","Aug","Sept","Oct","Nov","Dec"
];

$("#review-form").submit(function(e){
    e.preventDefault();

    let dt=new Date();
    let time=dt.getDate() + " "+monthNames[dt.getUTCMonth]+" "+dt.getFullYear();

    $.ajax({
        data:$(this).serialize(),
        method:$(this).attr("method"),
        url:$(this).attr("action"),
        dataType: "json",
        success:function(response){
            console.log("CommentSaved to db");

            if(response.bool == true){
                $("#review-rsp").html("Review Added Successfully.")
                $(".hide-comment-form").hide()
                $(".add-review").hide()

                let _html='<h4>'+response.context.user+'</h4>'
                    _html+='<h6>'+time+'</h6>'
                    for(let i=1;i<response.context.rating;i++){
                        _html+='<i>*</i'
                    }
                    _html+='<p>'+response.context.review+'<p>'                 
                    $(".comment-list").prepend(_html)
            }
            
        }
    })
})

//add to order functionality
$("#add-to-orders").on("click", function(){
    let quantity=$("#product-quantity").val()
    let product_title=$(".product-title")
    let product_id=$(".product-id").val()
    let product_price=$("#current-product-price").text()
    let this_val=$(this)
    
    console.log("Quantity:", quantity);
    console.log("Title:", product_title);
    console.log("Price:", product_price);
    console.log("ID:", product_id);
    console.log("Current Element:", this_val);

    $.ajax({
        url:'/add-to-orders',
        data:{
            'id':product_id,
            'qty':quantity,
            'title':product_title,
            'price':product_price
        },
        dataType: 'json',
        beforeSend: function(){
            console.log("Adding product to orders...");
        },
        success: function(response){
            this_val.html("item added to orders")
            console.log("Added product to orders");
            $(".order-items.counts").text(response.totaloderitems)

        }
    })
})


//filter by foodgroup, categories, vendors, price
$(document).ready(function(){
    $(".filter-checkbox, #price-filter-btn").on("click", function(){
        console.log("a checkbox has been clicked");

        let filter_object = {}

        let min_price= $("#max_price").attr("min")
        let max_price= $("#max_price").val()

        filter_object.min_price=min_price;
        filter_object.max_price=max_price;


        $(".filter-checkbox").each(function(){
            let filter_value = $(this).val()
            let filter_key = $(this).data("filter")

            console.log("Filter value os:", filter_value);
            console.log("Filter key is:", filter_key);

            filter_object[filter_key]=Array.from(document.querySelectorAll('input[data-filter='+filter_key+']:checked')).map(function(element){
                return element.value
            })
        })
        console.log("Filter objects is: ", filter_object);
        $.ajax({
            url:'/filter-products',
            data: filter_object,
            dataType: 'json',
            beforeSend:function(){
                console.log("trying to filter product...");
            },
            success:function(response){
                console.log(response);
                console.log("data filtered successfully...");
                $("#filtered-products").html(response.data)
            }
        })
    })
    $("#max_price").on("blur", function(){
        let min_price=$(this).attr("min")
        let max_price=$(this).attr("max")
        let current_price=$(this).val()

       // console.log("current price is: ", current_price);
        //console.log("max price is: ", max_price);
        //console.log("min price is: ", min_price);

        if(current_price<parseInt(min_price)||current_price>parseInt(max_price)){
           // console.log("error occured");

            min_price = Math.round(min_price*100)/100
            max_price = Math.round(max_price*100)/100

            //console.log("##################################");
            //console.log("Max price is: ", max_Price);
          //  console.log("Min price is: ", min_Price);

          alert("price must be between: " + min_price + " and "+max_price)
          $(this).val(min_price)
          $("#range").val(min_price)
          $(this).focus()
          return false
        }
    })
})



