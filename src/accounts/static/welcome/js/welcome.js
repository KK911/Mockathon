function HomeController($scope, $http) {
    $scope.master = {};

    $http.get('http://localhost/F5SeedProject/App/data/users.json')
        .success(function (data) {
            $scope.user = {};
            angular.copy(data.user, $scope.user);
    });
}
