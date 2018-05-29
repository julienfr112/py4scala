from py4j.java_gateway import JavaGateway
from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
# gateway = JavaGateway.launch_gateway()                  # connect to the JVM
random = gateway.jvm.java.util.Random()   # create a java.util.Random instance
number1 = random.nextInt(10)              # call the Random.nextInt method
number2 = random.nextInt(10)
print(number1, number2)
addition_app = gateway.entry_point               # get the AdditionApplication instance
value = addition_app.smain()  # call the addition method
print(value)
