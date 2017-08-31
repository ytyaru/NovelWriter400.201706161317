$(function() {
    var _timeout_title;
    $('#Title').bind('focus', _focus_title);
    $('#Title').bind('blur', function() { clearTimeout(_timeout_title); });
    function _focus_title() {
        $("#TitleLength").text($("#Title").val().length);
        _timeout_title = setTimeout(_focus_title, 100);
    }
    
    var _timeout_content;
    $('#Content').bind('focus', _focus_content);
    $('#Content').bind('blur', function() { clearTimeout(_timeout_content); });
    function _focus_content() {
//        $("#ContentLength").text($("#Content").val().length);
        count = $("#Content").val().length;
        $("#ContentLength").text(count);
        $("#Helper").text(NovelWriter.States.Helper(count));
        state = NovelWriter.States.Any(count);
        _show_button(state);
        _timeout_content = setTimeout(_focus_content, 100);
    }
    
    function _show_button(state) {
        if (null === state) {
            $("#Regist").hide();
//            $('#Title,#Content').tabChain();
            TabChain.Switch();
        } else {
            $("#Regist").text("" + state.Max + "字小説を登録する");
            $("#Regist").show();
//            $('#Title,#Content,#Regist').tabChain();
            TabChain.Switch();
        }
    }
});

