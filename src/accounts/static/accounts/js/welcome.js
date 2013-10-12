function HomeController($scope, $http) {
    $scope.master = {};

    $http.get('../accounts/info')
        .success(function (data) {
            $scope.user = {};
            angular.copy(data, $scope.user);
    });
}
