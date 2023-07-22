## Approach 1:
# import sys
# sys.path.append("C:/Users/Admin/PycharmProjects/pythonProject3/Day9/package1")
# sys.path.append("C:/Users\Admin\PycharmProjects\pythonProject3\Day9\package1\subpackage")
#
# import module1
# module1.display()       #this is function from module1..
#
# import module2
# module2.display()       #this is function is from module2..


## Approach 2:
from package1 import module1
from package1.subpackage import module2

module1.display()       #this is function from module1..
module2.display()       #this is function from module2..

from selenium.webdeiver.chrom.server import Service