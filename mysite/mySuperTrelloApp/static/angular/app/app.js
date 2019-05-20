var Trello = angular.module('Trello', ["ngRoute"]);

Trello.config(['$routeProvider', function ($routeProvider) {
    // при загрузке отображаем базовый шаблон
    $routeProvider.when('/index', {
        templateUrl: '/static/angular/app/html/_main.html',
        controller: 'IndexController'
    });
}]);

Trello.controller('IndexController', ['$http', '$scope', function IndexController($http, $scope) {
    var self = this;
}]);


