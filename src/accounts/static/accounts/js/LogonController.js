var app = angular.module("account", ['ui.bootstrap']);

app.config(function($interpolateProvider) {
	  $interpolateProvider.startSymbol('{[{');
	  $interpolateProvider.endSymbol('}]}');
	});

app.directive('disabler', function ($compile) {
    return {
        scope: {
            ngModel: '=',
            form: '='
        },
        link: function (scope, elm, attrs) {
            var btnContents = $compile(elm.contents())(scope);
            scope.$watch(attrs.ngModel, function (value) {
                if (value) {
                    elm.html(scope.$eval(attrs.disabler));
                    elm.attr('disabled', true);
                } else {
                    elm.html('').append(btnContents);
                    elm.attr('disabled', false);
                }
            });
        }
    }
});

function SignInController($scope, $http, $modal) {
	
	$scope.messageText = 'Unknown error.';
	
    $scope.login = function () {
        $http(
        {
            url: '../accounts/loggedin',
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

    $scope.showMessage = function () {
        var modalInstance = $modal.open({
            templateUrl: 'message.html',
            controller: MessageCtrl,
            resolve: {
                messageText: function () {
                    return $scope.messageText;
                }
            }
        });
    };
}

function SignUpController($scope, $http, $modal) {

    $scope.isSaveDisabled = function () {
        console.log($scope.signUpForm.$invalid);
        return $scope.signUpForm.$invalid;
    };

    $scope.saveNewUser = function () {
        $scope.loading = true;
        $http(
        {
            url: '../accounts/signedup',
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

        $scope.showMessage = function () {
            var modalInstance = $modal.open({
                templateUrl: 'message.html',
                controller: MessageCtrl,
                resolve: {
                    messageText: function () {
                        return $scope.messageText;
                    }
                }
            });
        };
    };
};

var MessageCtrl = function ($scope, $modalInstance, messageText) {

    $scope.messageBody = messageText;

    $scope.ok = function () {
        $modalInstance.close();
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };
};
