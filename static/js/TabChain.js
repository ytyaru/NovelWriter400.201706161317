var TabChain = TabChain || {};
TabChain.__isOn = false;
// TABキーが末端に到達したら先頭に戻す。
// isForcing: 強制実行するか否か
TabChain.Switch = function(isForcing=false) {
    if (TabChain.__isOn == $("#Regist").is(':visible') && !isForcing) { return; } // 変化なしのため終了
    console.log('process()');
    TabChain.__isOn = $("#Regist").is(':visible');
    $("#Title,#Content,#Regist").each(function(){ $(this).unbind('keydown'); }); // 関係DOMの全イベント削除（メモリリーク防止）
    var chains = [];
    var chain_ids = '#Title,#Content';
    if ($("#Regist").is(':visible')) { chain_ids += ',#Regist'; }
    $(chain_ids).each(function(i,v){ chains.push(v); });
    // 各要素にキーイベント登録する
    var process = function() {
        var first = chains[0];
        var last = chains[chains.length-1];
        for(el in chains){
            $(chains[el]).keydown(function(event){
                if (event.keyCode !== 9) { return; }
                if (event.target === last && !event.shiftKey) {
                    first.focus(1);
                    return false;
                }
                else if (event.target === first && event.shiftKey) {
                    last.focus(1);
                    return false;
                }
            });
        }
    };
    process();
}
