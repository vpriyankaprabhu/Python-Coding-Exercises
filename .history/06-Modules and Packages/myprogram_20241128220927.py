from mymodule import my_func

from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

#shows how to call function from simple module called mymodule
my_func()

#now lets try to call methods from package and subpackage
some_main_script.report_main()
mysubscript.SubPackage.sub_report()