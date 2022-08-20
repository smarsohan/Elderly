// Product Review Save
$("#addForm").submit(function(e){
	$.ajax({
		data:$(this).serialize(),
		method:$(this).attr('method'),
		url:$(this).attr('action'),
		dataType:'json',
		success:function(res){
			if(res.bool==true){
				$(".ajaxRes").html('Data has been added.');
				$("#reset").trigger('click');
				// Hide Button
				$(".reviewBtn").hide();
				// End

				// create data for review
				var _html='<blockquote class="blockquote text-left">';
				_html+='<h6>'+res.data.review_text+'</h6>';
				_html+='<footer"><p>-'+res.data.user+'</p>';
				_html+='<div class="ratings">';
				_html+='<div class="ratings-val" style="width: '+res.data.review_rating+'%;"></div>';
				_html+='</div>';
				_html+='</footer>';
				_html+='</blockquote>';
				_html+='</hr>';




				// Prepend Data
				$(".review-list").prepend(_html);

				// Hide Modal
				$("#productReview").modal('hide');

				// AVg Rating
				$(".avg-rating").text(res.avg_reviews.avg_rating.toFixed(1))
			}
		}
	});
	e.preventDefault();
});
// End