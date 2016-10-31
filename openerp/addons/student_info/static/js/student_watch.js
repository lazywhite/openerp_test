openerp.student_info = function(instance){
    instance.web.client_actions.add('student.watch', 'instance.student_watch.Action');

    instance.student_watch.Action = instance.web.Widget.extend({
        template: 'student_watch.action',
        events:{
            'click .oe_student_info_start button': 'watch_start',
            'click .oe_student_info_stop button': 'watch_stop',
        },
        init: function(){
            this._super.apply(this, arguments);
            this._start = null;
            this._stop = null;
        },
        update_counter: function(){
            var h, m, s;
            var diff = new Date() - this._start;
            s = diff / 1000;
            m = 
        }

    })
}
