var app = angular.module("account", ['ui.bootstrap']);

function AcctController($scope, $http) {
    var master = {};
    angular.copy($scope.user, master);

    $http.get('../accounts/info')
        .success(function (data) {
            angular.copy(data, master);
            $scope.user = data;
        });

    $scope.onSaveClick = function () {
        $http(
            {
                url: '../accounts/updateinfo',
                method: 'POST',
                data: $scope.user,
                headers: { 'Content-Type': 'application/json' }
            }).success(function (data) {
                if (data.message == 'Success')
                    window.location.href = data.redirect;
                else {
                    $scope.messageText = data.message;
                    $scope.showMessage();
                    $scope.loading = false;
                }
            }).error(function (data) {
                $scope.messageText = data.message ? data.message : "Error message from the server.";
                $scope.showMessage();
                $scope.loading = false;
            });
    };

    $scope.onCancelClick = function () {
    	console.log('cancelled');
        angular.copy(master, $scope.user);
    };

    $scope.isCancelDisabled = function () {
        return angular.equals(master, $scope.user);
    };

    $scope.isSaveDisabled = function () {
        return angular.equals(master, $scope.user) || $scope.acctForm.$invalid
    };
};