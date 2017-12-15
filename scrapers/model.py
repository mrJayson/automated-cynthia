from abc import ABC, abstractmethod, abstractproperty
import csv

class Scraper(ABC):

	lender_list = []
	product_list = []
	
	@abstractproperty
	def base_url(self):
		pass

	def lenders(self, force_fetch=False):

		if self.lender_list == [] or force_fetch == True:
			lender_list = self._lenders()

			if not lender_list == [] and not lender_list == None:
				self.lender_list = lender_list
			
		return self.lender_list

	@abstractmethod
	def _lenders(self):
		pass
	
	@abstractmethod
	def products(self):
		pass
	
	def to_csv(self, products, file_name):

		# Prepare file_name
		if not file_name.endswith('.csv'):
			file_name += '.csv'

		file_handle = open(file_name,'w')

		keys = products[0].keys()

		csv_writer = csv.DictWriter(file_handle,keys)
		csv_writer.writeheader()
		csv_writer.writerows(products)

		file_handle.close()
