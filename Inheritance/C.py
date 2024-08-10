# from A import A
from A import A
from B import B


class C(B, A):
    def call_print_msg(self):
        self.print_msg()
