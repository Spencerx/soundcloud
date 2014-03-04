from soundcloud.resource import Resource, ResourceList
import sys

sys.path.append('/Users/ankitkumar/Documents/coding/205Consulting')
from OpenSource.bipartite_lda.base_class import bpg_recommender

class Soundcloud_recommender(bpg_recommender):
	def __init__(self, b, user, num_clusters = 6):
		bpg_recommender.__init__(self, b, num_clusters)
		self.user = user
		self.user_partition_index = self.initialize_feature_mappings(user)
		
	def print_node(self, node):
		print node.title + ' url: ' + node.permalink_url


	def additional_feature_factory(self, node):
		features = []
		features.append(node.favoritings_count/node.playback_count)
		return features


class KResource(Resource):
	def __init__(self, soundcloud_resource):
		super(KResource,self).__init__(soundcloud_resource.obj)

	def __eq__(self, other):
		if self.id == other.id:
			return True
		else:
			return False

	def __ne__(self, other):
		if self.__eq__(other):
			return False
		else:
			return True

class KResourceList(ResourceList):
	def __init__(self, resource_list):
		data = [KResource(resource) for resource in resource_list]
		super(ResourceList,self).__init__(data)



