from EmployeeSelection import run_employee_selection
from ManageDeals import run_manage_deals
from ResourcesProvider import ResourcesProvider

resourcesProvider = ResourcesProvider("../data/")

chosenEmployeeOar = run_employee_selection(resourcesProvider)
run_manage_deals(resourcesProvider, chosenEmployeeOar)
