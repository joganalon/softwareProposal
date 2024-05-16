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