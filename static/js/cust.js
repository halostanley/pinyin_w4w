function completeAjax(){
    $(".alert-success").remove();
}

function beforeSendAjax(){
    $(".alert-warning").remove();
    $(".alert-success").remove();
    $(".col-md-auto").append("<div class=\"alert alert-success\" role=\"alert\">正在提交请求...</div>");
}

function showTextCountAlert(){
    $(".alert-warning").remove();
    $(".col-md-auto").append("<div class=\"alert alert-warning\" role=\"alert\">请输入10个汉字以内</div>");
    setTimeout('$(".alert-warning").fadeOut()', 2000);
}

function showIsNotChineseAlert(){
    $(".alert-warning").remove();
    $(".col-md-auto").append("<div class=\"alert alert-warning\" role=\"alert\">请输入中文</div>");
    setTimeout('$(".alert-warning").fadeOut()', 2000);
}

function isChinese(text_input)
{
    let re=/[^\u4e00-\u9fa5]/;

    if(re.test(text_input)){
        return false;
    }
    return true;
}

function add_result(responseData){
    let obj = JSON.parse(responseData);
    if(document.getElementsByClassName("per-search").length >= 50){
       $(".per-search:last").remove();
   }

    let col_block = document.getElementsByClassName("per-search")[0].cloneNode(true);
    col_block.getElementsByClassName("col-block")[0].getElementsByClassName("result-1")[0].getElementsByTagName("a")[0].innerText = document.getElementsByClassName("form-control")[0].value;
    col_block.getElementsByClassName("col-block")[0].getElementsByClassName("result-2")[0].getElementsByTagName("a")[0].innerText = obj["pinyin"];
    $(".whole-block").prepend(col_block);

}

function ajax_request_word(text){
$(document).ready(function () {
   let send_info = {
       'src_text': text,
   };

   $.ajax({
       type: 'POST',
       url: 'https://cnpinyin.info/translate',
       crossDomain: false,
       data: send_info,
       dataType: 'text',
       async: true,
       beforeSend: beforeSendAjax(),
       complete: completeAjax(),
       success: function (responseData, status) {
           add_result(responseData);
       },
       error: function (responseData, status, error) {
           console.log(status);
           console.log(error);
           console.log(responseData);
           console.log('POST error.');
       }
   });
});
}

$('document').ready(function(){

    $('.form-control').keypress(function(e){
        if( document.getElementsByClassName("form-control")[0].value.length == 0 || document.getElementsByClassName("form-control")[0].value.length >10){
            showTextCountAlert();
            return;
        }

        if(e.which == 13){ //Enter key pressed
            let text = $('.form-control').val();
            if(isChinese(text)){
                ajax_request_word(text);
            }else{
                showIsNotChineseAlert();
            }

        }
    });

    $(".search-input-area").click(function() {
        $('#tab4').tab('show');
    });


    $(".hdr-search-btn").click(function() {
        $('#tab4').tab('show');
        $(".alert-warning").remove();
        if( document.getElementsByClassName("form-control")[0].value.length == 0 || document.getElementsByClassName("form-control")[0].value.length >10){
            showTextCountAlert();
            return;
        }

        let text = $('.form-control').val();
        if(isChinese(text)){
            ajax_request_word(text);
        }else{
            showIsNotChineseAlert();
        }
    });





});
