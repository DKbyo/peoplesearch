angular.module("SearchApp")
.factory('Search', ['$resource', function($resource) {
	return $resource('http://127.0.0.1:8000/api/people/', null,
	{
		get: { method:'GET',isArray:true,cancellable:true,params:{
			format:"json"		
		}}
	});
}]);
