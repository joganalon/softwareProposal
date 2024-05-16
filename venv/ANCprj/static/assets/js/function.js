//adding review
console.log("working fine");

$("#review-from").submit(function(e){
    e.preventDefault();

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

                let _html=
            }
        }
    })
})

//add to order functionality
$("#add-to-cart-btn").on("click", function(){
    let quantity=$("#product-quantity").val()
    let product_title=$(".product-title")
    let product_id=$(".product.id").val()
    let product_price=$(".current-product-price").text()
    let this_val=$(this)
    
    console.log("Quantity:", quantity);
    console.log("Title:", product_title);
    console.log("Price:", product_price);
    console.log("ID:", product_id);
    console.log("Current Element:", this_val);
})