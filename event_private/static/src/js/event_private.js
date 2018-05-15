odoo.define('website_event.website_event_private', function (require) {

    var Widget = require('web.Widget');
    var web_editor_base = require('web_editor.base');

    // Catch registration form event, because of JS for attendee details
    var EventPrivateRegistrationForm = Widget.extend({
        start: function () {
            var self = this;
            var privateEvent;

            var res = this._super.apply(this.arguments).then(function () {
                privateEvent = $('#privateStatus').val() || false;
                if (privateEvent)
                    self.removeElement(['header .navbar-collapse', '#event_menu']);

            });
            return res
        },
        removeElement(els) {
            $.each(els, function (i, k) {
                $(k).remove();
            });
        }
    });

    web_editor_base.ready().then(function () {
        new EventPrivateRegistrationForm().appendTo($('#registration_form'));
    });

    return {
        EventPrivateRegistrationForm: EventPrivateRegistrationForm
    };

});