var app = angular.module("myChildren", []);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

function MyChildrenController($scope, $http) {
    $scope.master = {};

    $http.get('http://localhost/F5SeedProject/App/data/children.json')
    .success(function (data) {
        $scope.users = data;
    });
}
