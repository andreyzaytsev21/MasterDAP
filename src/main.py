from EmployeeSelection import run_employee_selection
from ManageDeals import run_manage_deals
from utils.storage.ResourcesManager import ResourcesProvider

resources_provider = ResourcesProvider("../data/")

chosen_employee = run_employee_selection(resources_provider)
run_manage_deals(resources_provider, chosen_employee)
