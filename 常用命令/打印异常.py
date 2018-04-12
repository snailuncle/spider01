import traceback

try:
    def ss(s):
        return s/0
    s1=ss(9)
except Exception as e:
    print('****************traceback.format_exc():****************\n%s' % traceback.format_exc())
