// It most be a better way to do this.
$(function() {
    var hideClass = 'o_form_invisible',
        nextHidenElement;

    $('[name=dataTypes]').bind('change', function(e){
        var self = $(this),
            selectedText = self.find('option:selected').text().toLowerCase() || '',
            isMatch = selectedText.match(/checkbox|dropdown|radio/);

        if(!nextHidenElement)
            nextHidenElement = $(self.parent().next().children(':eq(0)'));
        
        nextHidenElement[isMatch ? 'removeClass' : 'addClass']('o_form_invisible');

    }).change();
});