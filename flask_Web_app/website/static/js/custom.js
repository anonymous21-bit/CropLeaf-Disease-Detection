(function() {
	'use strict';

	var tinyslider = function() {
		var el = document.querySelectorAll('.testimonial-slider');

		if (el.length > 0) {
			var slider = tns({
				container: '.testimonial-slider',
				items: 1,
				axis: "horizontal",
				controlsContainer: "#testimonial-nav",
				swipeAngle: false,
				speed: 700,
				nav: true,
				controls: true,
				autoplay: true,
				autoplayHoverPause: true,
				autoplayTimeout: 3500,
				autoplayButtonOutput: false
			});
		}
	};
	tinyslider();

	


	var sitePlusMinus = function() {

		var value,
    		quantity = document.getElementsByClassName('quantity-container');

		function createBindings(quantityContainer) {
	      var quantityAmount = quantityContainer.getElementsByClassName('quantity-amount')[0];
	      var increase = quantityContainer.getElementsByClassName('increase')[0];
	      var decrease = quantityContainer.getElementsByClassName('decrease')[0];
	      increase.addEventListener('click', function (e) { increaseValue(e, quantityAmount); });
	      decrease.addEventListener('click', function (e) { decreaseValue(e, quantityAmount); });
	    }

	    function init() {
	        for (var i = 0; i < quantity.length; i++ ) {
						createBindings(quantity[i]);
	        }
	    };

	    function increaseValue(event, quantityAmount) {
	        value = parseInt(quantityAmount.value, 10);

	        console.log(quantityAmount, quantityAmount.value);

	        value = isNaN(value) ? 0 : value;
	        value++;
	        quantityAmount.value = value;
	    }

	    function decreaseValue(event, quantityAmount) {
	        value = parseInt(quantityAmount.value, 10);

	        value = isNaN(value) ? 0 : value;
	        if (value > 0) value--;

	        quantityAmount.value = value;
	    }
	    
	    init();
		
	};
	sitePlusMinus();


})()
//login
// script.js
document.addEventListener("DOMContentLoaded", function() {
    const tabs = document.querySelectorAll(".tab-group .tab");
    const panes = document.querySelectorAll(".tab-content .tab-pane");

    tabs.forEach((tab, index) => {
        tab.addEventListener("click", function(e) {
            e.preventDefault();
            const activeTab = document.querySelector(".tab-group .tab.active");
            const activePane = document.querySelector(".tab-content .tab-pane.active");
            
            activeTab.classList.remove("active");
            activePane.classList.remove("active");

            tab.classList.add("active");
            panes[index].classList.add("active");
        });
    });
});


/*  ==========================================
    SHOW UPLOADED IMAGE
* ========================================== */
function readURL(input) {
	if (input.files && input.files[0]) {
		var reader = new FileReader();

		reader.onload = function (e) {
			$('#imageResult')
				.attr('src', e.target.result);
			$('#imageResult')
				.css('width', '100%');
		};
		reader.readAsDataURL(input.files[0]);
	}
}

$(function () {
    $('#upload').on('change', function () {
        readURL(input);
    });
});

/*  ==========================================
    SHOW UPLOADED IMAGE NAME
* ========================================== */
var input = document.getElementById('upload');
var infoArea = document.getElementById('upload-label');

if (input) {
	input.addEventListener('change', showFileName);
}

function showFileName(event) {
	var input = event.srcElement;
	var fileName = input.files[0].name;
	infoArea.textContent = 'File name: ' + fileName;
}
