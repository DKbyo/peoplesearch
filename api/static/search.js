angular.module("SearchApp")
.controller("SearchCtrl",function($scope,Search){
	$scope.results =[];
	$scope.text ="Help";
	$scope.doSearch = function() {
		if($scope.searchText.length>=3){
			$scope.results = Search.get({search:$scope.searchText});
		}else {
			$scope.results = [];
		}
	}
});
