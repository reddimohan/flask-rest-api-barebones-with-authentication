from flask_restplus import Resource, Namespace, Resource, fields
api = Namespace('Leaves', description='')

from flask import request

@api.route('/leaverequests/<int:manager_id>')
class LeaveRequests(Resource):
    """docstring for LeaveRequests."""

    def __init__(self, arg):
        super(LeaveRequests, self).__init__()
        self.arg = arg


    def get(self, manager_id):
        print(manager_id)
        pass


new_leave_parser = api.parser()
new_leave_parser.add_argument('leave_type', type=str, help='Type of leave', location='form')
new_leave_parser.add_argument('leave_reason', type=str, help='Leave reason', location='form')
new_leave_parser.add_argument('from', type=str, help='From date', location='form')
new_leave_parser.add_argument('to', type=str, help='To Date', location='form')
@api.route('/leave/new')
class NewLeave(Resource):
    """docstring for NewLeave."""

    def __init__(self, arg):
        super(NewLeave, self).__init__()
        self.arg = arg

    @api.doc(parser= new_leave_parser)
    def post(self):
        pass


leave_type_parser = api.parser()
leave_type_parser.add_argument('type', type=str, help='Leave Type', location='form')
leave_type_parser.add_argument('status', type=str, help='Status', location='form')
@api.route('/leavetypes')
class LeaveType(Resource):
    """docstring for LeaveType."""

    def __init__(self, arg):
        super(LeaveType, self).__init__()
        self.arg = arg

    @api.doc(parser= leave_type_parser)
    def post(self):
        pass

    def get(self):
        print("Get Leave types")
        pass


# new_leave_parser = api.parser()
# new_leave_parser.add_argument('type', type=str, help='Leave Type', location='form')
# new_leave_parser.add_argument('status', type=str, help='Status', location='form')
# @api.route('/leavetype/new')
# class LeaveType(Resource):
#     """docstring for LeaveType."""
#
#     def __init__(self, arg):
#         super(LeaveType, self).__init__()
#         self.arg = arg
#
#     @api.doc(parser= user_register_parser)
#     def post(self):
#         pass
