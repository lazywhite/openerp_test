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
            'scores': fields.one2many('student.score', 'student_id', string=u"student scores")
            }
    _defaults = {
                'name': 'Atul',
                'active': True,
            }
student_student()
