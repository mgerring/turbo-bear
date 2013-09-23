requirejs.config({
    shim: {
        'vendor/jquery.color': ['vendor/jquery'],
    }
});

requirejs(['vendor/jquery','vendor/jquery.color'], function() {
	jQuery(function($){

		var $signature_count = $('#signature_count .number');
		var $leaderboard 	 = $('#leaderboard .states');

		function updateCount(flash) {
			$.ajax({
				type:'GET',
				url:'/count',
				ifModified: true,
				dataType:'JSON',
				success:function(response) {
					if (typeof response == 'undefined') return false;
					
					if(flash != false) {
						$signature_count.animate({
							backgroundColor : '#E0D31B'
						},1000)
						.animate({
							backgroundColor : 'transparent'
						},1500);
					}

					$signature_count.text(response.count);
					$leaderboard.empty();
					$.each(response.states, function(i,state){
						console.log(state);
						$leaderboard.append( $('<li>').text(state[1].join(', ')+" ("+state[0]+")") );
					});
				},
				timeout:5000,
				complete:window.setTimeout(updateCount,2000)
			});
		};
		updateCount(false);
	});
});