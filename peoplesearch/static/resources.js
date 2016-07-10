angular.module("SearchApp")
.factory('Search', ['$resource', function($resource) {
	return $resource('/api/people/', null,
	{
		get: { method:'GET',isArray:true,cancellable:true,params:{
			format:"json"		
		}}
	});
}]);
