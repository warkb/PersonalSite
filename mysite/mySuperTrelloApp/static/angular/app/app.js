var Trello = angular.module('Trello', ["ngRoute"]);

Trello.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/index', {
        templateUrl: '/static/angular/app/html/_main.html',
        controller: 'IndexController'
    });
}]);

loaded = false;

Trello.controller('IndexController', ['$http', '$scope', function IndexController($http, $scope) {
    var self = this;
    $http.get('/mysupertrelloapp/get_descs').then(function (response) {
        console.log(response.data);
        $scope.descs = response.data;
        descs = $scope.descs;
    });
}]);

// TODO: когда разберусь с контроллерами - сделать через контроллер
$(document).on('click', '[data-js-add-card]', function (event) {
    var newCard = $('<div>', {
        'class': 'card'
    }).text('Новая карточка');
    $(this).parent().find('.wrapper').append(newCard);
});

