angular.module('Trello').component('descList', {
    templateUrl: '/static/angular/app/html/desc-list.template.html',
    controller: function DescListController($http, $scope) {
        var self = this;
        // получаем список досок с сервера
        $http.get('/mysupertrelloapp/get_descs').then(function (response) {
            console.log(response.data);
            self.descs = response.data;
            // для добавления карточек, убрать когда буду делать через контроллер
            descs = $scope.descs;
        });
    }
});