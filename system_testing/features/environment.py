from support.driver_qa import DriverQA

def before_all(context):
	context.driverQA = DriverQA()
	context.driverQA.configDriver("firefox")

def after_all(context):
	context.driverQA.quit()