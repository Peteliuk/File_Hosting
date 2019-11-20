document.querySelectorAll(".reg").forEach((element)=>{
	element.oninput = function(){
		let regex = new RegExp("^[a-zA-Z0-9]+$|^$");
		if(!regex.test(element.value)){
			alert("The unprohibited symbols are numbers and letters only!");
			element.value = null;
		}
	}
});

function readURL(input) {
	if (input.files && input.files[0]) {
		let reader = new FileReader();
		reader.onload = function (e) {
			let path = document.querySelector(".custom-file-input").value;
			document.querySelector(".custom-file-label").innerHTML = path.split(/(\\|\/)/g).pop();
			if(e.target.result.indexOf("image") != -1){
				$('#preview').css('display', "block");
				$('#preview').attr('src', e.target.result);
			} else {
				$('#preview').css('display', "none");
			}
		}
		reader.readAsDataURL(input.files[0]);
	}
}

let fileInput = document.querySelector(".custom-file-input");
let submitFile = document.querySelector(".submit-file");
submitFile.style.display = "none";
$("#file-input").change(function(){
	readURL(this);
	submitFile.style.display = "inline";
});

const imgFormats = ['png', 'jpg', 'jpeg', 'gif'];

let showFileImage = document.querySelectorAll(".personal-show-file-image");
showFileImage.forEach((el)=>{
	el.style = `display: none`;
	elUrl = el.childNodes[1].innerHTML;
	for(let i = 0; i < imgFormats.length; i++){
		if(elUrl.indexOf(imgFormats[i]) != -1){
			el.style = `display: block`;
			el.style = `background-image: url(${elUrl})`;
		}
	}
});