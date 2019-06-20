$(document).ready(function(){
    $('#quantityField').keyup(function(){
        var quantity = $(this).val();
        var trs = $("#stocklist").find("tbody>tr");
        trs.each(function(){
            if($(this).hasClass("inBuyState")){
                var tds = $(this).find('td');
                $('#quantitySpan').html(quantity);
                $('.stockPrice').val(parseFloat(parseFloat(tds.eq(1).html()) * parseFloat(quantity)).toFixed(2));
            }
        });
    });

    $('.buyButton').click(function(){
        var item = $(this).closest("tr");
        var tds = item.find('td');

        $('#stockSymbol').html(tds.eq(0).html());
         $('.stockPriceSpan').html(tds.eq(1).html());
        $('.stockPrice').val(parseFloat(parseFloat(tds.eq(1).html()) * parseFloat($('#quantityField').val())).toFixed(2));
        $('#bg-modal').css('display','flex');

        item.addClass("inBuyState");

    });

    $('.closeBuyDialog').click(function(){
        $('#bg-modal').css('display','none');
        var trs = $("#stocklist").find("tbody>tr");
        trs.each(function(){
            if($(this).hasClass("inBuyState")){
                $(this).removeClass("inBuyState");
            }
        });
    });
});
