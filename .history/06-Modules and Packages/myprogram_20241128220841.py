from mymodule import my_func

from MyMainPackage import report_main
from MyMainPackage.SubPackage import sub_report

#shows how to call function from simple module called mymodule
my_func()

#now lets try to call methods from package and subpackage
MyMainPackage.report_main()
MyMainPackage.SubPackage.sub_report()
