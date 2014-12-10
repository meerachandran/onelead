from leaddb.models import Batch
from tastypie.resources import ModelResource

class EntryResource(ModelResource):
	class Meta:
		queryset = Batch.objects.all()
		resource_name = 'batch'
		include_resource_uri = False
		include_meta=False
	
		
