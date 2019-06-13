$(document).ready(function(){
    var trs = $("#stocklist").find("tbody>tr");
    setInterval(updateStockList,10000);
    function updateStockList(){
    	$.ajax({
	        type: "GET",
	        url: '/fetchvals/',
	        method: 'GET',
	        dataType: 'json',
	        async:false,
	        cache: false,
	        success: function(data) {
			    $('.classForHoverEffect').each(function(i){
			        trs.eq(i).find('td').eq(2).html(parseFloat(parseFloat(data.stocks[i].price)- parseFloat(trs.eq(i).find('td').eq(1).html())).toFixed(2));
			        var change = parseFloat(trs.eq(i).find('td').eq(2).html());
			        if(change < 0){
			            trs.eq(i).find('td').eq(2).css("color", "red");
			        }
			        else if(change > 0){
			            trs.eq(i).find('td').eq(2).css("color", "green");
			        }
			        else{
			            trs.eq(i).find('td').eq(2).html("");
			            trs.eq(i).find('td').eq(2).css("color", "");
			        }
			        trs.eq(i).find('td').eq(1).html(data.stocks[i].price);

                });
			},
			error: function(data) {
			    alert("error");
			}
		});
    }
});