var NovelWriter = NovelWriter || {};

// 全書式のうちヒットした書式を返す
NovelWriter.FormattingStates = function(states) {
    var s =  FormattingStates.prototype;
    function FormattingStates(states) { if (Array.isArray(states)) { this.states = states; } else { this.states = []; } }
    Object.defineProperty(s, "States", { get: function() { return Object.assign([], this.states); } });
    s.Any = function(count) {
        for (var i = 0; i < this.states.length; i++) {
            if (this.states[i].IsFormatting(count)) { return this.states[i]; }
        }
        return null;
    }
    s.All = function(count) {
        for (var i = 0; i < this.states.length; i++) {
            if (!this.states[i].IsFormatting(count)) { return false; }
        }
        return true;
    }
    s.Helper = function(count) {
        // 近似値を求める。ソートされていること。1書式あたり最小値、最大値の2値があること。
        var threshold = [];
        for (var i = 0; i < this.states.length; i++) {
            if (this.states[i].IsFormatting(count)) { return ''; }
            threshold.push(this.states[i].Min);
            threshold.push(this.states[i].Max);
        }
        var diff = [];
        var index = 0;
        $(threshold).each(function(i,val){
            diff[i] = Math.abs(count - val);
            index = (diff[index] < diff[i]) ? index : i;
        });
        return 'あと ' + (threshold[index] - count) + ' 字で ' + this.states[parseInt(index/2)].Max + '字小説';
    }
    return new FormattingStates(states);
};

// 指定した文字以内かどうかを返す    
NovelWriter.Formatting = function(maxLength, minRate=0.9) {
    var s =  Formatting.prototype;
    function Formatting(maxLength, minRate) {
        if (maxLength <= 0) { throw "Formattingの最大長(maxLength)は0より大きい整数値にしてください。: " + maxLength; }
        else { this.maxLength = maxLength; }
        if (1 < minRate) { throw "FormattingのminRateは1より小さい少数値にしてください。: " + minRate; }
        else { this.minRate = minRate; }
    }
    // https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty
    Object.defineProperty(s, "Min", { get: function() { return (this.maxLength * this.minRate); } });
    Object.defineProperty(s, "Max", { get: function() { return this.maxLength; } });
    s.IsFormatting = function(count) {
        if ((this.maxLength * this.minRate) <= count && count <= this.maxLength) { return true; }
        else { return false; }
    };
    s.Diff = function(count) {
        if ((this.maxLength * this.minRate) <= count && count <= this.maxLength) { return 0; }
        maxDiff = this.maxLength - count;
        minDiff = (this.maxLength * this.minRate) - count;
        if (Math.abs(maxDiff) <= Math.abs(minDiff)) { return maxDiff; }
        else { return minDiff; }
    }
    return new Formatting(maxLength, minRate);
};

NovelWriter.__states = NovelWriter.FormattingStates([
    NovelWriter.Formatting(100), 
    NovelWriter.Formatting(200), 
    NovelWriter.Formatting(300), 
    NovelWriter.Formatting(400)]);
Object.defineProperty(NovelWriter, "States", { get: function() { return NovelWriter.__states; } });

