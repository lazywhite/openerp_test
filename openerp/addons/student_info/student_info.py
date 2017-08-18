from osv import osv, fields

class student_student(osv.osv):
    _name = 'student.student'
    _rec_name = 'name'
    _columns = {
            'name': fields.char('Student Name', size=16, required=True, translate=True),
            'age': fields.integer('Age', readonly=True),
            'percent': fields.float('Percentage', help="Average marks of student out of 100"),
            'gender': fields.selection([('male', 'Male'), ('female', 'Female')], 'Gender'),
            'active': fields.boolean('Active'),
            'notes': fields.text('Details'),
            'scores': fields.one2many('student.score', 'student_id', string=u"student scores"),
            'state': fields.selection([
                ('new', 'New'),
                ('assigned', 'Assigned'),
                ('negotiation', 'Negotiation'),
                ('won', 'Won'),
                ('lost', 'Lost')], 'Stage'),

            }
    _defaults = {
                'name': 'Atul',
                'active': True,
            }
    def student_new(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state':'new'})
        return True

    def student_assigned(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state':'assigned'})
        return True

    def student_negotiation(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state':'negotiation'})
        return True

    def student_won(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state':'won'})
        return True

    def student_lost(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state':'lost'})
        return True

