var app = angular.module("account", []);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

function HomeController($scope, $http) {
    $scope.master = {};

    $http.get('../accounts/info')
        .success(function (data) {
            $scope.user = {};
            angular.copy(data, $scope.user);
    });
}
