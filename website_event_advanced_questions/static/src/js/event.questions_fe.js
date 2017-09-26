odoo.define('website_event.advanced_event', function (require) {
    
    var core = require('web.core');
        ajax = require('web.ajax'),
        widget = require('web.Widget');
        web_editor_base = require('web_editor.base');

    var _t = core._t,
        _lt = core._lt,
        qWeb = core.qweb;

    // Catch registration form event, because of JS for attendee details
    var AdvancedEventRegistrationForm = widget.extend({
        phAdvancedQuestions,
        start: function() {
            var self = this;
            var res = this._super.apply(this.arguments).then(function() {
                
                console.log('AdvancedEventRegistrationForm');

                $('#registration_form .a-submit')
                    .off('click')
                    .removeClass('a-submit')
                    .click(function (ev) {
                        self.onSubmitClick(ev);
                    });

                $('#btnNewUser').bind('click', self.onSubmitClick);

                //self.phAdvancedQuestions = $('#phAdvancedQuestions');

                // _aeForm = new aeForm();
                // console.log('_aeForm ', _aeForm);

                //tmplAdvancedQuestions

                // console.log('registration_attendee_details ', $('#registration_attendee_details'));

            });
            return res;
        },
        onSubmitClick: function(ev) {
            ev.preventDefault();
            ev.stopPropagation();

            console.log('RegistrationForm submit');

            return false;
            // var $form = $(ev.currentTarget).closest('form');
            // var post = {};
            // $("#registration_form select").each(function() {
            //     post[$(this).attr('name')] = $(this).val();
            // });
            // return ajax.jsonRpc($form.attr('action'), 'call', post).then(function (modal) {
            //     var $modal = $(modal);
            //     $modal.appendTo($form).modal();
            //     $modal.on('click', '.js_goto_event', function () {
            //         $modal.modal('hide');
            //     });
            // });
        },
        onNewUser: function(ev){
            ev.preventDefault();
            ev.stopPropagation();

            console.log('Add new user');

            return false;
        }
    });
    
    // var AeForm = widget.extend({
    //     template: "HomePageTemplate",
    //     start: function(){
    //         var self = this;
    //         return this._super.apply(this.arguments).then(function() {
    //             console.log('aeForm start');
    //         });
    //     }
    // });

    web_editor_base.ready().then(function(){
        var advanced_event_registration_form = new AdvancedEventRegistrationForm().appendTo($('#registration_form'));
        //var aeForm = new AeForm().appendTo($('#phAdvancedQuestions'));
    });
    
    return { 
        AdvancedEventRegistrationForm: AdvancedEventRegistrationForm
        //,AeForm: aeForm
    };
    
    });
    