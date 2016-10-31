from osv import osv, fields

class student_score(osv.osv):
    _name = 'student.score'
    _columns = {
            'student_id': fields.many2one('student.student', 'student name', select=True, ondelete='cascade'),
            'term': fields.char('Term', size=16),
            'score': fields.integer('Score', help="score"),
            }
    _defaults = {
                'term': 'middle',
                'score': 80,
            }
student_score()
