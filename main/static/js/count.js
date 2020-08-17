const targetForm = document.querySelector('.jss_content_form') 
const counted_text = document.querySelector('.counted_text')
//const-변하지 않는 값 지정,let-변하는 값 지정 // 
//. : class, # : id 지정 // 

targetForm.addEventListener("keyup", function() {
    counted_text.innerHTML = targetForm.value.length
})
//요소.addEventListener 이벤트를 감지했을때 실행되는 함수


