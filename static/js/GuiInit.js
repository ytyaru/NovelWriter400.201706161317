$(function() {
//    $('#Content').focus(); // 一度フォーカスをあてて文字カウントをクリアする
//    $('#Title').focus();
    Initialize();
    CreateButton();
    TabChain.Switch(isForcing=true);
//    $('#Title,#Content,#Regist').tabChain({onReadyFocus:true});
//    console.log($('#Title,#Content,#Regist'));
    
    function CallbackRegist(data) {
        console.log('CallbackRegist-------------------');
        json = JSON.parse(data);
        console.log(json);
        var archives = ''
        if (0 < json['Title'].length) { archives += json['Title'] + '\n\n'; }
        archives += json['Content'];
        $("#Archives pre").text(archives);
        $("#Archives").fadeIn("slow", function(){
            $(this).delay(5000).fadeOut(15000);
        });
//        $('#Title').val("");
//        $('#Content').val("");
//        $('#Content').focus(); // 一度フォーカスをあてて文字カウントをクリアする
//        $('#Title').focus();
        Initialize();
    }
    
    function Initialize() {
        $('#Title').val("");
        $('#Content').val("");
        $('#Content').focus(); // 一度フォーカスをあてて文字カウントをクリアする
        $('#Title').focus();
    }
    
    function CreateButton() {
        button_regist = $('<button type="submit" id="Regist" value="Regist">登録する</button>');
        button_regist.hide();
        button_regist.click(function() {
            $.ajax({
                type: 'POST',
                url: '/Regist',
                data: JSON.stringify({"Title": $('#Title').val(), "Content": $('#Content').val()}),
                contentType: 'application/json'
            })
            .done(function(data) {return CallbackRegist(data);})
            .fail(function() {});
        });
        $("#Details").append(button_regist)
    }
});

