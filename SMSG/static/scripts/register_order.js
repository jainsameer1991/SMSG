$(document).ready(function(){
    $('#buyStockButton').click(function(){
        var symbol = $('#stockSymbol').html();
        var quantity = $('#quantityField').val();
        var price = $('#totalPrice').val();
        $.ajax({
            type: "GET",
            url: '/orderbook/registerorder/',
            method: 'GET',
            dataType: 'json',
            async:false,
            cache: false,
            data:{
                'symbol': symbol,
                'quantity': quantity,
                'price': price,
            },
            success: function(data) {
               $('#bg-modal').css('display','none');
                var trs = $("#stocklist").find("tbody>tr");
                trs.each(function(){
                    if($(this).hasClass("inBuyState")){
                        $(this).removeClass("inBuyState");
                    }
                });
                $('.alert-success').css('display','block');
                window.setTimeout(function() {
                    $(".alert").fadeTo(500, 0).slideUp(500, function(){
                        $(this).remove();
                    });
                }, 1000);

                $('.toast').toast('show');
            },
            error: function(data) {
                alert(data);
            }
        });
    });
});