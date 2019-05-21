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
        self.addCard = function (desc) {
            /**
             * Добавляет новую карточку к доске
             */
            desc.cards.push({text: 'Новая карточка'});
        };
        self.removeCard = function (desc, card) {
            console.log(`desc=${desc}`);
            console.log(desc);
            console.log(`card=${card}`);
            console.log(card);
            desc.cards = desc.cards.filter(p => p.$$hashKey !== card.$$hashKey)
        }
    }
});