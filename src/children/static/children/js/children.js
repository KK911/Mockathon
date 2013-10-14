var app = angular.module("myChildren", []);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

function MyChildrenController($scope, $http) {
    $scope.master = {};
    
    $http.get('../children')
    .success(function (data) {
        $scope.children = data;
    });
}
