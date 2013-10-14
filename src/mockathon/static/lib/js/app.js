var babybooApp = angular.module("babybooApp", ['ui.bootstrap']);

babybooApp.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});
